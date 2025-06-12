class ContactFormElements:
    
    # Form container
    form_contact = "//form[@id='contactForm'][@class='form']"
    
    # Hidden token field
    input_token = "//form[@id='contactForm']/input[@name='__RequestVerificationToken']"
    
    # Alert message
    div_alert_danger = "//form[@id='contactForm']/div[@class='alert alert-danger'][@id='messageError']"
    
    # Name field
    div_name_group = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][1]"
    div_name_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][1]/div[@class='items validate-group'][1]"
    input_name = "//form[@id='contactForm']//input[@id='Sender']"
    div_name_validation = "//form[@id='contactForm']//input[@id='Sender']/following-sibling::div[@class='validate-input hide']"
    
    # Affiliate field
    div_affiliate_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][1]/div[@class='items'][2]"
    input_affiliate = "//form[@id='contactForm']//input[@id='Affiliate']"
    
    # Subject field
    div_subject_group = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][2]"
    div_subject_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][2]/div[@class='items validate-group'][1]"
    input_subject = "//form[@id='contactForm']//input[@id='Subject']"
    div_subject_validation = "//form[@id='contactForm']//input[@id='Subject']/following-sibling::div[@class='validate-input hide']"
    
    # Email field
    div_email_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-2'][2]/div[@class='items validate-group'][2]"
    input_email = "//form[@id='contactForm']//input[@id='Email']"
    div_email_validation = "//form[@id='contactForm']//input[@id='Email']/following-sibling::div[@class='validate-input hide']"
    
    # Comment field
    div_comment_group = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-1']"
    div_comment_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-1']/div[@class='items validate-group']"
    textarea_comment = "//form[@id='contactForm']//textarea[@id='Content']"
    div_comment_validation = "//form[@id='contactForm']//textarea[@id='Content']/following-sibling::div[@class='validate-input hide']"
    
    # Captcha field
    div_captcha_group = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-button']"
    div_captcha_items = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-button']/div[@class='items validate-group']"
    input_captcha = "//form[@id='contactForm']//input[@id='Captcha']"
    div_captcha_validation = "//form[@id='contactForm']//input[@id='Captcha']/following-sibling::div[@class='validate-input hide']"
    
    # Captcha image
    div_validation_value = "//form[@id='contactForm']/div[@class='form-group form-columns form-columns-button']/div[@class='validation-value'][@id='contactUsCaptchaBtn']"
    img_captcha = "//form[@id='contactForm']//img[@id='contactUsCaptchaImg']"
    
    # Form buttons
    div_group_button = "//form[@id='contactForm']/div[@class='form-group group-button']"
    button_submit = "//form[@id='contactForm']//button[@type='submit'][@class='custom-button']"
    button_reset = "//form[@id='contactForm']//button[@type='reset'][@id='btnReset'][@class='custom-button']"