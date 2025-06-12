class AdjustmentElements:
    
    # Form container
    frm_adjustment = "//form[@class='adjustment-form']"
    
    # Username title element
    txt_username_title = "//h5[@class='font-weight-bold']"
    
    # Balance section
    lbl_balance = "//label[text()='Balance Brought Forward']"
    lbl_balance_value = "//label[text()='Balance Brought Forward']/following-sibling::label"
    
    # Amount section
    lbl_amount = "//label[@for='amount']"
    inp_amount = "//input[@id='amount']"
    
    # Description section
    lbl_description = "//label[@for='description']"
    txt_description = "//textarea[@id='description']"
    
    # Submit button
    btn_submit = "//button[@type='button' and contains(@class, 'btn-success')]"
