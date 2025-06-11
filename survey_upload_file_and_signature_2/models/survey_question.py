# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
from odoo import fields, models, _
import json

class SurveyQuestion(models.Model):
    """
    This class extends the 'survey.question' model to add new functionality
    for file uploads.
    """
    _inherit = 'survey.question'

    question_type = fields.Selection(
        selection_add=[('upload_file', 'Upload File'), ('signature', 'signature')],
        help='Select the type of question to create.')
    upload_multiple_file = fields.Boolean(string='Upload Multiple File',
                                          help='Check this box if you want to '
                                               'allow users to upload '
                                               'multiple files')

    def validate_question(self, answer, comment=None):
        res = super(SurveyQuestion, self).validate_question(answer, comment)
        if self.question_type == 'signature':
            return self._validate_sinature(answer)
        if self.question_type == 'upload_file':
            return self._validate_upload_file(answer)
        return res

    def _validate_upload_file(self, answer):
        if self.constr_mandatory:
            filename = json.loads(answer[1])
            if not filename:
                if self.constr_error_msg:
                    return {self.id: _(self.constr_error_msg)}
                return {self.id: _('This question requires an answer')}
        return {}

    def _validate_sinature(self, answer):
        # Email format validation
        # all the strings of the form "<something>@<anything>.<extension>" will be accepted
        if self.constr_mandatory:
            if not answer:
                if self.constr_error_msg:
                    return {self.id: _(self.constr_error_msg)}
                return {self.id: _('This question requires an answer')}
        return {}
