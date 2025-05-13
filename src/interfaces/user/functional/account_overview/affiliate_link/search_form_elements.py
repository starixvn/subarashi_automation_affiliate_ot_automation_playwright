class SearchFormElements:
    """
    This class contains XPath locators for search form elements on the affiliate page.
    """
    
    # Main container elements
    div_search_form = "//div[@id='searchForm']"
    div_info_group = "//div[@id='searchForm'][@class='info-group']"
    div_title = "//div[@id='searchForm']/div[@class='title']"
    span_title_text = "//div[@id='searchForm']/div[@class='title']/span[@class='text']"
    
    # Search container
    div_search_container = "//div[@id='searchForm']/div[@class='search-container']"
    form_search = "//div[@class='search-container']/form"
    
    # Form columns
    div_column_form_first = "(//div[@class='search-container']/form/div[@class='column-form'])[1]"
    div_column_form_second = "(//div[@class='search-container']/form/div[@class='column-form'])[2]"
    
    # Form groups in first column
    div_form_group_link_type = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='AffLinkType']]"
    label_link_type = "//label[@class='control-label'][@for='AffLinkType']"
    div_control_input_link_type = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='AffLinkType']]/div[@class='control-input']"
    select_link_type = "//select[@id='AffLinkType']"
    option_affiliate_link = "//select[@id='AffLinkType']/option[@value='AffiliateLink']"
    
    div_form_group_target_country = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='TargetCountry']]"
    label_target_country = "//label[@class='control-label'][@for='TargetCountry']"
    div_control_input_target_country = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='TargetCountry']]/div[@class='control-input']"
    select_target_country = "//select[@id='TargetCountry']"
    
    div_form_group_language = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Language']]"
    label_language = "//label[@class='control-label'][@for='Language']"
    div_control_input_language = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Language']]/div[@class='control-input']"
    select_language = "//select[@id='Language']"
    
    # Form groups in second column
    div_form_group_domain = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Domain']]"
    label_domain = "//label[@class='control-label'][@for='Domain']"
    div_control_input_domain = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Domain']]/div[@class='control-input']"
    select_domain = "//select[@id='Domain']"
    
    div_form_group_page = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Page']]"
    label_page = "//label[@class='control-label'][@for='Page']"
    div_control_input_page = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Page']]/div[@class='control-input']"
    select_page = "//select[@id='Page']"
    
    div_form_group_channel = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Channel']]"
    label_channel = "//label[@class='control-label'][@for='Channel']"
    div_control_input_channel = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Channel']]/div[@class='control-input']"
    select_channel = "//select[@id='Channel']"
    
    # Generate button
    div_form_group_button = "//div[@class='form-group flex-sm-boostrap flex-center form-group-button']"
    label_none = "//label[@class='control-label none-label']"
    button_generate = "//button[@id='btnGenQRCode']"
    
    # Helper methods to get specific options
    def get_target_country_option(self, value):
        """Get a target country option by its value."""
        return f"//select[@id='TargetCountry']/option[@value='{value}']"
    
    def get_target_country_option_by_text(self, text):
        """Get a target country option by its display text."""
        return f"//select[@id='TargetCountry']/option[contains(text(), '{text}')]"
    
    def get_language_option(self, value):
        """Get a language option by its value."""
        return f"//select[@id='Language']/option[@value='{value}']"
    
    def get_language_option_by_text(self, text):
        """Get a language option by its display text."""
        return f"//select[@id='Language']/option[text()='{text}']"
    
    def get_domain_option(self, value):
        """Get a domain option by its value."""
        return f"//select[@id='Domain']/option[@value='{value}']"
    
    def get_domain_option_by_text(self, text):
        """Get a domain option by its display text."""
        return f"//select[@id='Domain']/option[contains(text(), '{text}')]"
    
    def get_page_option(self, value):
        """Get a page option by its value."""
        return f"//select[@id='Page']/option[@value='{value}']"
    
    def get_page_option_by_text(self, text):
        """Get a page option by its display text."""
        return f"//select[@id='Page']/option[text()='{text}']"
    
    def get_channel_option(self, value):
        """Get a channel option by its value."""
        return f"//select[@id='Channel']/option[@value='{value}']"
    
    def get_channel_option_by_text(self, text):
        """Get a channel option by its display text."""
        return f"//select[@id='Channel']/option[text()='{text}']"
    
    def get_add_new_channel_option(self):
        """Get the 'Add new...' channel option."""
        return "//select[@id='Channel']/option[@value='add-new']" 