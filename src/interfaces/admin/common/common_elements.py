class CommonElements:
    # Multiple option select
    div_multiple_option_filter = "//div[@class='my-sm-1 mr-sm-2 multiple-currency-filter form-group']"
    lbl_linked_currency = "//div[@class='my-sm-1 mr-sm-2 multiple-currency-filter form-group']/label[@class='mr-sm-2']"
    div_multiple_select_container = "//div[@id='multiple-select-1']"
    btn_multiple_select = "//div[@id='multiple-select-1']/button[@class='multiple-select-default multiple-select-label']"
    chk_multiple_select_all = "//input[@id='multiple-select-1-optionItemAll']"
    ul_multiple_select_options = "//div[@id='multiple-select-1']//ul[@class='multiple-select-options']"
    
    # Dynamic method for checkbox option by index
    @staticmethod
    def chk_multiple_select_option_by_index(index):
        return f"//div[@id='multiple-select-1']//input[@id='multiple-select-1-optionItem-{index}']"
    
    # Single option select (dropdown)
    div_single_option_filter = "//div[@class='my-sm-1 mr-sm-2 form-group']/label[text()='Base Currency']/.."
    lbl_base_currency = "//div[@class='my-sm-1 mr-sm-2 form-group']/label[@class='mr-sm-2']"
    sel_base_currency = "//select[@id='BaseCurrency']"
    
    # Dynamic method for option by value
    @staticmethod
    def opt_dropdown_option_by_value(value):
        return f"//select[@id='BaseCurrency']/option[@value='{value}']"
    
    # Date picker (From)
    div_date_picker_filter = "//div[@class='mr-sm-3 my-2 form-group']"
    lbl_date_from = "//div[@class='mr-sm-3 my-2 form-group']/label[@class='mr-sm-2']"
    div_daterange_container = "//div[@class='daterange-container']"
    div_daterange_label = "//div[@class='daterange-container']/div[@class='daterange-label']"
    inp_datepicker = "//div[@class='daterange-label']/input[@class='input-text datepicker']"
    div_date_overlay = "//div[@class='daterange-container']/div[@class='overlay']"
    div_date_range = "//div[@class='overlay']/div[@class='rdr-DateRange']"
    
    # Month and year selectors
    div_month_year = "//div[@class='rdr-MonthAndYear']"
    sel_month = "//span[@class='rdr-MonthAndYear-month']/select"
    sel_year = "//span[@class='rdr-MonthAndYear-year']/select"
    btn_prev_month = "//button[@class='rdr-MonthAndYear-button prev']"
    btn_next_month = "//button[@class='rdr-MonthAndYear-button next']"
    
    # Days grid
    div_weekdays = "//div[@class='rdr-WeekDays']"
    div_days = "//div[@class='rdr-Days']"
    
    # Dynamic method for day by number
    @staticmethod
    def day_selector_by_number(day_number):
        return f"//div[@class='rdr-Days']//span[@class='rdr-Day' and text()='{day_number}']"
    
    # Month picker 1 (table header)
    th_month_picker = "//th[@class='width-30 month-picker']"
    div_month_picker1 = "//th[@class='width-30 month-picker']/div[@class='position-relative d-inline-block']"
    div_rmp_container1 = "//th[@class='width-30 month-picker']//div[@class='rmp-main-container']"
    div_mp_form_container1 = "//th[@class='width-30 month-picker']//div[@class='mp-form-container']"
    inp_month_picker1 = "//th[@class='width-30 month-picker']//input[@class='mp-form-input']"
    div_mp_container1 = "//th[@class='width-30 month-picker']//div[@class='mp-container']"
    div_mp_header1 = "//th[@class='width-30 month-picker']//div[@class='mp-header']"
    sel_month_picker_year1 = "//th[@class='width-30 month-picker']//select[@class='mp-select-year']"
    
    # Dynamic method for month button in picker 1
    @staticmethod
    def btn_month1_by_name(month_name):
        return f"//th[@class='width-30 month-picker']//button[@class='mp-btn-month' and text()='{month_name}']"
    
    # Month picker 2 (form group)
    div_month_picker2 = "//div[@class='my-sm-1 mr-sm-2 form-group']/label[text()='From']/.."
    div_rmp_container2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//div[@class='rmp-main-container']"
    div_mp_form_container2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//div[@class='mp-form-container']"
    inp_month_picker2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//input[@class='mp-form-input']"
    div_mp_container2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//div[@class='mp-container']"
    div_mp_header2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//div[@class='mp-header']"
    sel_month_picker_year2 = "//div[@class='my-sm-1 mr-sm-2 form-group']//select[@class='mp-select-year']"
    
    # Dynamic method for month button in picker 2
    @staticmethod
    def btn_month2_by_name(month_name):
        return f"//div[@class='my-sm-1 mr-sm-2 form-group']//button[@class='mp-btn-month' and text()='{month_name}']"
    
    # Pagination
    div_pagination = "//div[@class='page-container center-align']"
    div_page_input = "//div[@class='page-container center-align']/div[@class='page-input']"
    inp_page_number = "//div[@class='page-input']/input[@class='page-form']"
    spn_total_pages = "//div[@class='page-input']/span[2]"
    btn_page_first = "//div[@class='page-container center-align']/a[@class='icon page-first']"
    btn_page_prev = "//div[@class='page-container center-align']/a[@class='icon page-prev']"
    btn_page_next = "//div[@class='page-container center-align']/a[@class='icon page-next']"
    btn_page_last = "//div[@class='page-container center-align']/a[@class='icon page-last']"
    sel_page_size = "//div[@class='page-container center-align']/select[@class='pagesize-select']"
    spn_page_info = "//div[@class='page-container center-align']/span[@class='page-info']"
    
    # Dynamic method for page size option
    @staticmethod
    def opt_page_size_by_value(size_value):
        return f"//select[@class='pagesize-select']/option[@value='{size_value}']" 