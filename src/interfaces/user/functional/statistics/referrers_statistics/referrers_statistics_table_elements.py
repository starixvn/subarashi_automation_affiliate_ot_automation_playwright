class ReferrersStatisticsTableElements:
    """
    Class containing XPath locators for the referrers statistics main table section.
    These elements are for the main table displaying statistics for different referring websites.
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
    th_website_url = "//div[@id='statisticsTable']/table/thead/tr/th[1]"
    th_total_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[2]"
    th_unique_clicks = "//div[@id='statisticsTable']/table/thead/tr/th[3]"
    th_signup = "//div[@id='statisticsTable']/table/thead/tr/th[4]"
    th_fdm = "//div[@id='statisticsTable']/table/thead/tr/th[5]"
    
    # Table body
    tbody = "//div[@id='statisticsTable']/table/tbody"
    tr_rows = "//div[@id='statisticsTable']/table/tbody/tr"
    
    # Row columns
    td_website_url = "//div[@id='statisticsTable']/table/tbody/tr/td[1]"
    td_total_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[2]"
    td_unique_clicks = "//div[@id='statisticsTable']/table/tbody/tr/td[3]"
    td_signup = "//div[@id='statisticsTable']/table/tbody/tr/td[4]"
    td_fdm = "//div[@id='statisticsTable']/table/tbody/tr/td[5]"
    
    # Website URL link
    a_statistics_item = "//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@class='statisticsItem']"
    
    def get_row_by_index(self, index):
        """Get row by its index (1-based)"""
        return f"//div[@id='statisticsTable']/table/tbody/tr[{index}]"
    
    def get_website_url_by_index(self, index):
        """Get website URL cell by row index (1-based)"""
        return f"//div[@id='statisticsTable']/table/tbody/tr[{index}]/td[1]"
    
    def get_website_link_by_index(self, index):
        """Get website link by row index (1-based)"""
        return f"//div[@id='statisticsTable']/table/tbody/tr[{index}]/td[1]/a"
    
    def get_website_link_by_domain(self, domain):
        """Get website link by domain name"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']"
    
    def get_row_by_domain(self, domain):
        """Get row by domain name"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']/ancestor::tr"
    
    def get_total_clicks_by_domain(self, domain):
        """Get total clicks cell for a specific domain"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']/ancestor::tr/td[2]"
    
    def get_unique_clicks_by_domain(self, domain):
        """Get unique clicks cell for a specific domain"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']/ancestor::tr/td[3]"
    
    def get_signup_by_domain(self, domain):
        """Get signup cell for a specific domain"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']/ancestor::tr/td[4]"
    
    def get_fdm_by_domain(self, domain):
        """Get FDM cell for a specific domain"""
        return f"//div[@id='statisticsTable']/table/tbody/tr/td[1]/a[@data-domain='{domain}']/ancestor::tr/td[5]"
    
    def get_row_with_none_value(self):
        """Get row with 'none' as the URL"""
        return "//div[@id='statisticsTable']/table/tbody/tr/td[1][normalize-space(text())='none']/ancestor::tr"
    
    def get_total_clicks_for_none(self):
        """Get total clicks for the 'none' row"""
        return "//div[@id='statisticsTable']/table/tbody/tr/td[1][normalize-space(text())='none']/ancestor::tr/td[2]"
    
    def get_unique_clicks_for_none(self):
        """Get unique clicks for the 'none' row"""
        return "//div[@id='statisticsTable']/table/tbody/tr/td[1][normalize-space(text())='none']/ancestor::tr/td[3]"
    
    def get_signup_for_none(self):
        """Get signup for the 'none' row"""
        return "//div[@id='statisticsTable']/table/tbody/tr/td[1][normalize-space(text())='none']/ancestor::tr/td[4]"
    
    def get_fdm_for_none(self):
        """Get FDM for the 'none' row"""
        return "//div[@id='statisticsTable']/table/tbody/tr/td[1][normalize-space(text())='none']/ancestor::tr/td[5]" 