class DailyEarningElements:
    """
    Class containing XPath locators for the Daily Earning elements.
    These elements are for the daily earning section with product types and earnings data.
    """

    # Container elements
    div_daily_earning = "//div[.//ol[@id='dailyEarningBreadcrumb']]"
    div_breadcrumb_container = "//div[@class='breadcrumb-container']"
    ol_breadcrumb = "//ol[@id='dailyEarningBreadcrumb']"
    li_statement_history = "//ol[@id='dailyEarningBreadcrumb']/li"
    a_statement_history = "//ol[@id='dailyEarningBreadcrumb']/li/a"
    
    # Filter form elements
    div_form_filter = "//div[.//select[@id='ProductId']]/div[@class='form-inline form-filter']"
    
    # Product type filter
    div_form_group_product = "//div[.//select[@id='ProductId']]//div[@class='form-group']"
    label_product_id = "//label[@for='ProductId']"
    select_product_id = "//select[@id='ProductId']"
    option_all = "//select[@id='ProductId']/option[@value='0']"
    
    # Base currency filter (second occurrence)
    div_form_group_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//div[@class='form-group']"
    label_base_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//label[@for='base-currency']"
    select_base_currency = "//div[.//select[@id='base-currency'] and .//label[@class='w120']]//select[@id='base-currency']"
    
    # Daily earning table
    div_daily_earning_content = "//div[@id='dailyEarningContent']"
    div_table_responsive = "//div[@id='dailyEarningContent'][@class='table table-responsive']"
    table = "//div[@id='dailyEarningContent']//table"
    
    # Table header elements
    thead = "//div[@id='dailyEarningContent']//table/thead"
    tr_header = "//div[@id='dailyEarningContent']//table/thead/tr"
    th_number = "//div[@id='dailyEarningContent']//table/thead/tr/th[1]"
    th_date = "//div[@id='dailyEarningContent']//table/thead/tr/th[2]"
    th_deposited = "//div[@id='dailyEarningContent']//table/thead/tr/th[3]"
    th_turnover = "//div[@id='dailyEarningContent']//table/thead/tr/th[4]"
    th_ggr = "//div[@id='dailyEarningContent']//table/thead/tr/th[5]"
    th_bonus = "//div[@id='dailyEarningContent']//table/thead/tr/th[6]"
    th_rebate = "//div[@id='dailyEarningContent']//table/thead/tr/th[7]"
    
    # Table body elements
    tbody = "//div[@id='dailyEarningContent']//table/tbody"
    tr_row = "//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))]"
    tr_total = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']"
    
    # Total row cells
    td_total_label = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[1]"
    td_total_deposited = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[3]"
    td_total_turnover = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[4]"
    td_total_ggr = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[5]"
    td_total_bonus = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[6]"
    td_total_rebate = "//div[@id='dailyEarningContent']//table/tbody/tr[@class='total']/td[7]"
    
    def get_row_by_index(self, index):
        """Get row by index (1-based)"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{index}]"
    
    def get_row_by_date(self, date):
        """Get row by date text (format: MM/DD/YYYY)"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][.//td[2][contains(text(), '{date}')]]"
    
    def get_cell(self, row_index, column_index):
        """Get cell by row index and column index (both 1-based)"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[{column_index}]"
    
    def get_row_number(self, row_index):
        """Get row number (1st column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[1]"
    
    def get_row_date(self, row_index):
        """Get row date (2nd column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[2]"
    
    def get_row_deposited(self, row_index):
        """Get row deposited amount (3rd column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[3]"
    
    def get_row_turnover(self, row_index):
        """Get row turnover amount (4th column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[4]"
    
    def get_row_ggr(self, row_index):
        """Get row GGR amount (5th column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[5]"
    
    def get_row_bonus(self, row_index):
        """Get row bonus amount (6th column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[6]"
    
    def get_row_rebate(self, row_index):
        """Get row rebate amount (7th column) by row index"""
        return f"//div[@id='dailyEarningContent']//table/tbody/tr[not(contains(@class, 'total'))][{row_index}]/td[7]"
    
    def get_product_option(self, value):
        """Get product type option by value"""
        return f"//select[@id='ProductId']/option[@value='{value}']"
    
    def get_product_option_by_text(self, text):
        """Get product type option by text"""
        return f"//select[@id='ProductId']/option[contains(text(), '{text}')]"
    
    def get_currency_option(self, value):
        """Get currency option by value (second occurrence)"""
        return f"//div[.//select[@id='base-currency'] and .//label[@class='w120']]//select[@id='base-currency']/option[@value='{value}']"
    
    def get_currency_option_by_text(self, text):
        """Get currency option by text (second occurrence)"""
        return f"//div[.//select[@id='base-currency'] and .//label[@class='w120']]//select[@id='base-currency']/option[text()='{text}']" 