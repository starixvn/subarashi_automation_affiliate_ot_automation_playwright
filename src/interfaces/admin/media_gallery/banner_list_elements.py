class BannerListElements:
    # Filter container elements
    sel_user_type = "//select[@id='userType']"
    lbl_user_type = "//label[@for='userType']"
    
    sel_category = "//select[@id='category']"
    lbl_category = "//label[@for='category']"
    
    sel_language = "//select[@id='language']"
    lbl_language = "//label[@for='language']"
    
    sel_currency = "//select[@id='currency']"
    lbl_currency = "//label[@for='currency']"
    
    sel_aff_type = "//select[@id='affType']"
    lbl_aff_type = "//label[@for='affType']"
    
    sel_device_type = "//select[@id='deviceType']"
    lbl_device_type = "//label[@for='deviceType']"
    
    sel_size = "//select[@id='size']"
    lbl_size = "//label[@for='size']"
    
    btn_search = "//button[.//span[@class='oi oi-magnifying-glass']]"
    icn_search = "//span[@class='oi oi-magnifying-glass']"
    
    # Add button
    btn_add = "//button[contains(text(), 'Add')]"
    icn_add = "//button[contains(text(), 'Add')]//span[@class='oi oi-plus ml-2']"
    
    # Table elements
    tbl_banner_list = "//div[@class='banner-list-content']//table"
    th_user_type = "//th[@title='User Type']"
    th_images = "//th[@title='Images']"
    th_file_name = "//th[@title='File Name']"
    th_category_col = "//th[@title='Category']"
    th_sub_category = "//th[@title='Sub Category']"
    th_language_col = "//th[@title='Language']"
    th_currency_col = "//th[@title='Currency']"
    th_device = "//th[@title='Device']"
    th_size_col = "//th[@title='Size']"
    th_edit = "//th[@title='Edit']"
    
    # No data row
    td_no_data = "//td[contains(text(), 'There is no information available')]"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    inp_page_number = "//input[@class='page-form']"
    btn_first_page = "//a[@class='icon page-first']"
    btn_prev_page = "//a[@class='icon page-prev']"
    btn_next_page = "//a[@class='icon page-next']"
    btn_last_page = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    spn_page_info = "//span[@class='page-info']"
    
    # Modal dialog elements when adding a banner
    mdl_add_banner = "//div[@class='modal-dialog']"
    mdl_title = "//h5[@class='modal-title']"
    btn_close_modal = "//button[@class='close']"
    
    # Banner form elements
    frm_banner = "//form[contains(@class, 'mb-2')]"
    lbl_valid_types = "//label[contains(text(), 'Valid Types')]"
    lbl_file_size = "//label[contains(text(), 'File Size Limit')]"
    lbl_max_files = "//label[contains(text(), 'Maximum files')]"
    
    lbl_file = "//label[@for='file']"
    btn_choose_file = "//button[contains(text(), 'Choose File')]"
    spn_file_chosen = "//span[contains(text(), 'No file choosen')]"
    inp_file = "//input[@name='file']"
    
    sel_user_type_modal = "//div[@class='modal-body']//select[@id='userType']"
    lbl_user_type_modal = "//div[@class='modal-body']//label[@for='userType']"
    
    div_category_select = "//div[@id='multiple-select-6']"
    btn_category_select = "//div[@id='multiple-select-6']//button"
    txt_category_display = "//div[@id='multiple-select-6']//span[@class='text-display']"
    chk_category_all = "//input[@id='multiple-select-6-optionItemAll']"
    
    div_sub_category_select = "//div[@id='multiple-select-7']"
    btn_sub_category_select = "//div[@id='multiple-select-7']//button"
    txt_sub_category_display = "//div[@id='multiple-select-7']//span[@class='text-display']"
    chk_sub_category_all = "//input[@id='multiple-select-7-optionItemAll']"
    
    sel_language_modal = "//div[@class='modal-body']//select[@id='language']"
    
    div_currency_select = "//div[@id='multiple-select-8']"
    btn_currency_select = "//div[@id='multiple-select-8']//button"
    txt_currency_display = "//div[@id='multiple-select-8']//span[@class='text-display']"
    chk_currency_all = "//input[@id='multiple-select-8-optionItemAll']"
    
    div_aff_type_select = "//div[@id='multiple-select-9']"
    btn_aff_type_select = "//div[@id='multiple-select-9']//button"
    txt_aff_type_display = "//div[@id='multiple-select-9']//span[@class='text-display']"
    chk_aff_type_all = "//input[@id='multiple-select-9-optionItemAll']"
    
    div_device_type_select = "//div[@id='multiple-select-10']"
    btn_device_type_select = "//div[@id='multiple-select-10']//button"
    txt_device_type_display = "//div[@id='multiple-select-10']//span[@class='text-display']"
    chk_device_type_all = "//input[@id='multiple-select-10-optionItemAll']"
    
    inp_file_name = "//input[@id='inputFileName0']"
    lbl_file_name = "//label[@for='inputFileName0']"
    btn_remove = "//button[contains(text(), 'Remove')]"
    
    btn_upload = "//button[contains(text(), 'Upload')]"
    btn_cancel = "//div[@class='modal-body']//button[contains(text(), 'Cancel')]" 