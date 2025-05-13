"""
Example Block Elements

This file contains XPath locators for the example block elements on the Affiliate page.
"""

class ExampleBlockElements:
    """
    Class containing XPath locators for the example block elements.
    """
    
    # Block container
    div_block_example = "//div[@class='block block-example']"
    div_page_container = "//div[@class='block block-example']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-example']/div[@class='page-container']/div[@class='group-page']"
    
    # Block title
    div_block_child_title = "//div[@class='block block-example']//div[@class='block-child-title title-spcing']"
    
    # Description paragraphs
    div_description_first = "//div[@class='block block-example']//div[@class='description'][1]"
    div_description_second = "//div[@class='block block-example']//div[@class='description'][2]"
    div_description_third = "//div[@class='block block-example']//div[@class='description'][3]"
    div_description_fourth = "//div[@class='block block-example']//div[@class='description'][4]"
    
    # Red-bold spans within descriptions
    span_red_bold_first = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][1]"
    span_red_bold_second = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][2]"
    span_red_bold_third = "//div[@class='block block-example']//div[@class='description'][1]/span[@class='red-bold'][3]"
    
    @staticmethod
    def get_description_by_index(index=1):
        """
        Get the XPath for a specific description paragraph by index.
        
        Args:
            index (int): The index of the description (1-based).
            
        Returns:
            str: XPath locator for the specified description.
        """
        return f"//div[@class='block block-example']//div[@class='description'][{index}]"
    
    @staticmethod
    def get_red_bold_by_description_and_index(desc_index=1, span_index=1):
        """
        Get the XPath for a specific red-bold span by description and span index.
        
        Args:
            desc_index (int): The index of the description (1-based).
            span_index (int): The index of the span within the description (1-based).
            
        Returns:
            str: XPath locator for the specified red-bold span.
        """
        return f"//div[@class='block block-example']//div[@class='description'][{desc_index}]/span[@class='red-bold'][{span_index}]" 