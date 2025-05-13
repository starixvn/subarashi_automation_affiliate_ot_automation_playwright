"""
FAQ Block Elements

This file contains XPath locators for FAQ block container elements.
"""

class FAQBlockElements:
    """
    Class containing XPath locators for FAQ block container elements.
    """
    
    # Block container
    div_block_faq = "//div[@class='block block-faq']"
    
    # Block content containers
    div_block_content = "//div[@class='block block-faq']/div[@class='block-content']"
    div_page_container = "//div[@class='block block-faq']/div[@class='block-content']/div[@class='page-container']"
    
    @staticmethod
    def get_block_content_by_index(index=1):
        """
        Get the XPath for a specific block content by index.
        
        Args:
            index (int): The index of the block content (1-based).
            
        Returns:
            str: XPath locator for the specified block content.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{index}]"
    
    @staticmethod
    def get_page_container_by_index(index=1):
        """
        Get the XPath for a specific page container by index.
        
        Args:
            index (int): The index of the page container (1-based).
            
        Returns:
            str: XPath locator for the specified page container.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{index}]/div[@class='page-container']" 