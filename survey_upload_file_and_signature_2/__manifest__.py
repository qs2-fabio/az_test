# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).
{
    'name': "File Upload and Signature In Survey",
    'version': "18.0.1.1",
    'category': 'Extra Tools',
    'summary': "Survey File Upload | Signature in Surveys | Multiple Attachments in Surveys | Survey Document Upload | File Upload in Survey Forms | Digital Signatures for Surveys | Survey Signature Field | Upload Files in Survey | Multiple File Attachments | Survey with Signatures | Document Upload Feature in Surveys | Survey Signature Option | File and Signature Support in Surveys | Upload Files for Survey Responses | Survey Form Attachments",
    'description': 'This module enhances the Survey functionality by enabling users to upload files and capture signatures directly in survey forms. Multiple file attachments are supported, making it easier to collect detailed responses and approvals.',
    'author': "Kanak Infosystems LLP.",
    'company': "Kanak Infosystems LLP.",
    'maintainer': "Kanak Infosystems LLP.",
    'website': "https://kanakinfosystems.com",
    'depends': ['survey'],
    'assets': {
        'survey.survey_assets': [
            'survey_upload_file_and_signature/static/src/signatures/name_and_signature_extend.js',
            'survey_upload_file_and_signature/static/src/js/survey_form_attachment.js',
            'survey_upload_file_and_signature/static/src/js/SurveyFormWidget.js',
            'survey_upload_file_and_signature/static/src/signatures/*',
        ],
    },
    'data': [
        'views/survey_question_views.xml',
        'views/survey_user_views.xml',
        'views/survey_templates.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': "OPL-1",
    'application': False,
    'installable': True,
    'auto_install': False,
    'price': 30,
    'currency': 'EUR',
}
