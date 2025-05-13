"""
About Elements

This file contains XPath locators for the About section elements.
"""

class AboutElements:
    """
    Class containing XPath locators for the About section elements.
    """
    
    # Section container
    div_block_about = "//div[@class='block block-about']"
    div_page_container = "//div[@class='block block-about']/div[@class='page-container']"
    div_group_block = "//div[@class='block block-about']/div[@class='page-container']/div[@class='group-block']"
    
    # Section title
    h2_block_title = "//div[@class='block block-about']//h2[@class='block-title']"
    img_title_about = "//div[@class='block block-about']//h2[@class='block-title']/img"
    
    # Content container
    div_block_content = "//div[@class='block block-about']//div[@class='block-content']"
    
    # Paragraphs
    p_first_paragraph = "//div[@class='block block-about']//div[@class='block-content']/p[1]"
    p_second_paragraph = "//div[@class='block block-about']//div[@class='block-content']/p[2]"
    
    @staticmethod
    def get_paragraph(index):
        """
        Returns XPath for a specific paragraph by index
        
        Args:
            index: The 1-based index of the paragraph
        """
        return f"//div[@class='block block-about']//div[@class='block-content']/p[{index}]" 