# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
from odoo import models
import base64
import json
class SurveyUserInput(models.Model):
    """
    This class extends the 'survey.user_input' model to add custom
    functionality for saving user answers.

    Methods:
        _save_lines: Save the user's answer for the given question
        _save_line_file:Save the user's file upload answer for the given
        question
        _get_line_answer_file_upload_values:
        Get the values to use when creating or updating a user input line
        for a file upload answer
    """
    _inherit = "survey.user_input"

    def _save_lines(self, question, answer, comment=None,
                    overwrite_existing=False):
        """Save the user's answer for the given question."""
        old_answers = self.env['survey.user_input.line'].search([
            ('user_input_id', '=', self.id),
            ('question_id', '=', question.id), ])
        if question.question_type in ['upload_file', 'signature']:
            res = self._save_line_simple_answer(question, old_answers, answer)
        else:
            res = super()._save_lines(question, answer, comment,
                                      overwrite_existing)
        return res

    def _save_line_simple_answer(self, question, old_answers, answer):
        """ Save the user's file upload answer for the given question."""
        if question.question_type in ['upload_file', 'signature']:
            vals = {}
            if question.question_type == 'upload_file':
                vals = self._get_line_answer_file_upload_values(question, 'upload_file', answer)
            if question.question_type == 'signature':
                vals = self._get_line_answer_signature_upload_values(question, 'signature', answer)
            if old_answers and vals:
                old_answers.write(vals)
                return old_answers
            else:
                return self.env['survey.user_input.line'].create(vals)
        else:
            vals = self._get_line_answer_values(question, answer, question.question_type)
            if old_answers and vals:
                old_answers.write(vals)
                return old_answers
            else:
                return self.env['survey.user_input.line'].create(vals)

    def _get_line_answer_signature_upload_values(self, question, answer_type, answer):
        vals = {
            'user_input_id': self.id,
            'question_id': question.id,
            'skipped': False,
            'answer_type': answer_type,
        }
        if answer_type == 'signature':
            file_data = answer
            if file_data:
                vals['value_signature'] = file_data
        return vals

    def _get_line_answer_file_upload_values(self, question, answer_type, answer):
        """Get the values to use when creating or updating a user input line
        for a file upload answer."""
        vals = {
            'user_input_id': self.id,
            'question_id': question.id,
            'skipped': False,
            'answer_type': answer_type,
        }
        if answer_type == 'upload_file':
            file_data = json.loads(answer[0])
            file_name = json.loads(answer[1])
            attachment_ids = []
            if file_name:
                for file in range(len(json.loads(answer[1]))):
                    attachment = self.env['ir.attachment'].create({
                        'name': file_name[file],
                        'type': 'binary',
                        'datas': file_data[file],
                        'res_model': 'survey.user_input',
                        'res_id': self.id
                    })
                    attachment_ids.append(attachment.id)
                vals['value_file_data_ids'] = attachment_ids
        return vals
