class LoginDialogElements:
    
    # Dialog container
    div_login_dialog = "//div[@class='modal fade login-dialog'][@id='loginDialog']"
    div_modal_dialog = "//div[@class='modal fade login-dialog'][@id='loginDialog']/div[@class='modal-dialog']"
    div_modal_content = "//div[@class='modal fade login-dialog'][@id='loginDialog']/div[@class='modal-dialog']/div[@class='modal-content']"
    div_modal_main_content = "//div[@class='modal fade login-dialog'][@id='loginDialog']/div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-main-content']"
    
    # Modal body
    div_modal_body = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='modal-body']"
    btn_close = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='modal-body']/button[@class='close']"
    img_close_pc = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='modal-body']/button[@class='close']/img[@class='show-pc']"
    img_close_mobile = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='modal-body']/button[@class='close']/img[@class='show-mobile']"
    
    # Main login container
    div_main_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']"
    
    # Left panel (join section)
    div_left_item = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]"
    div_login_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/div[@class='login-login']"
    img_logo = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/div[@class='login-login']/img"
    h2_logo_text = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/h2[@class='logo-text']"
    div_group_text = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/div[@class='group-text']"
    h3_title_affmember = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/div[@class='group-text']/h3[@class='title-affmember']"
    p_signup_text = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/div[@class='group-text']/p[@id='signUpToAffiliateProgram']"
    a_join_now = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][1]/a[@class='btn-join btn-submit btn-block text-uppercase']"
    
    # Right panel (login form)
    div_right_item = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]"
    div_heading_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]/div[@class='heading-login spacing-bt']"
    form_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]/form[@class='form-login']"
    h3_title = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]/form[@class='form-login']/h3[@class='title spacing-bt']"
    
    # Form inputs container
    div_spacing_bt = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']"
    
    # Username input
    div_username_input = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input'][1]"
    input_username = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input'][1]/input[@id='dialogtxtUsername']"
    
    # Password input
    div_password_input = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input'][2]"
    input_password = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input'][2]/input[@id='dialogtxtPassword']"
    
    # Captcha input
    div_captcha_input = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input columns-2']"
    input_validation = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input columns-2']/input[@id='dialogtxtValidation']"
    div_validation_value = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input columns-2']/div[@class='validation-value'][@id='loginDialogcaptchaBtn']"
    img_captcha = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/div[@class='spacing-bt']/div[@class='custom-input columns-2']/div[@class='validation-value']/img[@id='loginDialogcaptchaImg']"
    
    # Login button
    btn_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/button[@id='btnDialogLogin']"
    
    # Forgot password link
    a_forgot_login = "//div[@class='modal fade login-dialog'][@id='loginDialog']//form[@class='form-login']/a[@class='link-login-popup']"
    
    # Legacy site link
    p_redirect_old_link = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]/p[@class='redirect-old-link']"
    a_old_site = "//div[@class='modal fade login-dialog'][@id='loginDialog']//div[@class='main-login']/div[@class='item'][2]/p[@class='redirect-old-link']/a" 