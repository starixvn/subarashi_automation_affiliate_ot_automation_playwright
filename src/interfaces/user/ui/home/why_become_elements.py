"""
Why Become Elements

This file contains XPath locators for the "Why become a 12BET Affiliate" section elements.
"""

class WhyBecomeElements:
    """
    Class containing XPath locators for the Why Become section elements.
    """
    
    # Section container
    div_block_why_become = "//div[@class='block block-why-become']"
    div_page_container = "//div[@class='block block-why-become']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-why-become']//h2[@class='block-title']"
    span_why_become = "//div[@class='block block-why-become']//h2[@class='block-title']/span[@class='why-become']"
    img_title = "//div[@class='block block-why-become']//h2[@class='block-title']/img"
    span_affiliate = "//div[@class='block block-why-become']//h2[@class='block-title']/span[@class='affiliate']"
    
    # Content container
    div_block_content = "//div[@class='block block-why-become']//div[@class='block-content']"
    
    # Benefit items
    div_items = "//div[@class='block block-why-become']//div[@class='block-content']/div[@class='items']"
    
    @staticmethod
    def get_item(index):
        """
        Returns XPath for a specific benefit item by index
        
        Args:
            index: The 1-based index of the benefit item
        """
        return f"//div[@class='block block-why-become']//div[@class='block-content']/div[@class='items'][{index}]"
    
    @staticmethod
    def get_item_image(index):
        """
        Returns XPath for the image of a specific benefit item
        
        Args:
            index: The 1-based index of the benefit item
        """
        return f"//div[@class='block block-why-become']//div[@class='block-content']/div[@class='items'][{index}]/img"
    
    @staticmethod
    def get_item_heading(index):
        """
        Returns XPath for the heading of a specific benefit item
        
        Args:
            index: The 1-based index of the benefit item
        """
        return f"//div[@class='block block-why-become']//div[@class='block-content']/div[@class='items'][{index}]/div[@class='heading-items']"
    
    @staticmethod
    def get_item_wrap_text(index):
        """
        Returns XPath for the wrapped text in a specific benefit item heading
        
        Args:
            index: The 1-based index of the benefit item
        """
        return f"//div[@class='block block-why-become']//div[@class='block-content']/div[@class='items'][{index}]/div[@class='heading-items']/span[@class='wrap']" 