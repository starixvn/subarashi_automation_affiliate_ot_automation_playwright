class SearchFormElements:
    
    # Main container elements
    div_search_form = "//div[@id='searchForm']"
    div_info_group = "//div[@id='searchForm'][@class='info-group']"
    div_title = "//div[@id='searchForm']/div[@class='title']"
    span_title_text = "//div[@id='searchForm']/div[@class='title']/span[@class='text']"
    
    # Search container
    div_search_container = "//div[@id='searchForm']/div[@class='search-container']"
    form_search = "//div[@class='search-container']/form"
    
    # Form columns
    div_column_form_first = "(//div[@class='search-container']/form/div[@class='column-form'])[1]"
    div_column_form_second = "(//div[@class='search-container']/form/div[@class='column-form'])[2]"
    
    # Form groups in first column
    div_form_group_link_type = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='AffLinkType']]"
    label_link_type = "//label[@class='control-label'][@for='AffLinkType']"
    div_control_input_link_type = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='AffLinkType']]/div[@class='control-input']"
    select_link_type = "//select[@id='AffLinkType']"
    option_affiliate_link = "//select[@id='AffLinkType']/option[@value='AffiliateLink']"
    
    div_form_group_target_country = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='TargetCountry']]"
    label_target_country = "//label[@class='control-label'][@for='TargetCountry']"
    div_control_input_target_country = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='TargetCountry']]/div[@class='control-input']"
    select_target_country = "//select[@id='TargetCountry']"
    
    div_form_group_language = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Language']]"
    label_language = "//label[@class='control-label'][@for='Language']"
    div_control_input_language = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Language']]/div[@class='control-input']"
    select_language = "//select[@id='Language']"
    
    # Form groups in second column
    div_form_group_domain = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Domain']]"
    label_domain = "//label[@class='control-label'][@for='Domain']"
    div_control_input_domain = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Domain']]/div[@class='control-input']"
    select_domain = "//select[@id='Domain']"
    
    div_form_group_page = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Page']]"
    label_page = "//label[@class='control-label'][@for='Page']"
    div_control_input_page = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Page']]/div[@class='control-input']"
    select_page = "//select[@id='Page']"
    
    div_form_group_channel = "//div[@class='column-form']//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Channel']]"
    label_channel = "//label[@class='control-label'][@for='Channel']"
    div_control_input_channel = "//div[@class='form-group flex-sm-boostrap flex-center'][./label[@for='Channel']]/div[@class='control-input']"
    select_channel = "//select[@id='Channel']"
    
    # Generate button
    div_form_group_button = "//div[@class='form-group flex-sm-boostrap flex-center form-group-button']"
    label_none = "//label[@class='control-label none-label']"
    button_generate = "//button[@id='btnGenQRCode']"
    
