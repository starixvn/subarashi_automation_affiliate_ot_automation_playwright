class QrCodeElements:
    """
    This class contains XPath locators for QR code elements on the affiliate page.
    """
    
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
    
    def get_qr_item_by_index(self, index):
        """Get a QR item by its index (1-based)."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][{index}]"
    
    def get_qr_item_by_language(self, language):
        """Get a QR item by its language label."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]"
    
    def get_qr_item_by_link_containing(self, link_text):
        """Get a QR item by partial content of its link."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//div[@class='qr-link-display'][contains(text(), '{link_text}')]]"
    
    def get_qr_image_by_language(self, language):
        """Get a QR code image by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//img[@class='qrcode']"
    
    def get_copy_qr_button_by_language(self, language):
        """Get a copy QR button by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//button[@class='btn-copy-qr']"
    
    def get_save_img_button_by_language(self, language):
        """Get a save image button by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//button[@class='btn-save-img']"
    
    def get_link_display_by_language(self, language):
        """Get a link display by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//div[@class='qr-link-display']"
    
    def get_copy_link_button_by_language(self, language):
        """Get a copy link button by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//button[@class='btn-copy-link']"
    
    def get_toggle_by_language(self, language):
        """Get a toggle button by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]//div[@class='toggle btn btn-primary']"
    
    # QR item data attributes
    def get_qr_item_data_attribute(self, language, attribute_name):
        """Get a data attribute from a QR item by language."""
        return f"//div[@id='qr-code']/div[@class='flex flex-wrap qr-panel']/div[@class='qr-item'][.//label[text()='{language}']]/@data-{attribute_name}" 