/** @odoo-module **/

import { NameAndSignature } from "@web/core/signature/name_and_signature";
import { onMounted, useEffect } from "@odoo/owl";

export class NameAndSignatureCustom extends NameAndSignature {
	setup() {
        this.writedrawTimeout = null;
        super.setup();
        useEffect(
            (el) => {
                if (el) {
                    this.signaturePad.addEventListener("endStroke", () => {
                        this.onSignatureChange();
                    });
                    
                }
            },
            () => [this.signatureRef.el]
        );
    }
    async onChangeSignLoadInput(ev) {
        await super.onChangeSignLoadInput(ev);
        this.onSignatureChange();
    }
    async drawCurrentName() {
        await super.drawCurrentName();
        this.onSignatureChange();

    }
    onSignatureChange(){
        var self = this;
        if(this.props.signature.getSignatureImage()){
            clearTimeout(this.writedrawTimeout);
            this.writedrawTimeout = setTimeout(()=>{
                if(this.isSignatureEmpty){
                    var $inputsignature = $(this.signaturePad.canvas).closest('.o_survey_signature_container').find("input[data-question-type='signature']");
                    if($inputsignature.length){
                        $inputsignature.attr('data-oe-data', '');
                    } 
                }else{
                    var datas = this.props.signature.getSignatureImage().split(",")[1];
                    var $inputsignature = $(this.signaturePad.canvas).closest('.o_survey_signature_container').find("input[data-question-type='signature']");
                    if($inputsignature.length){
                        $inputsignature.attr('data-oe-data', datas);
                    } 
                }
               
            }, 0);
            
        }
    }
};