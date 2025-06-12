class PasswordModalElements:
    
    # Modal container
    mdl_password = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title' and contains(text(), 'Change Password')]"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Password form container
    div_password_container = "//div[@class='change-password-form-container']"
    frm_password = "//form[contains(@class, 'mb-5')]"
    
    # Password field
    div_password = "//div[@class='mb-2 row form-group'][1]"
    lbl_password = "//label[@for='Password']"
    inp_password = "//input[@name='password' and @id='Password']"
    div_password_feedback = "//input[@name='password']/following-sibling::div[@class='invalid-feedback']"
    txt_password_required = "//input[@name='password']/following-sibling::div[@class='invalid-feedback']/div"
    
    # Confirm Password field
    div_confirm_password = "//div[@class='mb-2 row form-group'][2]"
    lbl_confirm_password = "//label[@for='ConfirmPassword']"
    inp_confirm_password = "//input[@name='confirmPassword' and @id='ConfirmPassword']"
    div_confirm_feedback = "//input[@name='confirmPassword']/following-sibling::div[@class='invalid-feedback']"
    txt_confirm_required = "//input[@name='confirmPassword']/following-sibling::div[@class='invalid-feedback']/div"
    
    # Action buttons
    btn_submit = "//button[contains(@class, 'btn-success') and contains(text(), 'Submit')]"
    btn_cancel = "//button[contains(@class, 'btn-info') and contains(text(), 'Cancel')]" 