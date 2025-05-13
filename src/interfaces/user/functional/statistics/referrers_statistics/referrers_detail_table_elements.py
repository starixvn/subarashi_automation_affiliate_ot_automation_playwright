class ReferrersDetailTableElements:
    """
    Class containing XPath locators for the referrers statistics detail table section.
    These elements are for the detail table showing specific website URLs and their statistics,
    along with pagination controls.
    """
    
    # Pagination container
    div_statistics_detail_pager = "//div[@id='statisticsDetailPager']"
    div_pager_container = "//div[@id='statisticsDetailPager']/div[@class='pager-container']"
    
    # Pagination controls
    a_page_first = "//div[@id='statisticsDetailPager']//a[@class='icon glyphicon glyphicon-fast-backward page-first']"
    a_page_prev = "//div[@id='statisticsDetailPager']//a[@class='icon glyphicon glyphicon-triangle-left page-prev']"
    div_page_input = "//div[@id='statisticsDetailPager']//div[@class='page-input']"
    span_page_info = "//div[@id='statisticsDetailPager']//span[@class='text-pageInfo']"
    a_page_next = "//div[@id='statisticsDetailPager']//a[@class='icon glyphicon glyphicon-triangle-right page-next']"
    a_page_last = "//div[@id='statisticsDetailPager']//a[@class='icon glyphicon glyphicon-fast-forward page-last']"
    
    # Page size selector
    select_pagesize = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']"
    option_pagesize_10 = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='10']"
    option_pagesize_20 = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='20']"
    option_pagesize_50 = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='50']"
    option_pagesize_100 = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='100']"
    option_pagesize_200 = "//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='200']"
    
    # Detail table container
    div_statistics_detail_table = "//div[@id='statisticsDetailTable']"
    table_detail = "//div[@id='statisticsDetailTable']/table"
    
    # Table header
    thead_detail = "//div[@id='statisticsDetailTable']/table/thead"
    tr_header_detail = "//div[@id='statisticsDetailTable']/table/thead/tr"
    
    # Header columns
    th_detail_website_url = "//div[@id='statisticsDetailTable']/table/thead/tr/th[1]"
    th_detail_total_clicks = "//div[@id='statisticsDetailTable']/table/thead/tr/th[2]"
    th_detail_unique_clicks = "//div[@id='statisticsDetailTable']/table/thead/tr/th[3]"
    th_detail_signup = "//div[@id='statisticsDetailTable']/table/thead/tr/th[4]"
    th_detail_fdm = "//div[@id='statisticsDetailTable']/table/thead/tr/th[5]"
    
    # Table body
    tbody_detail = "//div[@id='statisticsDetailTable']/table/tbody"
    tr_detail_rows = "//div[@id='statisticsDetailTable']/table/tbody/tr"
    
    # Row columns
    td_detail_website_url = "//div[@id='statisticsDetailTable']/table/tbody/tr/td[1]"
    td_detail_total_clicks = "//div[@id='statisticsDetailTable']/table/tbody/tr/td[2]"
    td_detail_unique_clicks = "//div[@id='statisticsDetailTable']/table/tbody/tr/td[3]"
    td_detail_signup = "//div[@id='statisticsDetailTable']/table/tbody/tr/td[4]"
    td_detail_fdm = "//div[@id='statisticsDetailTable']/table/tbody/tr/td[5]"
    
    # Hidden input
    input_total_item = "//input[@id='TotalItem']"
    
    # JavaScript resource
    script_referrer_statistics = "//script[contains(@src, 'referrerstatistics')]"
    
    def get_detail_row_by_index(self, index):
        """Get detail row by its index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]"
    
    def get_detail_website_url_by_index(self, index):
        """Get website URL cell by row index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]/td[1]"
    
    def get_detail_total_clicks_by_index(self, index):
        """Get total clicks cell by row index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]/td[2]"
    
    def get_detail_unique_clicks_by_index(self, index):
        """Get unique clicks cell by row index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]/td[3]"
    
    def get_detail_signup_by_index(self, index):
        """Get signup cell by row index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]/td[4]"
    
    def get_detail_fdm_by_index(self, index):
        """Get FDM cell by row index (1-based)"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr[{index}]/td[5]"
    
    def get_pagesize_option(self, value):
        """Get page size option by value"""
        return f"//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='{value}']"
    
    def is_pagesize_selected(self, value):
        """Check if page size option is selected"""
        return f"//div[@id='statisticsDetailPager']//select[@class='pagesize-select']/option[@value='{value}' and @selected]"
    
    def is_page_control_disabled(self, control_class):
        """Check if a pagination control is disabled"""
        return f"//div[@id='statisticsDetailPager']//a[contains(@class, '{control_class}')][contains(@class, 'disable')]"
    
    def get_row_containing_url(self, url_part):
        """Get row containing part of a URL"""
        return f"//div[@id='statisticsDetailTable']/table/tbody/tr/td[1][contains(text(), '{url_part}')]/ancestor::tr" 