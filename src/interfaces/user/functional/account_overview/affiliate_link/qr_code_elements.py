class QrCodeElements:
    
    # Main container elements
    div_qr_code = "//div[@class='qr-code']"
    div_info_group = "//div[@class='qr-code']/div[@class='info-group']"
    div_title = "//div[@class='qr-code']/div[@class='info-group']/div[@class='title']"
    span_title_text = "//div[@class='qr-code']/div[@class='info-group']/div[@class='title']/span[@class='text']"
    
    # QR code container
    div_qr_code_container = "//div[@id='qr-code']"
    div_qr_panel = "//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']"
    
    # QR code item elements
    div_qr_item = "//div[@class='qr-item']"
    div_main_panel = "//div[@class='qr-item']/div[@class='main-panel']"
    
    # QR image elements
    div_qr_top_content = "//div[@class='qr-item']/div[@class='main-panel']/div[@class='qr-top-content flex']"
    div_qr_img = "//div[@class='qr-top-content flex']/div[@class='qr-img']"
    img_default = "//div[@class='qr-img']/img[@class='default']"
    img_qrcode = "//div[@class='qr-img']/img[@class='qrcode']"
    
    # QR action elements
    div_qr_action = "//div[@class='qr-top-content flex']/div[@class='qr-action']"
    div_flex_space_between = "//div[@class='qr-action']/div[@class='flex space-between']"
    label_language = "//div[@class='flex space-between']/div/label"
    
    # Toggle button
    div_toggle_btn = "//div[@class='flex space-between']/div[@class='toggle-btn']"
    div_toggle = "//div[@class='toggle-btn']/div[@class='toggle btn btn-primary']"
    input_toggle_link = "//div[@class='toggle btn btn-primary']/input[@class='toggle-link']"
    
    # QR buttons
    div_qr_btn_group = "//div[@class='qr-action']/div[@class='qr-btn-group']"
    button_copy_qr = "//div[@class='qr-btn-group']/button[@class='btn-copy-qr']"
    button_save_img = "//div[@class='qr-btn-group']/button[@class='btn-save-img']"
    
    # Link area elements
    div_qr_link_area = "//div[@class='qr-item']/div[@class='qr-link-area']"
    div_qr_link_display = "//div[@class='qr-link-area']/div[@class='qr-link-display']"
    button_copy_link = "//div[@class='qr-link-area']/button[@class='btn-copy-link']"
    