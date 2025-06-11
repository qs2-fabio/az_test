/** @odoo-module **/

import { loadJS } from "@web/core/assets";
import { registry } from "@web/core/registry"
import { NameAndSignatureCustom } from "./name_and_signature_extend";
import { Component, useState, onWillStart, onWillUpdateProps } from "@odoo/owl";

// Extend the survey functionality or listen for specific question type
export class SurveySignatureComponent extends Component {
    static template= "survey_upload_file_and_signature.SurveySignatureComponent";
    static components = { NameAndSignatureCustom};
    setup() {
        this.signature = useState({ name: ''});
        this.nameAndSignatureProps = {
            signature: this.signature,
            fontColor: "black",
        };
        super.setup();
    }
    getNameAndSignatureProps() {
        return {
            signature: '', 
        };
    }
};

registry.category("public_components").add("surveysignaturecomponent", SurveySignatureComponent);