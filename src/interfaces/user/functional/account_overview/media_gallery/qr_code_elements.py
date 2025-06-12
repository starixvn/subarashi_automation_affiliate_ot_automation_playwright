class QrCodeElements:
    # Main container elements
    div_qr_code = "//div[@id='qrcode']"
    div_info_group = "//div[@id='qrcode' and @class='info-group']"
    div_title = "//div[@id='qrcode']//div[@class='title']"
    span_title_text = "//div[@id='qrcode']//div[@class='title']/span[@class='text']"

    # QR code container
    div_qr_code_container = "//div[@id='qrcode']//div[@class='qrcode-container']"
    div_qr_panel = "//div[@id='qrcode']//div[@class='qr-panel']"

    # QR code item elements
    div_qr_item = "//div[@id='qrcode']//div[contains(@class, 'qr-item')]"
    div_main_panel = "//div[@id='qrcode']//div[contains(@class, 'main-panel')]"

    # QR image elements
    div_qr_top_content = "//div[@id='qrcode']//div[contains(@class, 'qr-topcontent')]"
    div_qr_img = "//div[@id='qrcode']//div[contains(@class, 'qr-img')]"
    img_default = "//div[@id='qrcode']//img[@class='default-img']"
    img_qrcode = "//div[@id='qrcode']//img[@class='qrcode-img']"

    # QR action elements
    div_qr_action = "//div[@id='qrcode']//div[contains(@class, 'qr-action')]"
    div_flex_space_between = "//div[@id='qrcode']//div[contains(@class, 'flex-space-between')]"
    label_language = "//div[@id='qrcode']//div[contains(@class, 'qr-action')]//label[@class='language']"

    # Toggle button
    div_toggle_btn = "//div[@id='qrcode']//div[contains(@class, 'toggle-btn')]"
    div_toggle = "//div[@id='qrcode']//div[@class='toggle']"
    input_toggle_link = "//div[@id='qrcode']//input[@type='checkbox']"

    # QR buttons
    div_qr_btn_group = "//div[@id='qrcode']//div[contains(@class, 'qr-btn-group')]"
    button_copy_qr = "//div[@id='qrcode']//button[contains(@class, 'btn-copy-qr')]"
    button_save_img = "//div[@id='qrcode']//button[contains(@class, 'btn-save-img')]"

    # Link area elements
    div_qr_link_area = "//div[@id='qrcode']//div[contains(@class, 'qr-link-area')]"
    div_qr_link_display = "//div[@id='qrcode']//div[contains(@class, 'qr-link-display')]"
    span_qr_link = "//div[@id='qrcode']//span[contains(@class, 'qr-link')]"
    button_copy_link = "//div[@id='qrcode']//button[contains(@class, 'btn-copy-link')]"
