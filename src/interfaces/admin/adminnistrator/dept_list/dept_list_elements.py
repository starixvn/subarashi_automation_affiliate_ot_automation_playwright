class DeptListElements:
    # Filter section elements
    lbl_user_name = "//label[text()='User Name']"
    inp_user_name = "//input[@name='userName']"
    
    lbl_first_letter = "//label[text()='First Letter']"
    sel_first_letter = "//select[@name='firstLetter']"
    opt_all = "//select[@name='firstLetter']/option[@value='']"
    
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    icn_search = "//span[@class='oi oi-magnifying-glass']"
    
    # Action buttons
    btn_add_acc = "//button[contains(text(), 'Add Acc')]"
    icn_add_acc = "//button[contains(text(), 'Add Acc')]/span[@class='oi oi-plus']"
    
    btn_add_existed_acc = "//button[contains(text(), 'Add Existed Acc')]"
    icn_add_existed_acc = "//button[contains(text(), 'Add Existed Acc')]/span[@class='oi oi-plus']"
    
    # Table headers
    tbl_admin_list = "//div[@class='common-list-content']//table"
    th_number = "//th[@title='#']"
    th_user_name = "//th[@title='User Name']"
    th_first_name = "//th[@title='First Name']"
    th_last_name = "//th[@title='Last Name']"
    th_status = "//th[@title='Status']"
    th_creator = "//th[@title='Creator']"
    th_created_date = "//th[@title='Created Date']"
    th_policy = "//th[@title='Policy']"
    th_department = "//th[@title='Department']"
    th_password = "//th[@title='Password']"
    
    # Table row elements (generic)
    td_row_number = "//td[@class='text-center' and @title]"
    btn_user_name = "//td[@class='text-center' and @title]/button[@class='btn btn-link p-0']"
    td_first_name = "//td[@class='text-center' and @title]"
    td_last_name = "//td[@class='text-center' and @title]"
    
    td_status = "//td[@class='text-center' and @title='Change Status']"
    chk_status = "//td[@class='text-center' and @title='Change Status']/input[@type='checkbox']"
    
    td_creator = "//td[@class='text-center' and @title]"
    td_created_date = "//td[@class='text-center' and @title]"
    
    btn_account_policy = "//td[@title='Edit Account Policy']/button"
    
    btn_department = "//td[@title='Edit Department']/button"
    
    btn_change_password = "//td[@title='Change Password']/button"
    icn_change_password = "//td[@title='Change Password']/button/span[@class='oi oi-pencil']"
    
    # Helper methods for dynamic selectors
    def get_user_by_name(self, username):
        return f"//td[@class='text-center' and @title='{username}']/button"
    
    def get_department_by_name(self, dept_name):
        return f"//td[@title='Edit Department']/button[text()='{dept_name}']"
    
    def get_row_by_number(self, row_number):
        return f"//td[@class='text-center' and @title='{row_number}']/.." 