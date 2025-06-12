class PaymentHistoryElements:
    
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