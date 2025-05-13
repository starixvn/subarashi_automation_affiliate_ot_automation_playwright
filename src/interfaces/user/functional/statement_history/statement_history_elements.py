class StatementHistoryElements:
    """
    Class containing XPath locators for the Statement History elements page.
    These elements are for the main statement history section.
    """

    # Main container elements
    div_sub_content = "//div[@class='sub-content']"
    div_page_title = "//div[@class='page-title']"
    span_text = "//div[@class='page-title']/span[@class='text']"
    
    # Base currency filter elements
    div_form_filter = "//div[@class='form-inline form-filter']"
    div_form_group = "//div[@class='form-inline form-filter']/div[@class='form-group']"
    label_base_currency = "//div[@class='form-inline form-filter']//label[text()='Base Currency:']"
    select_base_currency = "//select[@id='base-currency']"
    
    # Currency options
    option_myr = "//select[@id='base-currency']/option[@value='2']"
    option_usd = "//select[@id='base-currency']/option[@value='3']"
    option_thb = "//select[@id='base-currency']/option[@value='4']"
    option_cny = "//select[@id='base-currency']/option[@value='13']"
    option_idr = "//select[@id='base-currency']/option[@value='15']"
    option_vnd = "//select[@id='base-currency']/option[@value='51']"
    option_inr = "//select[@id='base-currency']/option[@value='61']"
    option_bdt = "//select[@id='base-currency']/option[@value='74']"
    
    # Info group container
    div_info_group = "//div[@class='info-group']"
    
    # Hidden input elements
    input_is_click_breadcumb = "//input[@id='isClickBreadcumb']"
    
    def get_currency_option_by_value(self, value):
        """Get currency option by value"""
        return f"//select[@id='base-currency']/option[@value='{value}']"
    
    def get_currency_option_by_text(self, text):
        """Get currency option by text"""
        return f"//select[@id='base-currency']/option[text()='{text}']" 