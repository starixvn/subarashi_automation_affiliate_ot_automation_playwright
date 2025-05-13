"""
FAQ Elements

This file contains XPath locators for the FAQ section elements.
"""

class FAQElements:
    """
    Class containing XPath locators for FAQ section elements.
    """
    
    # Section container
    div_block_faq = "//div[@class='block block-faq']"
    div_page_container = "//div[@class='block block-faq']/div[@class='page-container']"
    div_block_content = "//div[@class='block block-faq']/div[@class='page-container']/div[@class='block-content']"
    
    # First FAQ group - Negative Balance
    div_first_group_faq = "//div[@class='block block-faq']//div[@class='group-faq'][1]"
    div_first_question = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='question']"
    div_first_title = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='question']/div[@class='title']"
    span_first_title_text = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='question']/div[@class='title']/span"
    span_first_button_toggle = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='question']/span[@class='button-toggle open']"
    div_first_answer = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='anwser']"
    div_first_answer_text_1 = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='anwser']/div[@class='anwser-text'][1]"
    div_first_answer_text_2 = "//div[@class='block block-faq']//div[@class='group-faq'][1]/div[@class='anwser']/div[@class='anwser-text'][2]"
    
    # Second FAQ group - Commission Payment
    div_second_group_faq = "//div[@class='block block-faq']//div[@class='group-faq'][2]"
    div_second_question = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='question']"
    div_second_title = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='question']/div[@class='title']"
    span_second_title_text = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='question']/div[@class='title']/span"
    span_second_button_toggle = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='question']/span[@class='button-toggle open']"
    div_second_answer = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']"
    div_second_answer_text_1 = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][1]"
    div_second_answer_text_2 = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][2]"
    div_second_answer_text_3 = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][3]"
    ul_methods = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][2]/ul"
    li_player_account = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][2]/ul/li[1]"
    li_wire_transfer = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']/div[@class='anwser-text'][2]/ul/li[2]"
    span_red_bold = "//div[@class='block block-faq']//div[@class='group-faq'][2]/div[@class='anwser']//span[@class='red-bold']"
    
    @staticmethod
    def get_faq_group(index):
        """
        Returns XPath for a specific FAQ group by index
        
        Args:
            index: The 1-based index of the FAQ group
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq'][{index}]"
    
    @staticmethod
    def get_faq_question(index):
        """
        Returns XPath for a specific FAQ question by group index
        
        Args:
            index: The 1-based index of the FAQ group
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq'][{index}]/div[@class='question']"
    
    @staticmethod
    def get_faq_title(index):
        """
        Returns XPath for a specific FAQ title by group index
        
        Args:
            index: The 1-based index of the FAQ group
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq'][{index}]/div[@class='question']/div[@class='title']/span"
    
    @staticmethod
    def get_faq_answer(index):
        """
        Returns XPath for a specific FAQ answer section by group index
        
        Args:
            index: The 1-based index of the FAQ group
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq'][{index}]/div[@class='anwser']"
    
    @staticmethod
    def get_answer_text(group_index, text_index):
        """
        Returns XPath for a specific answer text by group and text index
        
        Args:
            group_index: The 1-based index of the FAQ group
            text_index: The 1-based index of the text block within the answer
        """
        return f"//div[@class='block block-faq']//div[@class='group-faq'][{group_index}]/div[@class='anwser']/div[@class='anwser-text'][{text_index}]" 