"""
Revenue Definition Elements

This file contains XPath locators for the revenue definition section elements.
"""

class RevenueDefinitionElements:
    """
    Class containing XPath locators for revenue definition section elements.
    """
    
    # Section container
    div_block_text = "//div[@class='block block-text']"
    div_page_container = "//div[@class='block block-text']/div[@class='page-container']"
    div_group_page = "//div[@class='block block-text']/div[@class='page-container']/div[@class='group-page']"
    
    # Text content
    span_font_bold = "//div[@class='block block-text']//span[@class='font-bold']"
    span_i_1 = "//div[@class='block block-text']//span[text()='(i)']"
    span_ii_2 = "//div[@class='block block-text']//span[text()='(ii)']"
    span_iii_3 = "//div[@class='block block-text']//span[text()='(iii)']"
    span_iv_4 = "//div[@class='block block-text']//span[text()='(iv)']" 