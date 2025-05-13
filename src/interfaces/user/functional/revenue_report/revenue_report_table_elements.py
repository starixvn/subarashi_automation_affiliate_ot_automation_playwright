class RevenueReportTableElements:
    """
    Class containing XPath locators for the Revenue Report table.
    These elements are for the main revenue report table with sortable columns.
    """

    # Report container
    div_report_container = "//div[@class='report-container']"
    div_table_commission_report = "//div[@class='table commission-report overview-table']"
    table_data = "//table[@id='dataTable']"
    
    # Table header
    thead = "//table[@id='dataTable']/thead"
    tr_header = "//table[@id='dataTable']/thead/tr"
    
    # Header columns
    th_number = "//table[@id='dataTable']/thead/tr/th[1]"
    th_month = "//table[@id='dataTable']/thead/tr/th[2]"
    th_turnover = "//table[@id='dataTable']/thead/tr/th[3]"
    th_ggr = "//table[@id='dataTable']/thead/tr/th[4]"
    th_royalty_fee = "//table[@id='dataTable']/thead/tr/th[5]"
    th_deposit_fee = "//table[@id='dataTable']/thead/tr/th[6]"
    th_withdrawal_fee = "//table[@id='dataTable']/thead/tr/th[7]"
    th_bonus = "//table[@id='dataTable']/thead/tr/th[8]"
    th_rebate = "//table[@id='dataTable']/thead/tr/th[9]"
    th_revenue_rate = "//table[@id='dataTable']/thead/tr/th[10]"
    th_revenue_share = "//table[@id='dataTable']/thead/tr/th[11]"
    th_earning_by = "//table[@id='dataTable']/thead/tr/th[12]"
    th_total_revenue_share = "//table[@id='dataTable']/thead/tr/th[13]"
    
    # Table body
    tbody = "//table[@id='dataTable']/tbody[@id='reportData']"
    
    # Month summary rows (sumrow)
    tr_sumrow = "//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')]"
    
    # Detail rows
    tr_detail = "//table[@id='dataTable']/tbody[@id='reportData']/tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    # Total row
    tr_total = "//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']"
    
    # Sort indicators
    span_default_sorting = "//span[@id='defaultSorting']"
    span_caret_asc = "//div[@class='icon-container']/span[@class='caret asc']"
    span_caret_desc = "//div[@class='icon-container']/span[@class='caret desc']"
    
    # Expand/collapse indicators
    span_chevron_bottom = "//span[@class='chevron toggleDetailRow bottom']"
    span_chevron_left = "//span[@class='chevron toggleDetailRow left']"
    
    # JavaScript resources
    script_lang_resource = "//script[contains(text(), 'langResource')]"
    script_commission_report = "//script[contains(@src, 'commission-report.js')]"
    
    def get_sort_column(self, column_name):
        """Get sort column by data-name attribute"""
        return f"//table[@id='dataTable']/thead/tr/th[@data-name='{column_name}']"
    
    def get_sort_asc_indicator(self, column_name):
        """Get ascending sort indicator for column"""
        return f"//table[@id='dataTable']/thead/tr/th[@data-name='{column_name}']//span[@class='caret asc']"
    
    def get_sort_desc_indicator(self, column_name):
        """Get descending sort indicator for column"""
        return f"//table[@id='dataTable']/thead/tr/th[@data-name='{column_name}']//span[@class='caret desc']"
    
    def get_current_sort_indicator(self):
        """Get current sort indicator"""
        return f"//table[@id='dataTable']/thead/tr//span[contains(@class, 'current')]"
    
    def get_sumrow_by_month(self, month):
        """Get summary row by month text"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]"
    
    def get_sumrow_by_index(self, index):
        """Get summary row by index (1-based)"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]"
    
    def get_detail_rows_by_month(self, month):
        """Get detail rows by month from parent sumrow"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]/following-sibling::tr[not(contains(@class, 'sumrow')) and not(contains(@class, 'total'))]"
    
    def get_detail_row_by_product(self, product):
        """Get detail row by product name"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr/td[2]/div[contains(text(), '{product}')]/ancestor::tr"
    
    def get_sumrow_month(self, index):
        """Get month text from summary row by index"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[2]/div/text()"
    
    def get_sumrow_turnover(self, index):
        """Get turnover value from summary row by index"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[3]"
    
    def get_sumrow_ggr(self, index):
        """Get GGR value from summary row by index"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[4]"
    
    def get_sumrow_revenue_share(self, index):
        """Get revenue share value from summary row by index"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[11]"
    
    def get_sumrow_total_revenue_share(self, index):
        """Get total revenue share value from summary row by index"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[13]"
    
    def get_total_turnover(self):
        """Get total turnover value"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']/td[3]"
    
    def get_total_ggr(self):
        """Get total GGR value"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']/td[4]"
    
    def get_total_revenue_share(self):
        """Get total revenue share value"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']/td[11]"
    
    def get_total_total_revenue_share(self):
        """Get total of total revenue share value"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[@class='total']/td[13]"
    
    def get_expand_button(self, month):
        """Get expand/collapse button for month"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]]//span[@class='chevron toggleDetailRow']"
    
    def is_expanded(self, month):
        """Check if month is expanded"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][.//div[contains(text(), '{month}')]][following-sibling::tr[1][contains(@class, 'expanded')]]"
    
    def is_revenue_rate_highest(self, index):
        """Check if revenue rate has 'highest share' tooltip"""
        return f"//table[@id='dataTable']/tbody[@id='reportData']/tr[contains(@class, 'sumrow')][{index}]/td[10][contains(@class, 'text-danger')]" 