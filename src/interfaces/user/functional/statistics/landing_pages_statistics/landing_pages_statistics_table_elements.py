class LandingPagesStatisticsTableElements:
    """
    Class containing XPath locators for the landing pages statistics main table section.
    These elements are for the main table displaying statistics for different pages and languages.
    """
    
    # Table container
    div_report_container = "//div[@class='report-container']"
    div_statistics_table = "//div[@id='statisticsTable']"
    
    # Table element
    table = "//div[@id='statisticsTable']/table"
    
    # Table header
    thead = "//div[@id='statisticsTable']/table/thead"
    tr_header = "//div[@id='statisticsTable']/table/thead/tr"
    
    # Header columns
    th_page = "//div[@id='statisticsTable']/table/thead/tr/th[1]"
    th_language = "//div[@id='statisticsTable']/table/thead/tr/th[2]"
    th_total_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[3]"
    th_unique_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[4]"
    th_signup = "//div[@id='statisticsTable']/table/thead/tr/th[5]"
    th_fdm = "//div[@id='statisticsTable']/table/thead/tr/th[6]"
    
    # Table body
    tbody = "//div[@id='statisticsTable']/table/tbody"
    tr_rows = "//div[@id='statisticsTable']/table/tbody/tr"
    
    # Row columns
    td_page = "//div[@id='statisticsTable']/table/tbody/tr/td[1]"
    td_language = "//div[@id='statisticsTable']/table/tbody/tr/td[2]"
    td_total_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[3]"
    td_unique_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[4]"
    td_signup = "//div[@id='statisticsTable']/table/tbody/tr/td[5]"
    td_fdm = "//div[@id='statisticsTable']/table/tbody/tr/td[6]"
    
    # Page link
    a_statistics_item = "//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@class='statisticsItem']"
    
    def get_row_by_index(self, index):
        """Get row by its index (1-based)"""
        return f"//div[@id='statisticsTable']/table/tbody/tr[{index}]"
    
    def get_page_link_by_index(self, index):
        """Get page link by row index (1-based)"""
        return f"//div[@id='statisticsTable']/table/tbody/tr[{index}]/td[1]/a"
    
    def get_page_link_by_page(self, page):
        """Get page link by page name"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[contains(text(), '{page}')]"
    
    def get_page_link_by_data_attributes(self, page, language):
        """Get page link by data-page and data-language attributes"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']"
    
    def get_row_by_page_and_language(self, page, language):
        """Get row by page name and language text"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']/ancestor::tr"
    
    def get_total_clicks_by_page_and_language(self, page, language):
        """Get total clicks cell for a specific page and language"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']/ancestor::tr/td[3]"
    
    def get_unique_clicks_by_page_and_language(self, page, language):
        """Get unique clicks cell for a specific page and language"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']/ancestor::tr/td[4]"
    
    def get_signup_by_page_and_language(self, page, language):
        """Get signup cell for a specific page and language"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']/ancestor::tr/td[5]"
    
    def get_fdm_by_page_and_language(self, page, language):
        """Get FDM cell for a specific page and language"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-page='{page}' and @data-language='{language}']/ancestor::tr/td[6]" 