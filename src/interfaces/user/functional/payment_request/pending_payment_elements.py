class PendingPaymentElements:
    """
    Class containing XPath locators for the Pending Payment section.
    These elements are for the pending payment request information and cancel button.
    """

    # Pending payment section
    div_pending_payment = "//div[@id='pendingPayment']"
    
    # Pending payment info group
    div_info_group = "//div[@id='pendingPayment']//div[@class='info-group']"
    div_title = "//div[@id='pendingPayment']//div[@class='title']"
    span_title_text = "//div[@id='pendingPayment']//div[@class='title']/span[@class='text']"
    
    # Pending payment form
    form_cancel_payment = "//form[@id='cancelPaymentForm']"
    input_verification_token = "//form[@id='cancelPaymentForm']/input[@name='__RequestVerificationToken']"
    
    # Pending payment table
    div_payment_history = "//form[@id='cancelPaymentForm']/div[@class='table payment-history table-responsive']"
    table = "//form[@id='cancelPaymentForm']//table"
    
    # Table header
    thead = "//form[@id='cancelPaymentForm']//table/thead"
    tr_header = "//form[@id='cancelPaymentForm']//table/thead/tr"
    th_request_date = "//form[@id='cancelPaymentForm']//table/thead/tr/th[1]"
    th_request_amount = "//form[@id='cancelPaymentForm']//table/thead/tr/th[2]"
    th_status = "//form[@id='cancelPaymentForm']//table/thead/tr/th[3]"
    th_action = "//form[@id='cancelPaymentForm']//table/thead/tr/th[4]"
    
    # Table body
    tbody = "//form[@id='cancelPaymentForm']//table/tbody"
    tr_row = "//form[@id='cancelPaymentForm']//table/tbody/tr"
    
    # Table data cells
    td_request_date = "//form[@id='cancelPaymentForm']//table/tbody/tr/td[1]"
    td_request_amount = "//form[@id='cancelPaymentForm']//table/tbody/tr/td[2]"
    td_status = "//form[@id='cancelPaymentForm']//table/tbody/tr/td[3]"
    td_action = "//form[@id='cancelPaymentForm']//table/tbody/tr/td[4]"
    
    # Cancel button
    button_cancel_payment = "//button[@id='cancelPaymentRequest']"
    
    # Hidden inputs
    input_hidden_trans_id = "//form[@id='cancelPaymentForm']//input[@id='TransId']"
    input_hidden_amount = "//form[@id='cancelPaymentForm']//input[@id='Amount']"
    input_hidden_request_date = "//form[@id='cancelPaymentForm']//input[@id='RequestDate']"
    
    def get_pending_request_date(self):
        """Get pending request date"""
        return self.td_request_date
    
    def get_pending_request_amount(self):
        """Get pending request amount"""
        return self.td_request_amount
    
    def get_pending_status(self):
        """Get pending status"""
        return self.td_status
    
    def has_pending_request(self):
        """Check if there is a pending request"""
        return f"//form[@id='cancelPaymentForm']//table/tbody/tr"
    
    def is_request_processing(self):
        """Check if request is in processing status"""
        return f"//form[@id='cancelPaymentForm']//table/tbody/tr/td[3][text()='Processing']" 