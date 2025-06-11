# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
from odoo import api, fields, models, _
import textwrap


class SurveyUserInputLine(models.Model):
    """
    This class extends the 'survey.user_input.line' model to add additional
    fields and constraints for file uploads.
    Methods:
        _check_answer_type_skipped:Check that a line's answer type is
        not set to 'upload_file' if the line is skipped
    """
    _inherit = "survey.user_input.line"

    answer_type = fields.Selection(
        selection_add=[('upload_file', 'Upload File'), ('signature', 'Signature')],
        help="The type of answer for this question (upload_file if the user "
             "is uploading a file).")
    value_file_data_ids = fields.Many2many('ir.attachment',
                                           help="The attachments "
                                                "corresponding to the user's "
                                                "file upload answer, if any.")

    value_signature = fields.Image(string="Signature")

    @api.constrains('skipped', 'answer_type')
    def _check_answer_type_skipped(self):
        """ Check that a line's answer type is not set to 'upload_file' if
        the line is skipped."""
        for line in self:
            if line.answer_type != 'upload_file' and line.answer_type != 'signature':
                super(SurveyUserInputLine, line)._check_answer_type_skipped()

    @api.depends(
        'answer_type', 'value_text_box', 'value_numerical_box',
        'value_char_box', 'value_date', 'value_datetime',
        'suggested_answer_id.value', 'matrix_row_id.value',
    )
    def _compute_display_name(self):
        for line in self:
            if line.answer_type == 'char_box':
                line.display_name = line.value_char_box
            elif line.answer_type == 'text_box' and line.value_text_box:
                line.display_name = textwrap.shorten(line.value_text_box, width=50, placeholder=" [...]")
            elif line.answer_type == 'numerical_box':
                line.display_name = line.value_numerical_box
            elif line.answer_type == 'date':
                line.display_name = fields.Date.to_string(line.value_date)
            elif line.answer_type == 'datetime':
                line.display_name = fields.Datetime.to_string(line.value_datetime)
            elif line.answer_type == 'scale':
                line.display_name = line.value_scale
            elif line.answer_type == 'suggestion':
                if line.matrix_row_id:
                    line.display_name = f'{line.suggested_answer_id.value}: {line.matrix_row_id.value}'
                else:
                    line.display_name = line.suggested_answer_id.value
            elif line.answer_type == 'upload_file':
                line.display_name = ', '.join(line.value_file_data_ids.mapped('name'))
            elif line.answer_type == 'signature' and line.value_signature:
                line.display_name = _("Signature Provided")

            if not line.display_name:
                line.display_name = _('Skipped')
