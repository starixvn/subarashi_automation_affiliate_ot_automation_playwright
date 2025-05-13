class AdminListElements:
    # Add Department button
    btn_add_dept = "//button[contains(@class, 'btn-outline-secondary') and contains(text(), 'Add Dept')]"
    icn_add_dept = "//button[contains(@class, 'btn-outline-secondary')]//span[@class='oi oi-plus']"
    
    # Department list table elements
    tbl_department_list = "//div[@class='department-list-content']//table"
    
    # Table headers
    th_number = "//th[@title='#']"
    th_department = "//th[@title='Department']"
    th_no_of_user = "//th[@title='No of User']"
    th_description = "//th[@title='Description']"
    th_role_policy = "//th[@title='Role Policy']"
    th_edit = "//th[@title='Edit']"
    th_delete = "//th[@title='Delete']"
    
    # Table row elements (generic patterns for rows)
    td_row_number = "//td[@class='text-center' and @title]"
    td_department_name = "//td[@class='text-center' and @title]"
    btn_no_of_user = "//td[@class='text-center']/button[@class='btn btn-link p-0']"
    td_description = "//td[@class='text-center' and @title]"
    btn_role_policy = "//td[@title='Edit Role Policy']/button"
    btn_edit_department = "//td[@title='Edit Department']/button"
    icn_edit_department = "//td[@title='Edit Department']/button/span[@class='oi oi-pencil']"
    btn_delete_department = "//td[@title='Delete Department']/button"
    icn_delete_department = "//td[@title='Delete Department']/button/span[@class='oi oi-x']"
    
    # Specific row selection using row index or content (example)
    def get_department_row_by_name(self, department_name):
        return f"//td[@class='text-center' and @title='{department_name}']/.."
    
    def get_role_policy_button_by_row(self, row_index):
        return f"(//td[@class='text-center' and @title='Edit Role Policy']/button)[{row_index}]"
    
    def get_edit_button_by_row(self, row_index):
        return f"(//td[@class='text-center' and @title='Edit Department']/button)[{row_index}]" 