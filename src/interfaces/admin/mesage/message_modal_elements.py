class MessageModalElements:
    # Modal dialog container
    mdl_message = "//div[@class='modal-dialog modal-lg']"
    mdl_content = "//div[@class='modal-content']"
    
    # Modal header
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Modal body
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_form_container = "//div[@class='message-form-container']"
    
    # Form elements
    frm_message = "//form[contains(@class, 'mb-2')]"
    
    # Important checkbox
    div_important = "//div[@class='mb-2 row form-group'][1]"
    lbl_important = "//label[@for='important']"
    chk_important = "//input[@name='important']"
    
    # Language text areas
    div_english = "//div[@class='mb-2 row form-group'][2]"
    lbl_english = "//label[@for='Message_en']"
    txt_english = "//textarea[@id='Message_en']"
    
    div_indonesian = "//div[@class='mb-2 row form-group'][3]"
    lbl_indonesian = "//label[@for='Message_id']"
    txt_indonesian = "//textarea[@id='Message_id']"
    
    div_korean = "//div[@class='mb-2 row form-group'][4]"
    lbl_korean = "//label[@for='Message_ko']"
    txt_korean = "//textarea[@id='Message_ko']"
    
    div_thai = "//div[@class='mb-2 row form-group'][5]"
    lbl_thai = "//label[@for='Message_th']"
    txt_thai = "//textarea[@id='Message_th']"
    
    div_vietnamese = "//div[@class='mb-2 row form-group'][6]"
    lbl_vietnamese = "//label[@for='Message_vn']"
    txt_vietnamese = "//textarea[@id='Message_vn']"
    
    div_chinese = "//div[@class='mb-2 row form-group'][7]"
    lbl_chinese = "//label[@for='Message_cs']"
    txt_chinese = "//textarea[@id='Message_cs']"
    
    # Form buttons
    btn_add = "//div[@class='message-form-container']/button[@class='btn btn-success']"
    btn_cancel = "//div[@class='message-form-container']/button[@class='ml-2 btn btn-info']" 