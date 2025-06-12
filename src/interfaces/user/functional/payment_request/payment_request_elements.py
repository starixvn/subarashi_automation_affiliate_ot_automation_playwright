class PaymentRequestElements:
    
    # Main container elements
    div_main_content = "//div[@class='main-content']"
    div_container_fluid = "//div[@class='main-content']/div[@class='container-fluid']"
    div_main_panel = "//div[@id='mainPanel']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_page_title_text = "//div[@class='page-title']/span[@class='text']"
    
    # Payment request container
    div_payment_request = "//div[@id='paymentRequest']"
    
    # Request payout section
    div_request_payout = "//div[@id='requestPayout']"
    
    # Payment info group
    div_info_group = "//div[@id='requestPayout']//div[@class='info-group']"
    div_title = "//div[@id='requestPayout']//div[@class='title']"
    span_title_text = "//div[@id='requestPayout']//div[@class='title']/span[@class='text']"
    
    # Payment info container
    div_payment_info = "//div[@id='requestPayout']//div[@class='payment-info']"
    div_result_message = "//div[@id='resultMessage']"
    p_alert_message = "//div[@id='resultMessage']/p[@class='alert alert-danger']"
    
    # Payment request form
    form_request_payout = "//form[@id='requestPayoutForm']"
    input_verification_token = "//form[@id='requestPayoutForm']/input[@name='__RequestVerificationToken']"
    
    # Balance Brought Forward
    div_form_group_balance = "//form[@id='requestPayoutForm']/div[contains(@class, 'form-group')][./label[contains(text(), 'Balance Brought Forward')]]"
    label_balance = "//form[@id='requestPayoutForm']//label[contains(text(), 'Balance Brought Forward')]"
    p_balance_value = "//form[@id='requestPayoutForm']//label[contains(text(), 'Balance Brought Forward')]/../../div/p"
    
    # Minimum Withdrawal Amount
    div_form_group_min_amount = "//form[@id='requestPayoutForm']/div[contains(@class, 'form-group')][./label[contains(text(), 'Minimum Withdrawal Amount')]]"
    label_min_amount = "//form[@id='requestPayoutForm']//label[contains(text(), 'Minimum Withdrawal Amount')]"
    p_min_amount_value = "//form[@id='requestPayoutForm']//label[contains(text(), 'Minimum Withdrawal Amount')]/../../div/p"
    
    # Input Request Amount
    div_form_group_amount = "//form[@id='requestPayoutForm']/div[contains(@class, 'form-group')][./label[contains(text(), 'Input Request Amount')]]"
    label_amount = "//form[@id='requestPayoutForm']//label[@for='Amount']"
    input_amount = "//form[@id='requestPayoutForm']//input[@id='Amount']"
    
    # Request button
    div_form_group_button = "//form[@id='requestPayoutForm']/div[contains(@class, 'form-group')][.//button]"
    button_request_payout = "//form[@id='requestPayoutForm']//button[contains(text(), 'Request Payout')]"
    
    # Hidden inputs
    input_hidden_balance = "//form[@id='requestPayoutForm']//input[@id='BalBroughtForward']"
    input_hidden_min_amount = "//form[@id='requestPayoutForm']//input[@id='MinAmount']"