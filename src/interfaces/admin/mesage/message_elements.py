class MessageElements:
    # Main page elements - Filter section
    lbl_search_by = "//label[text()='Search By']"
    sel_search_by = "//select[@name='searchBy']"
    opt_all = "//select[@name='searchBy']/option[@value='0']"
    opt_normal = "//select[@name='searchBy']/option[@value='1']"
    opt_important = "//select[@name='searchBy']/option[@value='2']"
    
    lbl_all_date = "//label[contains(@class, 'form-check-label') and contains(text(), 'All Date')]"
    chk_all_date = "//input[@name='isGetAll']"
    
    lbl_from = "//label[text()='From']"
    inp_from_date = "//label[text()='From']/following-sibling::div//input[@class='input-text datepicker']"
    icn_from_calendar = "//label[text()='From']/following-sibling::div//span[@class='oi oi-calendar']"
    
    lbl_to = "//label[text()='To']"
    inp_to_date = "//label[text()='To']/following-sibling::div//input[@class='input-text datepicker']"
    icn_to_calendar = "//label[text()='To']/following-sibling::div//span[@class='oi oi-calendar']"
    
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    icn_search = "//button[contains(@class, 'btn-outline-primary')]/span[@class='oi oi-magnifying-glass']"
    
    # Calendar elements (date picker)
    sel_month = "//select[contains(@class, 'rdr-MonthAndYearSelect')][1]"
    sel_year = "//select[contains(@class, 'rdr-MonthAndYearSelect')][2]"
    btn_prev_month = "//button[contains(@class, 'rdr-MonthAndYear-button prev')]"
    btn_next_month = "//button[contains(@class, 'rdr-MonthAndYear-button next')]"
    
    # Action buttons
    btn_delete = "//button[contains(@class, 'btn-outline-danger')]"
    icn_delete = "//button[contains(@class, 'btn-outline-danger')]/span[@class='oi oi-x']"
    
    btn_add = "//button[contains(text(), 'Add') and contains(@class, 'btn-outline-secondary')]"
    icn_add = "//button[contains(text(), 'Add')]/span[@class='oi oi-plus']"
    
    btn_current_message = "//button[text()='Current Message']"
    
    # Selection helpers
    txt_select = "//span[text()='Select:']"
    btn_select_all = "//button[contains(@class, 'btn-link')]/u[text()='All']/.."
    btn_select_none = "//button[contains(@class, 'btn-link')]/u[text()='None']/.."
    
    # Table headers
    tbl_message = "//div[@class='message-content']//table"
    th_checkbox = "//thead//th[1]"
    th_number = "//th[@title='#']"
    th_creator = "//th[@title='Creator']"
    th_posted_date = "//th[@title='Posted Date']"
    th_message = "//th[@title='Message']"
    th_important = "//th[@title='Important']"
    th_updated_by = "//th[@title='Updated By']"
    th_updated_date = "//th[@title='Updated Date']"
    
    # Table rows and cells (generic)
    chk_row = "//td[@class='text-center']/input[@type='checkbox']"
    td_row_number = "//td[@class='text-center' and @title]"
    td_creator = "//td[@class='text-center' and @title]"
    td_posted_date = "//td[@class='text-center' and @title]"
    btn_view_message = "//td[@title='View Detail']/button"
    td_important = "//td[@class='text-center' and @title]"
    td_updated_by = "//td[@class='text-center' and @title]"
    td_updated_date = "//td[@class='text-center' and @title]"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    btn_first_page = "//a[@class='icon page-first']"
    btn_prev_page = "//a[@class='icon page-prev']"
    inp_page_number = "//input[@class='page-form']"
    txt_total_pages = "//div[@class='page-input']/span[contains(text(), 'of')]"
    btn_next_page = "//a[@class='icon page-next']"
    btn_last_page = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    txt_page_info = "//span[@class='page-info']"
    
    # Modal dialog elements - Add New Message
    mdl_add_message = "//div[@class='modal-dialog modal-lg']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close_modal = "//button[@class='close']"
    
    # Form elements
    frm_message = "//form[contains(@class, 'mb-2')]"
    
    lbl_important = "//label[@for='important']"
    chk_important = "//input[@name='important']"
    
    lbl_english = "//label[@for='Message_en']"
    txt_english = "//textarea[@id='Message_en']"
    
    lbl_indonesian = "//label[@for='Message_id']"
    txt_indonesian = "//textarea[@id='Message_id']"
    
    lbl_korean = "//label[@for='Message_ko']"
    txt_korean = "//textarea[@id='Message_ko']"
    
    lbl_thai = "//label[@for='Message_th']"
    txt_thai = "//textarea[@id='Message_th']"
    
    lbl_vietnamese = "//label[@for='Message_vn']"
    txt_vietnamese = "//textarea[@id='Message_vn']"
    
    lbl_chinese = "//label[@for='Message_cs']"
    txt_chinese = "//textarea[@id='Message_cs']"
    
    # Modal action buttons
    btn_add_modal = "//div[@class='modal-body']//button[contains(@class, 'btn-success')]"
    btn_cancel_modal = "//div[@class='modal-body']//button[contains(@class, 'btn-info')]" 