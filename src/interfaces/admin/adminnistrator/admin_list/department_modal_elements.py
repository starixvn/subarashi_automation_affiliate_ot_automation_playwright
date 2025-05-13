class DepartmentModalElements:
    # Modal container
    mdl_department = "//div[@class='modal-content']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Form elements
    frm_department = "//form[contains(@class, 'mb-5')]"
    
    # Department Name field
    div_department_name = "//div[@class='mb-2 row form-group']"
    lbl_department_name = "//label[@for='departmentName']"
    inp_department_name = "//input[@name='departmentName']"
    
    # Description field
    div_description = "//div[@class='row form-group']"
    lbl_description = "//label[@for='description']"
    inp_description = "//input[@name='description']"
    
    # Action buttons
    btn_submit = "//button[contains(@class, 'btn-success')]"
    btn_cancel = "//button[contains(@class, 'btn-info')]"
    
    # Department detail modal (when clicking on Department name)
    mdl_department_detail = "//div[@class='modal-dialog modal-xl']"
    mdl_department_name = "//h5[@class='modal-title' and contains(text(), 'Department')]"
    
    # Filter elements in department detail
    lbl_keyword = "//label[text()='Keyword']"
    inp_keyword = "//input[@name='userName' and @placeholder='Keyword']"
    
    lbl_first_letter = "//label[text()='First Letter']"
    sel_first_letter = "//select[@name='firstLetter']"
    opt_all = "//select[@name='firstLetter']/option[@value='']"
    
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    icn_search = "//button[contains(@class, 'btn-outline-primary')]/span[@class='oi oi-magnifying-glass']"
    
    btn_update = "//button[contains(@class, 'btn-outline-secondary') and text()='Update']"
    
    # Selection helpers
    txt_select = "//span[text()='Select:']"
    btn_select_all = "//button[contains(@class, 'btn-link')]/u[text()='All']/.."
    btn_select_none = "//button[contains(@class, 'btn-link')]/u[text()='None']/.."
    
    # Account list table in department detail
    tbl_account_list = "//div[@class='common-list-content']//table"
    
    # Table headers
    th_checkbox = "//th[1]"
    th_number = "//th[@title='#']"
    th_user_name = "//th[@title='User Name']"
    th_first_name = "//th[@title='First Name']"
    th_last_name = "//th[@title='Last Name']"
    th_status = "//th[@title='Status']"
    th_creator = "//th[@title='Creator']"
    th_created_date = "//th[@title='Created Date']"
    th_policy = "//th[@title='Policy']"
    th_password = "//th[@title='Password']"
    
    # Account row elements
    chk_account = "//td[@class='text-center']/input[@type='checkbox']"
    td_row_number = "//td[@class='text-center' and @title]"
    btn_user_name = "//td[@class='text-center' and @title]/button"
    td_first_name = "//td[@class='text-center' and @title]"
    td_last_name = "//td[@class='text-center' and @title]"
    td_status = "//td[@class='text-center' and @title='Change Status']"
    td_creator = "//td[@class='text-center' and @title]"
    td_created_date = "//td[@class='text-center' and @title]"
    btn_role_policy = "//td[@title='Edit Account Policy']/button"
    btn_change_password = "//td[@title='Change Password']/button"
    icn_change_password = "//td[@title='Change Password']/button/span[@class='oi oi-pencil']" 