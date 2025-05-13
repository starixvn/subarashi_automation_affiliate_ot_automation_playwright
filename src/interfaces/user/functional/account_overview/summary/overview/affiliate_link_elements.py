"""
Affiliate Link Elements

This file contains XPath locators for the affiliate link elements on the Account Overview page.
"""

class AffiliateLinkElements:
    """
    Class containing XPath locators for affiliate link elements.
    """
    
    # Affiliate link section container
    div_affiliate_link_section = "//div[@id='affiliate-link-section']"
    
    # Affiliate link form container
    div_affiliate_link_form = "//div[@id='affiliate-link-section']/div[@class='affiliate-link-form']"
    
    # Affiliate link label and input
    label_affiliate_link = "//div[@class='affiliate-link-form']/div[@class='form-group']/label"
    input_affiliate_link = "//div[@class='affiliate-link-form']/div[@class='form-group']/div[@class='input-group']/input[@id='affiliate-link']"
    button_copy = "//div[@class='affiliate-link-form']/div[@class='form-group']/div[@class='input-group']/div[@class='input-group-append']/button[@class='btn btn-copy']"
    img_copy_icon = "//div[@class='affiliate-link-form']//button[@class='btn btn-copy']/img"
    
    # Affiliate link options
    div_options = "//div[@class='affiliate-link-form']/div[@class='options']"
    
    # Language options
    div_language_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option language']"
    select_language = "//div[@class='option language']/select[@id='language']"
    
    # Product options
    div_product_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option product']"
    select_product = "//div[@class='option product']/select[@id='product']"
    
    # URL options
    div_url_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option url']"
    select_url = "//div[@class='option url']/select[@id='url']"
    
    # Campaign options
    div_campaign_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option campaign']"
    input_campaign = "//div[@class='option campaign']/input[@id='campaign']"
    
    # Generate button
    div_generate_button = "//div[@class='affiliate-link-form']/div[@class='generate-button']"
    button_generate = "//div[@class='affiliate-link-form']/div[@class='generate-button']/button[@id='btn-generate']"
    
    # Select options helpers
    @staticmethod
    def get_language_option_by_value(value):
        """
        Get the XPath for a specific language option by its value.
        
        Args:
            value (str): The value of the language option (e.g., 'en-US', 'zh-CN', etc.).
            
        Returns:
            str: XPath locator for the specified language option.
        """
        return f"//div[@class='option language']/select[@id='language']/option[@value='{value}']"
    
    @staticmethod
    def get_product_option_by_value(value):
        """
        Get the XPath for a specific product option by its value.
        
        Args:
            value (str): The value of the product option (e.g., 'sports', 'casino', etc.).
            
        Returns:
            str: XPath locator for the specified product option.
        """
        return f"//div[@class='option product']/select[@id='product']/option[@value='{value}']"
    
    @staticmethod
    def get_url_option_by_value(value):
        """
        Get the XPath for a specific URL option by its value.
        
        Args:
            value (str): The value of the URL option.
            
        Returns:
            str: XPath locator for the specified URL option.
        """
        return f"//div[@class='option url']/select[@id='url']/option[@value='{value}']"
    
    @staticmethod
    def get_language_option_by_text(text):
        """
        Get the XPath for a specific language option by its display text.
        
        Args:
            text (str): The display text of the language option (e.g., 'English', 'Chinese', etc.).
            
        Returns:
            str: XPath locator for the specified language option.
        """
        return f"//div[@class='option language']/select[@id='language']/option[text()='{text}']"
    
    @staticmethod
    def get_product_option_by_text(text):
        """
        Get the XPath for a specific product option by its display text.
        
        Args:
            text (str): The display text of the product option (e.g., 'Sports', 'Casino', etc.).
            
        Returns:
            str: XPath locator for the specified product option.
        """
        return f"//div[@class='option product']/select[@id='product']/option[text()='{text}']"
    
    @staticmethod
    def get_url_option_by_text(text):
        """
        Get the XPath for a specific URL option by its display text.
        
        Args:
            text (str): The display text of the URL option.
            
        Returns:
            str: XPath locator for the specified URL option.
        """
        return f"//div[@class='option url']/select[@id='url']/option[text()='{text}']" 