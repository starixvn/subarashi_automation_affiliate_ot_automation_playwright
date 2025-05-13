class RevenueReportFilterElements:
    """
    Class containing XPath locators for the Revenue Report filter section.
    These elements are for the filter panel with year and base currency selectors.
    """

    # Main container elements
    div_main_content = "//div[@class='main-content']"
    div_container_fluid = "//div[@class='main-content']/div[@class='container-fluid']"
    div_main_panel = "//div[@id='mainPanel']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_page_title_text = "//div[@class='page-title']/span[@class='text']"
    
    # Filter panel container
    div_info_group = "//div[@class='info-group']"
    div_panel_custom = "//div[@class='info-group']/div[@class='panel custom-panel']"
    div_panel_body = "//div[@class='info-group']/div[@class='panel custom-panel']/div[@class='panel-body']"
    
    # Filter form
    form_filter = "//form[@class='form-inline form-filter']"
    
    # Year filter
    div_form_group_year = "//form[@class='form-inline form-filter']/div[@class='form-group'][./label[text()='Year:']]"
    label_year = "//form[@class='form-inline form-filter']//label[text()='Year:']"
    select_year = "//select[@id='year']"
    option_2025 = "//select[@id='year']/option[@value='2025']"
    option_2024 = "//select[@id='year']/option[@value='2024']"
    option_2023 = "//select[@id='year']/option[@value='2023']"
    option_2022 = "//select[@id='year']/option[@value='2022']"
    option_2021 = "//select[@id='year']/option[@value='2021']"
    option_2020 = "//select[@id='year']/option[@value='2020']"
    option_2019 = "//select[@id='year']/option[@value='2019']"
    option_2018 = "//select[@id='year']/option[@value='2018']"
    
    # Base Currency filter
    div_form_group_currency = "//form[@class='form-inline form-filter']/div[@class='form-group'][./label[text()='Base Currency:']]"
    label_base_currency = "//form[@class='form-inline form-filter']//label[text()='Base Currency:']"
    select_base_currency = "//select[@id='base-currency']"
    option_myr = "//select[@id='base-currency']/option[@value='2']"
    option_usd = "//select[@id='base-currency']/option[@value='3']"
    option_thb = "//select[@id='base-currency']/option[@value='4']"
    option_cny = "//select[@id='base-currency']/option[@value='13']"
    option_idr = "//select[@id='base-currency']/option[@value='15']"
    option_vnd = "//select[@id='base-currency']/option[@value='51']"
    option_inr = "//select[@id='base-currency']/option[@value='61']"
    option_bdt = "//select[@id='base-currency']/option[@value='74']"
    
    # Submit button
    div_form_group_button = "//form[@class='form-inline form-filter']/div[@class='form-group'][./button[@id='btnSubmit']]"
    button_submit = "//button[@id='btnSubmit']"
    
    def get_year_option(self, year):
        """Get year option by value"""
        return f"//select[@id='year']/option[@value='{year}']"
    
    def get_currency_option_by_value(self, value):
        """Get currency option by value"""
        return f"//select[@id='base-currency']/option[@value='{value}']"
    
    def get_currency_option_by_text(self, text):
        """Get currency option by text"""
        return f"//select[@id='base-currency']/option[text()='{text}']"
    
    def is_year_selected(self, year):
        """Check if year is selected"""
        return f"//select[@id='year']/option[@value='{year}' and @selected]"
    
    def is_currency_selected(self, value):
        """Check if currency is selected"""
        return f"//select[@id='base-currency']/option[@value='{value}' and @selected]" 