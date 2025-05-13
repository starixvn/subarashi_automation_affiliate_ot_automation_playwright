"""
Footer Elements

This file contains XPath locators for footer elements.
"""

class FooterElements:
    """
    Class containing XPath locators for footer elements.
    """
    
    # Footer container
    footer_container = "//footer[@class='footer']"
    div_footer_inner = "//footer[@class='footer']/div[@class='footer-inner']"
    
    # Footer top
    div_ft_top = "//footer[@class='footer']//div[@class='ft-top']"
    
    # Partner logos
    div_partner_logo = "//footer[@class='footer']//div[@class='partner-logo']"
    div_plg_wrapper = "//footer[@class='footer']//div[@class='plg-wrapper']"
    a_partner_links = "//footer[@class='footer']//div[@class='plg-wrapper']/a"
    img_partner_logos = "//footer[@class='footer']//div[@class='plg-wrapper']/a/img"
    
    # Bank logos
    div_bank_logo = "//footer[@class='footer']//div[@class='bank-logo']"
    div_blg_wrapper = "//footer[@class='footer']//div[@class='blg-wrapper']"
    img_bank_logos = "//footer[@class='footer']//div[@class='blg-wrapper']/img"
    
    # Footer middle
    div_ft_mid = "//footer[@class='footer']//div[@class='ft-mid']"
    
    # Support information
    div_support_info = "//footer[@class='footer']//div[@class='support-info']"
    div_support_phone = "//footer[@class='footer']//div[@class='support-info']/div[@class='support-phone']"
    div_support_email = "//footer[@class='footer']//div[@class='support-info']/div[@class='support-email']"
    
    # Footer bottom
    div_ft_bot = "//footer[@class='footer']//div[@class='ft-bot']"
    div_copyright = "//footer[@class='footer']//div[@class='copyright']"
    div_copyright_text = "//footer[@class='footer']//div[@class='copyright']/span"
    
    # Social links
    div_social_link = "//footer[@class='footer']//div[@class='social-link']"
    ul_social_list = "//footer[@class='footer']//div[@class='social-link']/ul"
    li_social_items = "//footer[@class='footer']//div[@class='social-link']/ul/li"
    
    @staticmethod
    def get_social_item_by_index(index):
        """
        Returns XPath for a social media link by its index
        
        Args:
            index: The 1-based index of the social media item
        """
        return f"//footer[@class='footer']//div[@class='social-link']/ul/li[{index}]"
    
    @staticmethod
    def get_social_link_by_index(index):
        """
        Returns XPath for a social media anchor by its index
        
        Args:
            index: The 1-based index of the social media item
        """
        return f"//footer[@class='footer']//div[@class='social-link']/ul/li[{index}]/a"
    
    @staticmethod
    def get_partner_logo_by_index(index):
        """
        Returns XPath for a partner logo by its index
        
        Args:
            index: The 1-based index of the partner logo
        """
        return f"//footer[@class='footer']//div[@class='plg-wrapper']/a[{index}]/img" 