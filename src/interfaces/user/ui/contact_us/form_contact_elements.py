class FormContactElements:
    
    # Block container
    div_block_form_contact = "//div[@class='block block-form-contact']"
    div_page_container = "//div[@class='block block-form-contact']/div[@class='page-container']"
    div_main_contact = "//div[@class='block block-form-contact']/div[@class='page-container']/div[@class='main-contact']"
    
    # Title elements
    div_title = "//div[@class='block block-form-contact']//div[@class='title']"
    div_logo = "//div[@class='block block-form-contact']//div[@class='title']/div[@class='logo']"
    img_logo = "//div[@class='block block-form-contact']//div[@class='title']/div[@class='logo']/img"
    h4_title = "//div[@class='block block-form-contact']//div[@class='title']/h4"
    
    # Form container
    form_contact_us = "//div[@class='block block-form-contact']//form[@class='form-contact-us']"
    
    # Form fields - Name
    div_name_group = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][1]"
    label_name = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][1]/label"
    div_input_group_name = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][1]/div[@class='input-group']"
    input_name = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][1]/div[@class='input-group']/input[@id='name']"
    div_invalid_feedback_name = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][1]/div[@class='invalid-feedback']"
    
    # Form fields - Email
    div_email_group = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][2]"
    label_email = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][2]/label"
    div_input_group_email = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][2]/div[@class='input-group']"
    input_email = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][2]/div[@class='input-group']/input[@id='email']"
    div_invalid_feedback_email = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][2]/div[@class='invalid-feedback']"
    
    # Form fields - Subject
    div_subject_group = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][3]"
    label_subject = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][3]/label"
    div_input_group_subject = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][3]/div[@class='input-group']"
    input_subject = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][3]/div[@class='input-group']/input[@id='subject']"
    div_invalid_feedback_subject = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][3]/div[@class='invalid-feedback']"
    
    # Form fields - Message
    div_message_group = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][4]"
    label_message = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][4]/label"
    div_input_group_message = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][4]/div[@class='input-group']"
    textarea_message = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][4]/div[@class='input-group']/textarea[@id='message']"
    div_invalid_feedback_message = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][4]/div[@class='invalid-feedback']"
    
    # Form fields - Attachment
    div_attachment_group = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]"
    label_attachment = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]/label"
    div_custom_file = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]/div[@class='custom-file']"
    input_attachment = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]/div[@class='custom-file']/input[@id='attachment']"
    label_custom_file = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]/div[@class='custom-file']/label[@class='custom-file-label']"
    div_invalid_feedback_attachment = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-group'][5]/div[@class='invalid-feedback']"
    
    # Submit button
    div_form_submit = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-submit']"
    button_submit = "//div[@class='block block-form-contact']//form[@class='form-contact-us']/div[@class='form-submit']/button[@type='submit']"