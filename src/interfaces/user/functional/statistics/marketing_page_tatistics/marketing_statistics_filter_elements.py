class MarketingStatisticsFilterElements:

    # Main container elements
    div_main_panel = "//div[@id='mainPanel']"
    div_sub_content = "//div[@class='sub-content']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_page_title_text = "//div[@class='page-title']/span[@class='text']"
    
    # Info group container
    div_info_group = "//div[@class='info-group']"
    
    # Filter form
    form_filter = "//form[@class='form-inline form-filter']"
    
    # Date range - From
    div_form_group_from = "//form[@class='form-inline form-filter']/div[@class='form-group'][./label[text()='From:']]"
    label_from = "//form[@class='form-inline form-filter']//label[text()='From:']"
    div_from_picker = "//div[@id='fromPicker']"
    input_from_date = "//input[@id='FromDate']"
    span_from_calendar_icon = "//div[@id='fromPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    # Date range - To
    div_form_group_to = "//form[@class='form-inline form-filter']/div[@class='form-group'][./label[text()='To:']]"
    label_to = "//form[@class='form-inline form-filter']//label[text()='To:']"
    div_to_picker = "//div[@id='toPicker']"
    input_to_date = "//input[@id='ToDate']"
    span_to_calendar_icon = "//div[@id='toPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    # Language filter
    div_form_group_language = "//form[@class='form-inline form-filter']/div[@class='form-group'][./label[text()='Language:']]"
    label_language = "//form[@class='form-inline form-filter']//label[text()='Language:']"
    select_language = "//select[@id='language']"
    
    # Language options
    option_all = "//select[@id='language']/option[@value='']"
    option_english = "//select[@id='language']/option[@value='en-US']"
    option_english_bangladesh = "//select[@id='language']/option[@value='bn-BD']"
    option_english_india = "//select[@id='language']/option[@value='en-IN']"
    option_indonesian = "//select[@id='language']/option[@value='id-ID']"
    option_japanese = "//select[@id='language']/option[@value='ja-JP']"
    option_korean = "//select[@id='language']/option[@value='ko-KR']"
    option_thai = "//select[@id='language']/option[@value='th-TH']"
    option_vietnamese = "//select[@id='language']/option[@value='vi-VN']"
    option_chinese_simplified = "//select[@id='language']/option[@value='zh-CN']"
    option_telugu = "//select[@id='language']/option[@value='te-IN']"
    option_english_europe = "//select[@id='language']/option[@value='en-GB']"
    
    # Include inactive checkbox
    div_checkbox_group = "//form[@class='form-inline form-filter']/div[@class='checkbox form-group']"
    span_checkbox_label = "//form[@class='form-inline form-filter']//span[@class='text-bold']"
    input_include_inactive = "//input[@id='includeInActive']"
    
    # Submit button
    button_submit = "//button[@id='btnStatisticsSubmit']"