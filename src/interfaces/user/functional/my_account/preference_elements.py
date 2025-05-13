class PreferenceElements:
    """
    Class containing XPath locators for the Preference section.
    These elements are for the preference settings fields.
    """

    # Preference info group
    div_preference_info_group = "//div[@class='info-group'][.//span[text()='Preference']]"
    div_preference_title = "//div[@class='info-group'][.//span[text()='Preference']]/div[@class='title']"
    span_preference_title_text = "//div[@class='info-group'][.//span[text()='Preference']]//span[@class='text']"
    
    # Preference info fields
    div_form_horizontal_preference = "//div[@class='info-group'][.//span[text()='Preference']]/div[@class='form-horizontal']"
    
    # Target Country field
    div_form_group_target_country = "//div[@class='info-group'][.//span[text()='Preference']]//div[@class='form-group'][.//label[text()='Target Country']]"
    label_target_country = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Target Country']"
    select_target_country = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']"
    option_select_one = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[text()='Select One']"
    option_malaysia = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='MY']"
    option_bangladesh = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='BD']"
    option_india = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='IN']"
    option_indonesia = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='ID']"
    option_japan = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='JP']"
    option_south_korea = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='KR']"
    option_thailand = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='TH']"
    option_vietnam = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='VN']"
    option_china = "//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='CN']"
    span_validation_target_country = "//span[@data-valmsg-for='AccountInformation.TargetCountryCode']"
    
    # Language field
    div_form_group_language = "//div[@class='info-group'][.//span[text()='Preference']]//div[@class='form-group'][.//label[text()='Language']]"
    label_language = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Language']"
    p_language_value = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Language']/../../div[2]/p"
    
    # Affiliate Currency field
    div_form_group_affiliate_currency = "//div[@class='info-group'][.//span[text()='Preference']]//div[@class='form-group'][.//label[text()='Affiliate Currency']]"
    label_affiliate_currency = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Affiliate Currency']"
    p_affiliate_currency_value = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Affiliate Currency']/../../div[2]/p"
    
    # Default Base Currency field
    div_form_group_default_base_currency = "//div[@class='info-group'][.//span[text()='Preference']]//div[@class='form-group'][.//label[text()='Default Base Currency']]"
    label_default_base_currency = "//div[@class='info-group'][.//span[text()='Preference']]//label[text()='Default Base Currency']"
    select_default_base_currency = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']"
    option_myr = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='2']"
    option_usd = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='3']"
    option_thb = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='4']"
    option_cny = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='13']"
    option_idr = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='15']"
    option_vnd = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='51']"
    option_inr = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='61']"
    option_bdt = "//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='74']"
    div_info_container = "//div[@class='info-group'][.//span[text()='Preference']]//div[@class='info-container col-sm-1']"
    span_glyphicon_info = "//div[@class='info-group'][.//span[text()='Preference']]//span[@class='glyphicon glyphicon-info-sign']"
    
    def get_target_country_option_by_value(self, value):
        """Get target country option by value"""
        return f"//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[@value='{value}']"
    
    def get_target_country_option_by_text(self, text):
        """Get target country option by text"""
        return f"//div[@class='info-group'][.//span[text()='Preference']]//select[@name='TargetCountryCode']/option[contains(text(), '{text}')]"
    
    def get_default_base_currency_option_by_value(self, value):
        """Get default base currency option by value"""
        return f"//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[@value='{value}']"
    
    def get_default_base_currency_option_by_text(self, text):
        """Get default base currency option by text"""
        return f"//div[@class='info-group'][.//span[text()='Preference']]//select[@id='DefaultBaseCurrency']/option[text()='{text}']" 