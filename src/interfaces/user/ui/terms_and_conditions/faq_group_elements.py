"""
FAQ Group Elements

This file contains XPath locators for FAQ group elements.
"""

class FAQGroupElements:
    """
    Class containing XPath locators for FAQ group elements.
    """
    
    # Group container
    div_group_faq = "//div[@class='group-faq']"
    div_number = "//div[@class='group-faq']/div[@class='number']"
    div_question = "//div[@class='group-faq']/div[@class='question']"
    div_question_title = "//div[@class='group-faq']/div[@class='question']/div[@class='title']"
    span_question_text = "//div[@class='group-faq']/div[@class='question']/div[@class='title']/span"
    span_button_toggle = "//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle']"
    div_answer = "//div[@class='group-faq']/div[@class='anwser']"
    div_answer_text = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']"
    span_list_number = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']/span[@class='list-number']"
    span_answer_heading = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']/span[@class='anwser-heading']"
    div_view_more = "//div[@class='group-faq']/div[@class='anwser']/div[@class='view-more']"
    
    @staticmethod
    def get_group_by_index(block_index, group_index):
        """
        Get the XPath for a specific FAQ group by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified FAQ group.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]"
    
    @staticmethod
    def get_number_by_index(block_index, group_index):
        """
        Get the XPath for a specific number element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified number element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='number']"
    
    @staticmethod
    def get_question_by_index(block_index, group_index):
        """
        Get the XPath for a specific question element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified question element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='question']"
    
    @staticmethod
    def get_question_title_by_index(block_index, group_index):
        """
        Get the XPath for a specific question title element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified question title element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='question']/div[@class='title']"
    
    @staticmethod
    def get_question_text_by_index(block_index, group_index):
        """
        Get the XPath for a specific question text element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified question text element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='question']/div[@class='title']/span"
    
    @staticmethod
    def get_button_toggle_by_index(block_index, group_index):
        """
        Get the XPath for a specific button toggle element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified button toggle element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='question']/span[@class='button-toggle']"
    
    @staticmethod
    def get_answer_by_index(block_index, group_index):
        """
        Get the XPath for a specific answer element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified answer element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='anwser']"
    
    @staticmethod
    def get_answer_text_by_index(block_index, group_index, text_index=1):
        """
        Get the XPath for a specific answer text element by block, group, and text index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            text_index (int): The index of the answer text within the answer element (1-based).
            
        Returns:
            str: XPath locator for the specified answer text element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='anwser']/div[@class='anwser-text'][{text_index}]"
    
    @staticmethod
    def get_list_number_by_index(block_index, group_index, text_index=1):
        """
        Get the XPath for a specific list number element by block, group, and text index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            text_index (int): The index of the answer text within the answer element (1-based).
            
        Returns:
            str: XPath locator for the specified list number element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='anwser']/div[@class='anwser-text'][{text_index}]/span[@class='list-number']"
    
    @staticmethod
    def get_answer_heading_by_index(block_index, group_index, text_index=1):
        """
        Get the XPath for a specific answer heading element by block, group, and text index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            text_index (int): The index of the answer text within the answer element (1-based).
            
        Returns:
            str: XPath locator for the specified answer heading element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='anwser']/div[@class='anwser-text'][{text_index}]/span[@class='anwser-heading']"
    
    @staticmethod
    def get_view_more_by_index(block_index, group_index):
        """
        Get the XPath for a specific view more element by block and group index.
        
        Args:
            block_index (int): The index of the block content (1-based).
            group_index (int): The index of the group within the block (1-based).
            
        Returns:
            str: XPath locator for the specified view more element.
        """
        return f"//div[@class='block block-faq']/div[@class='block-content'][{block_index}]/div[@class='page-container']/div[@class='group-faq'][{group_index}]/div[@class='anwser']/div[@class='view-more']" 