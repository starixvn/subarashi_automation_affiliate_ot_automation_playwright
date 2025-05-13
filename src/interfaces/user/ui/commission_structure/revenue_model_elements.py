"""
Revenue Model Elements

This file contains XPath locators for the revenue model section elements.
"""

class RevenueModelElements:
    """
    Class containing XPath locators for revenue model section elements.
    """
    
    # Section container
    div_block_revenue = "//div[@class='block block-revenue']"
    div_page_container = "//div[@class='block block-revenue']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-revenue']/div[@class='page-container']/div[@class='group-page']"
    
    # Title
    div_top_title = "//div[@class='block block-revenue']//div[@class='top-title']"
    
    # Description paragraphs
    div_description = "//div[@class='block block-revenue']//div[@class='description']"
    first_paragraph = "//div[@class='block block-revenue']//div[@class='description'][1]"
    second_paragraph = "//div[@class='block block-revenue']//div[@class='description'][2]"
    
    @staticmethod
    def get_paragraph(index):
        """
        Returns XPath for a specific paragraph by index
        
        Args:
            index: The 1-based index of the paragraph
        """
        return f"//div[@class='block block-revenue']//div[@class='description'][{index}]" 