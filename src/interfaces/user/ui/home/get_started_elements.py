"""
Get Started Elements

This file contains XPath locators for the "Get Started" section elements.
"""

class GetStartedElements:
    """
    Class containing XPath locators for the Get Started section elements.
    """
    
    # Section container
    div_block_get_started = "//div[@class='block block-get-started']"
    div_page_container = "//div[@class='block block-get-started']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-get-started']//h2[@class='block-title']"
    
    # Wrapper block
    div_wrapper_block = "//div[@class='block block-get-started']//div[@class='wrapper-block']"
    
    # Content container
    div_block_content = "//div[@class='block block-get-started']//div[@class='wrapper-block']/div[@class='block-content']"
    
    # Step items
    div_items = "//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items']"
    
    # Join now button
    div_text_center = "//div[@class='block block-get-started']//div[@class='wrapper-block']/div[@class='text-center']"
    a_join_now = "//div[@class='block block-get-started']//a[@class='custom-button']"
    
    @staticmethod
    def get_step_item(index):
        """
        Returns XPath for a specific step item by index
        
        Args:
            index: The 1-based index of the step item
        """
        return f"//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items'][{index}]"
    
    @staticmethod
    def get_step_number(index):
        """
        Returns XPath for the number of a specific step
        
        Args:
            index: The 1-based index of the step item
        """
        return f"//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items'][{index}]/span[@class='number']"
    
    @staticmethod
    def get_step_icon(index):
        """
        Returns XPath for the icon of a specific step
        
        Args:
            index: The 1-based index of the step item
        """
        return f"//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items'][{index}]/div[@class='icon']/img"
    
    @staticmethod
    def get_step_heading(index):
        """
        Returns XPath for the heading of a specific step
        
        Args:
            index: The 1-based index of the step item
        """
        return f"//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items'][{index}]/div[@class='heading-items']"
    
    @staticmethod
    def get_step_description(index):
        """
        Returns XPath for the description of a specific step
        
        Args:
            index: The 1-based index of the step item
        """
        return f"//div[@class='block block-get-started']//div[@class='block-content']/div[@class='items'][{index}]/div[@class='description']" 