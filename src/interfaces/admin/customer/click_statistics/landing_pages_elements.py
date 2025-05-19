class LandingPagesElements:
    # Filter section
    div_filter_container = "//div[@class='filter-container py-0']"
    div_form_inline = "//div[@class='filter-container py-0']/div[@class='form-inline']"
    
    # Page dropdown
    div_page = "//div[@class='mr-sm-2 my-2 form-group'][1]"
    lbl_page = "//label[@for='selectedPage']"
    sel_page = "//select[@id='selectedPage']"
    opt_all_pages = "//select[@id='selectedPage']/option[@value='']"
    
    # Helper method for page options
    def get_page_option(self, value):
        return f"//select[@id='selectedPage']/option[@value='{value}']"
    
    # Language dropdown
    div_language = "//div[@class='mr-sm-2 my-2 form-group'][2]"
    lbl_language = "//label[@for='languageCode']"
    sel_language = "//select[@id='languageCode']"
    opt_all_languages = "//select[@id='languageCode']/option[@value='']"
    
    # Helper method for language options
    def get_language_option(self, value):
        return f"//select[@id='languageCode']/option[@value='{value}']"
    
    # From date field
    div_from_date = "//div[@class='mr-sm-2 my-2 form-group'][3]"
    lbl_from_date = "//div[@class='mr-sm-2 my-2 form-group'][3]/label"
    div_from_daterange = "//div[@class='mr-sm-2 my-2 form-group'][3]//div[@class='daterange-container']"
    inp_from_date = "//div[@class='mr-sm-2 my-2 form-group'][3]//input[@class='input-text datepicker']"
    spn_from_calendar = "//div[@class='mr-sm-2 my-2 form-group'][3]//span[@class='oi oi-calendar']"
    
    # To date field
    div_to_date = "//div[@class='mr-sm-2 my-2 form-group'][4]"
    lbl_to_date = "//div[@class='mr-sm-2 my-2 form-group'][4]/label"
    div_to_daterange = "//div[@class='mr-sm-2 my-2 form-group'][4]//div[@class='daterange-container']"
    inp_to_date = "//div[@class='mr-sm-2 my-2 form-group'][4]//input[@class='input-text datepicker']"
    spn_to_calendar = "//div[@class='mr-sm-2 my-2 form-group'][4]//span[@class='oi oi-calendar']"
    
    # Device dropdown
    div_device = "//div[@class='mr-sm-2 my-2 form-group'][5]"
    lbl_device = "//label[@for='deviceType']"
    sel_device = "//select[@id='deviceType']"
    opt_all_devices = "//select[@id='deviceType']/option[@value='-1']"
    opt_pc_laptop = "//select[@id='deviceType']/option[@value='0']"
    opt_mobile = "//select[@id='deviceType']/option[@value='1']"
    
    # Search button
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    spn_search_icon = "//button[contains(@class, 'btn-outline-primary')]/span[@class='oi oi-magnifying-glass']"
    
    # First table - Pages and Languages
    div_table_first = "//div[@class='table-responsive table-striped my-2'][1]"
    tbl_pages = "//div[@class='table-responsive table-striped my-2'][1]//div[@class='body-content']"
    
    # First table headers
    th_page = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='Page']"
    th_language = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='Language']"
    th_total_click = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='Total Click']"
    th_unique_click = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='Unique Click']"
    th_signups = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='Signups']"
    th_fdm = "//div[@class='table-responsive table-striped my-2'][1]//th[@title='FDM']"
    
    # Second table - Website URL
    div_table_second = "//div[@class='table-responsive table-striped my-2'][2]"
    tbl_website_url = "//div[@class='table-responsive table-striped my-2'][2]//div[@class='body-content']"
    
    # Second table headers
    th_website_url = "//div[@class='table-responsive table-striped my-2'][2]//th[@title='Website URL']"
    th_total_clicks = "//div[@class='table-responsive table-striped my-2'][2]//th[@title='Total Clicks']"
    th_unique_clicks = "//div[@class='table-responsive table-striped my-2'][2]//th[@title='Unique Clicks']"
    th_sign_up = "//div[@class='table-responsive table-striped my-2'][2]//th[@title='Sign up']"
    th_fdm_second = "//div[@class='table-responsive table-striped my-2'][2]//th[@title='FDM']"
    
    # Pagination section
    div_pagination = "//div[@class='page-container center-align']"
    a_page_first = "//div[@class='page-container center-align']/a[@class='icon page-first']"
    a_page_prev = "//div[@class='page-container center-align']/a[@class='icon page-prev']"
    div_page_input = "//div[@class='page-container center-align']/div[@class='page-input']"
    inp_page_number = "//div[@class='page-container center-align']//input[@class='page-form']"
    a_page_next = "//div[@class='page-container center-align']/a[@class='icon page-next']"
    a_page_last = "//div[@class='page-container center-align']/a[@class='icon page-last']"
    sel_page_size = "//div[@class='page-container center-align']/select[@class='pagesize-select']"
    spn_page_info = "//div[@class='page-container center-align']/span[@class='page-info']"
    
    # Helper methods for dynamic table rows
    def get_page_row_by_name(self, page_name):
        return f"//div[@class='table-responsive table-striped my-2'][1]//td[@title='{page_name}']/parent::tr"
    
    def get_page_button(self, page_name):
        return f"//div[@class='table-responsive table-striped my-2'][1]//td[@title='{page_name}']/button"
    
    def get_website_url_row(self, url):
        return f"//div[@class='table-responsive table-striped my-2'][2]//td[@title='{url}']/parent::tr" 