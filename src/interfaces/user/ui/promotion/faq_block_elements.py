class FAQBlockElements:
    
    # Block container
    div_block_faq = "//div[@class='block block-faq']"
    div_block_content = "//div[@class='block block-faq']/div[@class='block-content']"
    div_page_container = "//div[@class='block block-faq']/div[@class='block-content']/div[@class='page-container']"
    
    # FAQ group container
    div_group_faq = "//div[@class='block block-faq']//div[@class='group-faq']"
    
    # Question section
    div_question = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']"
    div_title = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/div[@class='title']"
    span_title_text = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/div[@class='title']/span"
    span_button_toggle = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle']"
    span_button_toggle_open = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle open']"
    
    # Answer section
    div_answer = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']"
    div_answer_heading = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-heading']"
    
    # Answer text items
    div_answer_text_first = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][1]"
    div_answer_text_second = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][2]"
    div_answer_text_third = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][3]"
    div_answer_text_fourth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][4]"
    div_answer_text_fifth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][5]"
    div_answer_text_sixth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][6]"
    
    # List numbers in answer text
    span_list_number_first = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][1]/span[@class='list-number']"
    span_list_number_second = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][2]/span[@class='list-number']"
    span_list_number_third = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][3]/span[@class='list-number']"
    span_list_number_fourth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][4]/span[@class='list-number']"
    span_list_number_fifth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][5]/span[@class='list-number']"
    span_list_number_sixth = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][6]/span[@class='list-number']"
    
    # Link in answer text
    a_terms_link = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][6]/a[@href='/UserAsian/en/TermAndCondition']"
    span_red_bold_in_link = "//div[@class='block block-faq']//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text'][6]/a/span[@class='red-bold']"