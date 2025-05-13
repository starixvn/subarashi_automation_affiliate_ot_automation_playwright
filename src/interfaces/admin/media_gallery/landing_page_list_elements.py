class LandingPageListElements:
    # Main action buttons
    btn_delete = "//button[contains(@class, 'btn-outline-danger')]"
    icn_delete = "//button[contains(@class, 'btn-outline-danger')]/span[@class='oi oi-x ml-2']"
    
    btn_add = "//button[contains(@class, 'btn-outline-secondary')]"
    icn_add = "//button[contains(@class, 'btn-outline-secondary')]/span[@class='oi oi-plus ml-2']"
    
    # Selection helpers
    txt_select = "//span[text()='Select:']"
    btn_select_all = "//button[contains(@class, 'btn-link')]/u[text()='All']/.."
    btn_select_none = "//button[contains(@class, 'btn-link')]/u[text()='None']/.."
    
    # Table headers
    tbl_landing_page = "//div[@class='landing-page-content']//table"
    th_landing_page_name = "//th[@title='Landing Page Name (Shown in dropdown)']"
    th_landing_page_code = "//th[@title='Landing Page Code (Contained in links)']"
    th_block_target_country = "//th[@title='Block Target Country']"
    th_edit = "//th[@title='Edit']"
    
    # Row elements (generic selectors for rows)
    chk_row = "//td[@class='text-center']/input[@type='checkbox']"
    td_row_number = "//td[@class='text-center' and @title]"
    td_landing_page_name = "//td[@class='text-left' and @title]"
    td_landing_page_code = "//td[@class='text-left' and @title]"
    td_block_target_country = "//td[@class='text-left' and @title]"
    btn_edit = "//td[@title='Edit Landing Page']/button"
    icn_edit = "//td[@title='Edit Landing Page']/button/span[@class='oi oi-pencil text-secondary']"
    
    # Pagination elements
    div_pagination = "//div[@class='page-container center-align']"
    inp_page_number = "//input[@class='page-form']"
    btn_first_page = "//a[@class='icon page-first']"
    btn_prev_page = "//a[@class='icon page-prev']"
    btn_next_page = "//a[@class='icon page-next']"
    btn_last_page = "//a[@class='icon page-last']"
    sel_page_size = "//select[@class='pagesize-select']"
    spn_page_info = "//span[@class='page-info']"
    
    # Modal dialog elements (add/edit landing page)
    mdl_landing_page = "//div[@class='modal-content']"
    mdl_title = "//h5[@class='modal-title']"
    btn_close_modal = "//button[@class='close']"
    
    # Form elements in modal
    inp_landing_page_name = "//input[@name='pageName']"
    lbl_landing_page_name = "//label[@for='pageName']"
    div_feedback_name = "//input[@name='pageName']/following-sibling::div[@class='invalid-feedback']"
    
    inp_landing_page_code = "//input[@name='pageCode']"
    lbl_landing_page_code = "//label[@for='pageCode']"
    div_feedback_code = "//input[@name='pageCode']/following-sibling::div[@class='invalid-feedback']"
    
    # Block target country checkboxes
    lbl_block_target_country = "//div[@class='modal-body']//label[text()='Block Target Country']"
    div_target_countries = "//div[@class='block-target-country']"
    
    chk_my = "//input[@id='MY']"
    lbl_my = "//label[@for='MY']"
    
    chk_bd = "//input[@id='BD']"
    lbl_bd = "//label[@for='BD']"
    
    chk_in = "//input[@id='IN']"
    lbl_in = "//label[@for='IN']"
    
    chk_id = "//input[@id='ID']"
    lbl_id = "//label[@for='ID']"
    
    chk_jp = "//input[@id='JP']"
    lbl_jp = "//label[@for='JP']"
    
    chk_kr = "//input[@id='KR']"
    lbl_kr = "//label[@for='KR']"
    
    chk_th = "//input[@id='TH']"
    lbl_th = "//label[@for='TH']"
    
    chk_vn = "//input[@id='VN']"
    lbl_vn = "//label[@for='VN']"
    
    chk_cn = "//input[@id='CN']"
    lbl_cn = "//label[@for='CN']"
    
    chk_all_countries = "//input[@id='All-Target-Countries']"
    lbl_all_countries = "//label[@for='All-Target-Countries']"
    
    # Form action buttons
    btn_submit = "//div[@class='modal-body']//button[contains(@class, 'btn-success')]"
    btn_cancel = "//div[@class='modal-body']//button[contains(@class, 'btn-info')]" 