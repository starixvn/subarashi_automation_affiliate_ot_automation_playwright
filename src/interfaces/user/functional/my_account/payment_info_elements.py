class PaymentInfoElements:
    """
    Class containing XPath locators for the Payment Information section.
    These elements are for the payment details fields.
    """

    # Payment info group
    div_payment_info_group = "//div[@class='info-group'][.//span[text()='Payment Information']]"
    div_payment_title = "//div[@class='info-group'][.//span[text()='Payment Information']]/div[@class='title']"
    span_payment_title_text = "//div[@class='info-group'][.//span[text()='Payment Information']]//span[@class='text']"
    
    # Payment info fields
    div_form_horizontal_payment = "//div[@class='info-group'][.//span[text()='Payment Information']]/div[@class='form-horizontal']"
    
    # Payment Method field
    div_form_group_payment_method = "//div[@class='info-group'][.//span[text()='Payment Information']]//div[@class='form-group'][.//label[text()='Payment Method']]"
    label_payment_method = "//div[@class='info-group'][.//span[text()='Payment Information']]//label[text()='Payment Method']"
    label_player_account = "//div[@class='info-group'][.//span[text()='Payment Information']]//label[contains(text(), '12BET Player Account')]"
    input_player_account = "//div[@class='info-group'][.//span[text()='Payment Information']]//label[contains(text(), '12BET Player Account')]/input"
    
    # User Name field
    div_form_group_player_username = "//div[@class='info-group'][.//span[text()='Payment Information']]//div[@class='form-group'][.//label[text()='User Name']]"
    label_player_username = "//div[@class='info-group'][.//span[text()='Payment Information']]//label[@for='PlayerUsername']"
    p_player_username = "//div[@class='info-group'][.//span[text()='Payment Information']]//p[@id='PlayerUsername']"
    span_validation_player_username = "//span[@data-valmsg-for='PlayerUsername']"
    
    # Button block
    div_button_block = "//div[@class='info-group'][.//span[text()='Payment Information']]/../div[@class='col-sm-offset-3 button-block']"
    button_submit = "//button[@id='btnMyAccountSubmit']"
    button_cancel = "//button[@id='btnCancel']"
    
    def get_payment_form_group_by_label(self, label_text):
        """Get payment form group by label text"""
        return f"//div[@class='info-group'][.//span[text()='Payment Information']]//div[@class='form-group'][.//label[text()='{label_text}']]"
    
    def get_payment_field_value_by_label(self, label_text):
        """Get payment field value by label text"""
        return f"//div[@class='info-group'][.//span[text()='Payment Information']]//div[@class='form-group'][.//label[text()='{label_text}']]/div[2]/p" 