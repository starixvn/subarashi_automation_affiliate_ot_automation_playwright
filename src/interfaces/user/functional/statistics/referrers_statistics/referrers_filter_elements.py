class ReferrersFilterElements:
    
    # Main container
    div_main_panel = "//div[@id='mainPanel']"
    div_sub_content = "//div[@class='sub-content']"
    
    # Page title
    div_page_title = "//div[@class='page-title']"
    span_page_title_text = "//div[@class='page-title']/span[@class='text']"
    
    # Filter form
    form_filter = "//form[@class='form-inline form-filter']"
    
    # Date range filter - From date
    div_form_group_from_date = "//form[@class='form-inline form-filter']/div[@class='form-group'][1]"
    label_from_date = "//form[@class='form-inline form-filter']/div[@class='form-group'][1]/label"
    div_from_date_picker = "//div[@id='fromPicker']"
    input_from_date = "//input[@id='FromDate']"
    span_from_date_calendar_icon = "//div[@id='fromPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    # Date range filter - To date
    div_form_group_to_date = "//form[@class='form-inline form-filter']/div[@class='form-group'][2]"
    label_to_date = "//form[@class='form-inline form-filter']/div[@class='form-group'][2]/label"
    div_to_date_picker = "//div[@id='toPicker']"
    input_to_date = "//input[@id='ToDate']"
    span_to_date_calendar_icon = "//div[@id='toPicker']/span[@class='glyphicon glyphicon-calendar']"
    
    # Device filter
    div_form_group_device = "//form[@class='form-inline form-filter']/div[@class='form-group'][3]"
    label_device = "//form[@class='form-inline form-filter']/div[@class='form-group'][3]/label"
    select_device = "//select[@id='DeviceType']"
    option_device_all = "//select[@id='DeviceType']/option[@value='-1']"
    option_device_pc = "//select[@id='DeviceType']/option[@value='0']"
    option_device_mobile = "//select[@id='DeviceType']/option[@value='1']"
    
    # Submit button
    button_submit = "//button[@id='btnStatisticsSubmit']"