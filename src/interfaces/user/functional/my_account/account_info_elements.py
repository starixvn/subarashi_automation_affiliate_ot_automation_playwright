class AccountInfoElements:
    """
    Class containing XPath locators for the Account Information section.
    These elements are for the main account information fields.
    """

    # Main container elements
    div_account_information = "//div[@class='account-information']"
    div_page_title = "//div[@class='account-information']/div[@class='page-title']"
    span_page_title_text = "//div[@class='account-information']/div[@class='page-title']/span[@class='text']"
    
    # Alert message
    div_alert = "//div[@id='messageResult']"
    
    # Form element
    form_account = "//form[@id='accountForm']"
    input_request_verification_token = "//input[@name='__RequestVerificationToken']"
    
    # Account info group
    div_account_info_group = "//div[@class='info-group'][.//span[text()='Account Information']]"
    div_account_title = "//div[@class='info-group'][.//span[text()='Account Information']]/div[@class='title']"
    span_account_title_text = "//div[@class='info-group'][.//span[text()='Account Information']]//span[@class='text']"
    
    # Account info fields
    div_form_horizontal_account = "//div[@class='info-group'][.//span[text()='Account Information']]/div[@class='form-horizontal']"
    
    # Username field
    div_form_group_username = "//div[@class='info-group'][.//span[text()='Account Information']]//div[@class='form-group'][.//label[text()='User Name']]"
    label_username = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='User Name']"
    p_username_value = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='User Name']/../../div[2]/p"
    
    # Password field
    div_form_group_password = "//div[@class='info-group'][.//span[text()='Account Information']]//div[@class='form-group'][.//label[text()='Password']]"
    label_password = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='Password']"
    p_password_value = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='Password']/../../div[2]/p"
    a_change_password = "//div[@class='info-group'][.//span[text()='Account Information']]//a[text()='Change']"
    
    # Affiliate ID field
    div_form_group_affiliate_id = "//div[@class='info-group'][.//span[text()='Account Information']]//div[@class='form-group'][.//label[text()='Affiliate ID']]"
    label_affiliate_id = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='Affiliate ID']"
    p_affiliate_id_value = "//div[@class='info-group'][.//span[text()='Account Information']]//label[text()='Affiliate ID']/../../div[2]/p"
    
    # Action buttons
    button_submit = "//button[@id='btnMyAccountSubmit']"
    button_cancel = "//button[@id='btnCancel']"
    
    def get_form_group_by_label(self, label_text):
        """Get form group by label text"""
        return f"//div[@class='form-group'][.//label[text()='{label_text}']]"
    
    def get_field_value_by_label(self, label_text):
        """Get field value by label text"""
        return f"//div[@class='form-group'][.//label[text()='{label_text}']]/div[2]/p" 