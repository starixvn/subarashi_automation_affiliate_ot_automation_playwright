"""
Flag Contact Elements

This file contains XPath locators for the flag contact elements on the Contact page.
"""

class FlagContactElements:
    """
    Class containing XPath locators for flag contact elements.
    """
    
    # Block container
    div_block_flag_contact = "//div[@class='block block-flag-contact']"
    div_page_container = "//div[@class='block block-flag-contact']/div[@class='page-container']"
    div_main_flag = "//div[@class='block block-flag-contact']/div[@class='page-container']/div[@class='main-flag']"
    
    # Flag item container
    div_items = "//div[@class='block block-flag-contact']//div[@class='main-flag']/div[@class='items']"
    
    # Single flag elements
    div_single_flag = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='single-flag']"
    img_flag = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='single-flag']/img"
    
    # Info elements
    div_info = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']"
    p_language = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/p[@class='language']"
    a_contact_info = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a[@class='contact-info']"
    a_contact_info_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a[@class='contact-info info-whats-app']"
    
    # Contact icon elements
    img_telegram = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/img[@class='im-icon']"
    img_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/img[@class='im-whats-app']"
    
    # Number container elements
    div_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']"
    span_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/span"
    p_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/p[1]"
    p_phone_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/p[@class='phone-number']"
    span_phone_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/span[@class='phone-number']"
    
    @staticmethod
    def get_flag_contact_block_by_index(index=1):
        """
        Get the XPath for a specific flag contact block by index.
        
        Args:
            index (int): The index of the flag contact block (1-based).
            
        Returns:
            str: XPath locator for the specified flag contact block.
        """
        return f"(//div[@class='block block-flag-contact'])[{index}]"
    
    @staticmethod
    def get_items_by_block_and_index(block_index=1, item_index=1):
        """
        Get the XPath for a specific items container by block and item index.
        
        Args:
            block_index (int): The index of the flag contact block (1-based).
            item_index (int): The index of the items container (1-based).
            
        Returns:
            str: XPath locator for the specified items container.
        """
        return f"(//div[@class='block block-flag-contact'])[{block_index}]//div[@class='main-flag']/div[@class='items'][{item_index}]"
    
    @staticmethod
    def get_flag_by_country(country):
        """
        Get the XPath for a specific country flag.
        
        Args:
            country (str): The country name (english, china, vietnam, thailand, indonesian, india, korea, bangladesh).
            
        Returns:
            str: XPath locator for the specified country flag.
        """
        return f"//div[@class='block block-flag-contact']//div[@class='single-flag']/img[contains(@src, '{country.lower()}')]"
    
    @staticmethod
    def get_language_by_text(language_text):
        """
        Get the XPath for a specific language text.
        
        Args:
            language_text (str): The language text (English Support, China Support, etc.).
            
        Returns:
            str: XPath locator for the specified language text.
        """
        return f"//div[@class='block block-flag-contact']//p[@class='language'][text()='{language_text}']"
    
    @staticmethod
    def get_contact_link_by_platform_and_handle(platform, handle):
        """
        Get the XPath for a specific contact link by platform and handle.
        
        Args:
            platform (str): The platform name (telegram, whatsapp).
            handle (str): The username or handle.
            
        Returns:
            str: XPath locator for the specified contact link.
        """
        if platform.lower() == 'telegram':
            return f"//div[@class='block block-flag-contact']//div[@class='number']/span[text()='{handle}']"
        elif platform.lower() == 'whatsapp':
            return f"//div[@class='block block-flag-contact']//div[@class='number']/p[@class='phone-number'][text()='{handle}'] | //div[@class='block block-flag-contact']//div[@class='number']/span[@class='phone-number'][text()='{handle}']"
        else:
            return f"//div[@class='block block-flag-contact']//div[@class='number']//text()[contains(.,'{handle}')]" 