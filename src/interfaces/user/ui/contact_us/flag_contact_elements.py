class FlagContactElements:
    
    # Block container
    div_block_flag_contact = "//div[@class='block block-flag-contact']"
    div_page_container = "//div[@class='block block-flag-contact']/div[@class='page-container']"
    div_main_flag = "//div[@class='block block-flag-contact']/div[@class='page-container']/div[@class='main-flag']"
    
    # Flag item container
    div_items = "//div[@class='block block-flag-contact']//div[@class='main-flag']/div[@class='items']"
    
    # Single flag elements
    div_single_flag = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='single-flag']"
    img_flag = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='single-flag']/img"
    
    # Info elements
    div_info = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']"
    p_language = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/p[@class='language']"
    a_contact_info = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a[@class='contact-info']"
    a_contact_info_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a[@class='contact-info info-whats-app']"
    
    # Contact icon elements
    img_telegram = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/img[@class='im-icon']"
    img_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/img[@class='im-whats-app']"
    
    # Number container elements
    div_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']"
    span_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/span"
    p_whatsapp = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/p[1]"
    p_phone_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/p[@class='phone-number']"
    span_phone_number = "//div[@class='block block-flag-contact']//div[@class='items']/div[@class='info']/a/div[@class='number']/span[@class='phone-number']"