class DeptDetailElements:
    # Modal container elements
    mdl_dept_detail = "//div[@class='modal-dialog modal-xl']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Container elements
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_dept_container = "//div[@class='department-popup-container']"
    
    # Filter section
    div_filter = "//div[@class='filter-container']"
    frm_filter = "//div[@class='form-inline']"
    
    # Keyword field
    div_keyword = "//div[@class='mr-sm-3 form-group'][1]"
    lbl_keyword = "//label[text()='Keyword']"
    inp_keyword = "//input[@name='userName' and @placeholder='Keyword']"
    
    # First letter field
    div_first_letter = "//div[@class='mr-sm-3 form-group'][2]"
    lbl_first_letter = "//label[text()='First Letter']"
    sel_first_letter = "//select[@name='firstLetter']"
    opt_all = "//select[@name='firstLetter']/option[@value='']"
    
    # Search button
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    icn_search = "//span[@class='oi oi-magnifying-glass']"
    
    # Update button
    btn_update = "//button[contains(@class, 'btn-outline-secondary') and text()='Update']"
    
    # Selection helpers
    txt_select = "//span[text()='Select:']"
    btn_select_all = "//button[contains(@class, 'btn-link')]/u[text()='All']/.."
    btn_select_none = "//button[contains(@class, 'btn-link')]/u[text()='None']/.."
    
    # Table container
    div_data_content = "//div[@class='data-content']"
    div_list_content = "//div[@class='common-list-content']"
    tbl_users = "//div[@class='common-list-content']//table"
    
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
    
    # Row elements
    chk_user = "//td[@class='text-center']/input[@type='checkbox']"
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
    
    # Helper methods for dynamic selectors
    def get_user_by_name(self, username):
        return f"//td[@class='text-center' and @title='{username}']/button"
    
    def get_checkbox_by_row(self, row_index):
        return f"(//td[@class='text-center']/input[@type='checkbox'])[{row_index}]" 