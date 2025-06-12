class FAQGroupElements:
    
    # Group container
    div_group_faq = "//div[@class='group-faq']"
    div_number = "//div[@class='group-faq']/div[@class='number']"
    
    # Question section
    div_question = "//div[@class='group-faq']/div[@class='question']"
    div_question_title = "//div[@class='group-faq']/div[@class='question']/div[@class='title']"
    span_question_text = "//div[@class='group-faq']/div[@class='question']/div[@class='title']/span"
    span_button_toggle = "//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle']"
    span_button_toggle_open = "//div[@class='group-faq']/div[@class='question']/span[@class='button-toggle open']"
    
    # Answer section
    div_answer = "//div[@class='group-faq']/div[@class='anwser']"
    div_anwser_heading = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-heading']"
    div_answer_text = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']"
    span_red_bold = "//div[@class='group-faq']/div[@class='anwser']/div[@class='anwser-text']/span[@class='red-bold']"
    
    # View more section
    div_view_more = "//div[@class='group-faq']/div[@class='anwser']/div[@class='view-more']"
    a_view_more_link = "//div[@class='group-faq']/div[@class='anwser']/div[@class='view-more']/a[@class='nounderline']"
    img_view_more = "//div[@class='group-faq']/div[@class='anwser']/div[@class='view-more']/a/img[@class='img-item img-responsive']"