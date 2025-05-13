"""
FAQ Elements

This file contains XPath locators for the FAQ section elements.
"""

class FAQElements:
    """
    Class containing XPath locators for the FAQ section elements.
    """
    
    # Section container
    div_block_faq = "//div[@class='block block-faq']"
    div_page_container = "//div[@class='block block-faq']/div[@class='page-container']"
    
    # Section title
    h2_block_title = "//div[@class='block block-faq']//h2[@class='block-title fill-color']"
    
    # Content container
    div_block_content = "//div[@class='block block-faq']//div[@class='block-content']"
    
    # FAQ group
    div_group_faq = "//div[@class='block block-faq']//div[@class='group-faq']"
    div_number = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='number']"
    
    # Question section
    div_question = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']"
    div_title = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/div[@class='title']"
    span_title_text = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/div[@class='title']/span"
    span_button_toggle = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle open']"
    
    # Answer section
    div_answer = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']"
    
    # FAQ items
    div_answer_heading = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-heading']"
    div_answer_text = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']"
    
    # More FAQs button
    div_text_center = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='text-center']"
    a_more_faqs = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='text-center']/a"
    
    @staticmethod
    def get_faq_heading(index):
        """
        Returns XPath for a specific FAQ heading by index
        
        Args:
            index: The 1-based index of the FAQ heading
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-heading'][{index}]"
    
    @staticmethod
    def get_faq_text(index):
        """
        Returns XPath for a specific FAQ text by index
        
        Args:
            index: The 1-based index of the FAQ text
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][{index}]" 