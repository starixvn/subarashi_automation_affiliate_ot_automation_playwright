class MarketingStatisticsTableElements:
    """
    Class containing XPath locators for the Marketing Statistics table section.
    These elements are for the table displaying channel statistics including clicks, unique clicks, signups, and FDM.
    """
    
    # Table container elements
    div_report_container = "//div[@class='report-container']"
    div_statistics_table = "//div[@id='statisticsTable']"
    table_statistics = "//table[@class='row-toogleable-table']"
    
    # Table header
    thead = "//table[@class='row-toogleable-table']/thead"
    tr_header = "//table[@class='row-toogleable-table']/thead/tr"
    
    # Header columns
    th_index = "//table[@class='row-toogleable-table']/thead/tr/th[1]"
    th_channel = "//table[@class='row-toogleable-table']/thead/tr/th[2]"
    th_language = "//table[@class='row-toogleable-table']/thead/tr/th[3]"
    th_total_clicks = "//table[@class='row-toogleable-table']/thead/tr/th[4]"
    th_unique_clicks = "//table[@class='row-toogleable-table']/thead/tr/th[5]"
    th_signup = "//table[@class='row-toogleable-table']/thead/tr/th[6]"
    th_fdm = "//table[@class='row-toogleable-table']/thead/tr/th[7]"
    
    # Table body
    tbody = "//table[@class='row-toogleable-table']/tbody"
    
    # Parent rows (channel summary rows)
    tr_parent_rows = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']"
    
    # Child rows (detail rows)
    tr_child_rows = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]"
    
    # Parent row columns
    td_parent_index = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[1]"
    td_parent_channel = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[2]"
    span_channel_name = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[2]//span[@class='flex-0']"
    button_toggle = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[2]//button[@class='btn btn-transparent']"
    span_chevron = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[2]//span[@class='chevron bottom']"
    
    td_parent_language = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[3]"
    td_parent_total_clicks = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[4]"
    td_parent_unique_clicks = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[5]"
    td_parent_signup = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[6]"
    td_parent_fdm = "//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[7]"
    
    # Child row columns
    td_child_empty = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[1]"
    td_child_url = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[2]"
    td_child_language = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[3]"
    td_child_total_clicks = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[4]"
    td_child_unique_clicks = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[5]"
    td_child_signup = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[6]"
    td_child_fdm = "//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item')]/td[7]"
    
    # JavaScript resource
    script_statistics = "//script[contains(@src, 'marketing-statistics.js')]"
    
    def get_parent_row_by_index(self, index):
        """Get parent row by index (1-based as shown in the UI)"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']/td[1][text()='{index}']/parent::tr"
    
    def get_parent_row_by_channel(self, channel_name):
        """Get parent row by channel name"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/ancestor::tr"
    
    def get_parent_row_by_data_id(self, data_id):
        """Get parent row by data-id attribute"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@data-id='{data_id}']"
    
    def get_child_rows_by_parent(self, data_parent):
        """Get all child rows for a parent"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@data-parent='{data_parent}']"
    
    def get_toggle_button_for_channel(self, channel_name):
        """Get toggle button for a specific channel"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/following-sibling::div//button"
    
    def get_cell_value(self, row_index, column_index):
        """Get the value of a cell by row and column index"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[{row_index}]/td[{column_index}]"
    
    def get_total_clicks_for_channel(self, channel_name):
        """Get total clicks for a specific channel"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/ancestor::tr/td[4]"
    
    def get_unique_clicks_for_channel(self, channel_name):
        """Get unique clicks for a specific channel"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/ancestor::tr/td[5]"
    
    def get_signup_for_channel(self, channel_name):
        """Get signup count for a specific channel"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/ancestor::tr/td[6]"
    
    def get_fdm_for_channel(self, channel_name):
        """Get FDM count for a specific channel"""
        return f"//table[@class='row-toogleable-table']/tbody/tr[@class='parent-item']//span[@class='flex-0'][text()='{channel_name}']/ancestor::tr/td[7]" 