class AffiliateLinkElements:
    
    # Affiliate link section container
    div_affiliate_link_section = "//div[@id='affiliate-link-section']"
    
    # Affiliate link form container
    div_affiliate_link_form = "//div[@id='affiliate-link-section']/div[@class='affiliate-link-form']"
    
    # Affiliate link label and input
    label_affiliate_link = "//div[@class='affiliate-link-form']/div[@class='form-group']/label"
    input_affiliate_link = "//div[@class='affiliate-link-form']/div[@class='form-group']/div[@class='input-group']/input[@id='affiliate-link']"
    button_copy = "//div[@class='affiliate-link-form']/div[@class='form-group']/div[@class='input-group']/div[@class='input-group-append']/button[@class='btn btn-copy']"
    img_copy_icon = "//div[@class='affiliate-link-form']//button[@class='btn btn-copy']/img"
    
    # Affiliate link options
    div_options = "//div[@class='affiliate-link-form']/div[@class='options']"
    
    # Language options
    div_language_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option language']"
    select_language = "//div[@class='option language']/select[@id='language']"
    
    # Product options
    div_product_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option product']"
    select_product = "//div[@class='option product']/select[@id='product']"
    
    # URL options
    div_url_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option url']"
    select_url = "//div[@class='option url']/select[@id='url']"
    
    # Campaign options
    div_campaign_option = "//div[@class='affiliate-link-form']/div[@class='options']/div[@class='option campaign']"
    input_campaign = "//div[@class='option campaign']/input[@id='campaign']"
    
    # Generate button
    div_generate_button = "//div[@class='affiliate-link-form']/div[@class='generate-button']"
    button_generate = "//div[@class='affiliate-link-form']/div[@class='generate-button']/button[@id='btn-generate']"