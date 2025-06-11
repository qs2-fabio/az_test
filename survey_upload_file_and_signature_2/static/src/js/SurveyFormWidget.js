/** @odoo-module */
import SurveyFormWidget from '@survey/js/survey_form';
import SurveySignatureComponent from '../signatures/survey_signature';
import { Component } from "@odoo/owl";
import { makeEnv, startServices } from "@web/env";

SurveyFormWidget.include({
    /** Get all question answers by question type */
    _prepareSubmitValues(formData, params) {
        this._super(...arguments);
        this.$('[data-question-type]').each(function () {
        if ($(this).data('questionType') === 'upload_file'){
             params[this.name] = [$(this).attr('data-oe-data'), $(this).attr('data-oe-file_name')];
        }
        if ($(this).data('questionType') === 'signature' && this.nodeName == 'INPUT'){
             params[this.name] = $(this).attr('data-oe-data') || '';
        }
        });
    },
    _nextScreen: async function (nextScreenPromise, options) {
        var res = await this._super(...arguments);
        await this.mountSignatureComponent();
        return res;
    },
    async mountSignatureComponent() {
        const el = document.querySelector("#survey_signature_component");
        if(el){
            if(!$(el).find('.o_web_sign_name_input').length){
                await Component.env.services.public_component.destroyComponents();
                await Component.env.services.public_component.mountComponents();
            }
        }
    }
});
