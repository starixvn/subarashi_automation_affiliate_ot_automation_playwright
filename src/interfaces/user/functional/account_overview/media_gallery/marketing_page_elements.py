class MarketingPageElements:
    """
    Class containing XPath locators for the Marketing Page elements on the Affiliate page.
    These elements are used to display and interact with marketing banners and materials.
    """

    # Main container elements
    div_marketing_banner = "//div[@id='marketingBanner']"
    div_list_content = "//div[@id='marketingBanner']//div[@class='list-content']"
    
    # Banner control elements
    div_banner_control = "//div[@id='marketingBanner']//div[contains(@class, 'banner-control')]"
    div_banner_link = "//div[@id='marketingBanner']//div[contains(@class, 'banner-link')]"
    img_banner = "//div[@id='marketingBanner']//img[contains(@class, 'banner')]"
    
    # Banner control button elements
    div_banner_control_button = "//div[@id='marketingBanner']//div[contains(@class, 'control-button')]"
    div_banner_code = "//div[@id='marketingBanner']//div[contains(@class, 'banner-code')]"
    p_banner_code_text = "//div[@id='marketingBanner']//p[contains(@class, 'code-text')]"
    a_copy_code = "//div[@id='marketingBanner']//a[contains(@class, 'copy-code')]"
    img_copy_icon = "//div[@id='marketingBanner']//img[contains(@class, 'copy-icon')]"
    
    # Social media buttons
    div_social_media_button_group = "//div[@id='marketingBanner']//div[contains(@class, 'social-media-button-group')]"
    a_social_media_button = "//div[@id='marketingBanner']//a[contains(@class, 'social-media-button')]"
    
    # Social media list
    div_social_media_list = "//div[@id='marketingBanner']//div[contains(@class, 'social-media-list')]"
    span_social_media_name = "//div[@id='marketingBanner']//span[contains(@class, 'social-media-name')]"
    
    # Search form info group
    div_info_group = "//div[@id='marketingBanner']//div[contains(@class, 'info-group')]"
    div_title = "//div[@id='marketingBanner']//div[@class='title']"
    span_title_text = "//div[@id='marketingBanner']//div[@class='title']/span[@class='text']"
    
    # Marketing content
    div_marketing_content = "//div[@id='marketingBanner']//div[@class='marketing-content']"
    
    # Gallery navigation
    a_gallery_prev = "//div[@id='marketingBanner']//a[contains(@class, 'gallery-prev')]"
    a_gallery_next = "//div[@id='marketingBanner']//a[contains(@class, 'gallery-next')]"
    
    def get_banner_control_by_index(self, index):
        """Get banner control element by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-control')][{index}]"
    
    def get_banner_link_by_index(self, index):
        """Get banner link element by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-link')][{index}]"
    
    def get_banner_image_by_index(self, index):
        """Get banner image element by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-control')][{index}]//img[contains(@class, 'banner')]"
    
    def get_banner_code_by_index(self, index):
        """Get banner code element by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-control')][{index}]//div[contains(@class, 'banner-code')]"
    
    def get_code_text_by_index(self, index):
        """Get code text element by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-control')][{index}]//p[contains(@class, 'code-text')]"
    
    def get_copy_code_by_index(self, index):
        """Get copy code button by index (1-based)"""
        return f"//div[@id='marketingBanner']//div[contains(@class, 'banner-control')][{index}]//a[contains(@class, 'copy-code')]"
    
    def get_social_media_button_by_index(self, index):
        """Get social media button by index (1-based)"""
        return f"//div[@id='marketingBanner']//a[contains(@class, 'social-media-button')][{index}]"
    
    def get_social_media_button_by_name(self, name):
        """Get social media button by name"""
        return f"//div[@id='marketingBanner']//a[contains(@class, 'social-media-button')][.//span[contains(text(), '{name}')]]" 