class PaymentHistoryElements:
    """
    Class containing XPath locators for the Payment History section.
    These elements are for the recent payment history table and year filter.
    """

    # Payment list section
    div_payment_list = "//div[@id='paymentList']"
    
    # Payment info group
    div_info_group = "//div[@id='paymentList']/div[@class='info-group']"
    div_title = "//div[@id='paymentList']/div[@class='info-group']/div[@class='title']"
    span_title_text = "//div[@id='paymentList']/div[@class='info-group']/div[@class='title']/span[@class='text']"
    
    # Year filter form
    form_payment_list = "//form[@id='paymentListForm']"
    div_form_group = "//form[@id='paymentListForm']/div[@class='form-group']"
    label_year = "//form[@id='paymentListForm']//label[text()='Year']"
    select_year = "//select[@id='year']"
    option_2025 = "//select[@id='year']/option[@value='2025']"
    option_2024 = "//select[@id='year']/option[@value='2024']"
    option_2023 = "//select[@id='year']/option[@value='2023']"
    button_submit = "//button[@id='btnSubmit']"
    
    # Payment history table
    div_payment_history = "//div[@id='payment-history']"
    table = "//div[@id='payment-history']/table"
    
    # Table header
    thead = "//div[@id='payment-history']/table/thead"
    tr_header = "//div[@id='payment-history']/table/thead/tr"
    th_ref_no = "//div[@id='payment-history']/table/thead/tr/th[1]"
    th_request_date = "//div[@id='payment-history']/table/thead/tr/th[2]"
    th_request_amount = "//div[@id='payment-history']/table/thead/tr/th[3]"
    th_payment_method = "//div[@id='payment-history']/table/thead/tr/th[4]"
    th_completed_date = "//div[@id='payment-history']/table/thead/tr/th[5]"
    th_status = "//div[@id='payment-history']/table/thead/tr/th[6]"
    th_description = "//div[@id='payment-history']/table/thead/tr/th[7]"
    
    # Table body
    tbody = "//div[@id='payment-history']/table/tbody"
    tr_row = "//div[@id='payment-history']/table/tbody/tr"
    
    # JavaScript resources
    script_resource_lang = "//script[contains(text(), 'resourceLang')]"
    script_payment_request = "//script[contains(@src, 'payment-request.js')]"
    
    def get_year_option(self, year):
        """Get year option by value"""
        return f"//select[@id='year']/option[@value='{year}']"
    
    def get_row_by_index(self, index):
        """Get table row by index (1-based)"""
        return f"//div[@id='payment-history']/table/tbody/tr[{index}]"
    
    def get_row_by_ref_no(self, ref_no):
        """Get table row by reference number"""
        return f"//div[@id='payment-history']/table/tbody/tr[./td[1][text()='{ref_no}']]"
    
    def get_cell(self, row_index, col_index):
        """Get table cell by row and column index (both 1-based)"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[{col_index}]"
    
    def get_ref_no(self, row_index):
        """Get reference number from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[1]"
    
    def get_request_date(self, row_index):
        """Get request date from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[2]"
    
    def get_request_amount(self, row_index):
        """Get request amount from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[3]"
    
    def get_payment_method(self, row_index):
        """Get payment method from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[4]"
    
    def get_completed_date(self, row_index):
        """Get completed date from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[5]"
    
    def get_status(self, row_index):
        """Get status from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[6]"
    
    def get_description(self, row_index):
        """Get description from row by index"""
        return f"//div[@id='payment-history']/table/tbody/tr[{row_index}]/td[7]"
    
    def get_rows_by_status(self, status):
        """Get all rows with specific status"""
        return f"//div[@id='payment-history']/table/tbody/tr[./td[6][contains(text(), '{status}')]]" 