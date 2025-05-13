class MarketingPageElements:
    """
    This class contains XPath locators for marketing page elements on the affiliate page.
    """
    
    # Main container elements
    div_marketing_banner = "//div[@class='marketing-banner']"
    div_list_content = "//div[@class='marketing-banner']/div[@class='list-content']"
    
    # Banner control elements
    div_banner_control = "//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control']"
    div_banner_link = "//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control']/div[@class='banner-link']"
    img_banner = "//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control']/div[@class='banner-link']/img"
    
    # Banner control button elements
    div_banner_control_button = "//div[@class='banner-control-button']"
    div_banner_code = "//div[@class='banner-control-button']/div[@class='banner-code']"
    p_banner_code_text = "//div[@class='banner-control-button']/div[@class='banner-code']/p"
    a_copy_code = "//div[@class='banner-control-button']/div[@class='banner-code']/a"
    img_copy_icon = "//div[@class='banner-control-button']/div[@class='banner-code']/a/img"
    
    # Social media buttons
    div_social_media_button_group = "//div[@class='banner-control-button']/div[@class='social-media-button-group']"
    a_social_media_button = "//div[@class='banner-control-button']/div[@class='social-media-button-group']/a"
    
    # Social media list
    div_social_media_list = "//div[@class='list-content']/div[@class='social-media-list']"
    span_social_media_name = "//div[@class='list-content']/div[@class='social-media-list']/span"
    
    def get_social_media_button_by_index(self, index):
        """Get a social media button by its index (1-based)."""
        return f"//div[@class='banner-control-button']/div[@class='social-media-button-group']/a[{index}]"
    
    def get_social_media_button_by_platform(self, platform):
        """Get a social media button by its platform name in the title or alt attribute."""
        return f"//div[@class='banner-control-button']/div[@class='social-media-button-group']/a[contains(@title, '{platform}') or ./img[contains(@alt, '{platform}')]]"
    
    def get_banner_control_by_index(self, index):
        """Get a banner control element by its index (1-based)."""
        return f"//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control'][{index}]"
    
    def get_banner_image_by_index(self, index):
        """Get a banner image element by its index (1-based)."""
        return f"//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control'][{index}]/div[@class='banner-link']/img"
    
    def get_banner_code_by_index(self, index):
        """Get a banner code element by its index (1-based)."""
        return f"//div[@class='marketing-banner']/div[@class='list-content']/div[@class='banner-control'][{index}]//div[@class='banner-code']/a"
    
    # Search form elements
    div_info_group = "//div[@class='info-group']"
    div_title = "//div[@class='info-group']/div[@class='title']"
    span_title_text = "//div[@class='info-group']/div[@class='title']/span[@class='text']"
    
    # Search form for marketing
    div_search_container = "//div[@id='searchForm']/div[@class='search-container']"
    form_search = "//div[@class='search-container']/form"
    div_column_form = "//div[@class='search-container']/form/div[@class='column-form']"
    
    # Form inputs and selects
    select_link_type = "//select[@id='AffLinkType']"
    select_target_country = "//select[@id='TargetCountry']"
    select_language = "//select[@id='Language']"
    select_domain = "//select[@id='Domain']"
    select_page = "//select[@id='Page']"
    select_channel = "//select[@id='Channel']"
    
    # Generate button
    button_generate = "//button[@id='btnGenQRCode']"
    
    def get_link_type_option(self, value):
        """Get a link type option by its value."""
        return f"//select[@id='AffLinkType']/option[@value='{value}']"
    
    def get_target_country_option(self, value):
        """Get a target country option by its value."""
        return f"//select[@id='TargetCountry']/option[@value='{value}']"
    
    def get_language_option(self, value):
        """Get a language option by its value."""
        return f"//select[@id='Language']/option[@value='{value}']"
    
    def get_domain_option(self, value):
        """Get a domain option by its value."""
        return f"//select[@id='Domain']/option[@value='{value}']"
    
    def get_page_option(self, value):
        """Get a page option by its value."""
        return f"//select[@id='Page']/option[@value='{value}']"
    
    def get_channel_option(self, value):
        """Get a channel option by its value."""
        return f"//select[@id='Channel']/option[@value='{value}']"
    
    def get_channel_option_by_text(self, text):
        """Get a channel option by its display text."""
        return f"//select[@id='Channel']/option[text()='{text}']" 