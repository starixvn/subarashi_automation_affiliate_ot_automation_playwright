class LandingPagesFilterElements:
    
    # Main container
    div_main_panel = "//div[@id='mainPanel']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_page_title_text = "//div[@class='page-title']/span[@class='text']"
    
    # Device filter
    div_form_group_device = "//form[@class='form-inline form-filter']/div[@class='form-group'][1]"
    label_device = "//form[@class='form-inline form-filter']/div[@class='form-group'][1]/label"
    select_device = "//select[@id='DeviceType']"
    option_device_all = "//select[@id='DeviceType']/option[@value='-1']"
    option_device_pc = "//select[@id='DeviceType']/option[@value='0']"
    option_device_mobile = "//select[@id='DeviceType']/option[@value='1']"
    
    # Language filter
    div_form_group_language = "//form[@class='form-inline form-filter']/div[@class='form-group'][2]"
    label_language = "//form[@class='form-inline form-filter']/div[@class='form-group'][2]/label"
    select_language = "//select[@id='Language']"
    option_language_all = "//select[@id='Language']/option[@value='']"
    
    # Page filter
    div_form_group_page = "//form[@class='form-inline form-filter']/div[@class='form-group'][3]"
    label_page = "//form[@class='form-inline form-filter']/div[@class='form-group'][3]/label"
    select_page = "//select[@id='SportCode']"
    option_page_all = "//select[@id='SportCode']/option[@value='']"
    
    # Date range filter
    div_form_group_from_date = "//form[@class='form-inline form-filter'][2]/div[@class='form-group'][1]"
    label_from_date = "//form[@class='form-inline form-filter'][2]/div[@class='form-group'][1]/label"
    div_from_date_picker = "//div[@id='fromPicker']"
    input_from_date = "//input[@id='FromDate']"
    span_from_date_calendar_icon = "//div[@id='fromPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    div_form_group_to_date = "//form[@class='form-inline form-filter'][2]/div[@class='form-group'][2]"
    label_to_date = "//form[@class='form-inline form-filter'][2]/div[@class='form-group'][2]/label"
    div_to_date_picker = "//div[@id='toPicker']"
    input_to_date = "//input[@id='ToDate']"
    span_to_date_calendar_icon = "//div[@id='toPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    # Submit button
    button_submit = "//button[@id='btnStatisticsSubmit']"