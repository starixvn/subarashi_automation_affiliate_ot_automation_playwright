class AccountModalElements:
    # Modal container for Add Existed Account
    mdl_account = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title_add = "//h5[@class='modal-title' and contains(text(), 'Add Existed Account')]"
    mdl_title_edit = "//h5[@class='modal-title']"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Form elements for Add Existed Account
    div_form_container = "//div[@class='account-form-container']"
    frm_account = "//form[contains(@class, 'mb-5')]"
    
    # Username field
    div_username = "//div[@class='mb-2 row form-group']"
    lbl_username = "//label[@for='userName']"
    inp_username = "//input[@name='userName']"
    
    # Department field
    div_department = "//div[@class='row form-group']"
    lbl_department = "//label[@for='department']"
    sel_department = "//select[@name='department']"
    opt_select_dept = "//select[@name='department']/option[@value='0']"
    
    # Action buttons
    btn_add = "//button[contains(@class, 'btn-success') and text()='Add']"
    btn_cancel = "//button[contains(@class, 'btn-info') and text()='Cancel']"
    
    # Form elements for Edit Account (when clicking on username)
    # First Name field
    div_first_name = "//div[@class='mb-2 row form-group'][1]"
    lbl_first_name = "//label[@for='firstName']"
    inp_first_name = "//input[@name='firstName']"
    
    # Last Name field
    div_last_name = "//div[@class='mb-2 row form-group'][2]"
    lbl_last_name = "//label[@for='lastName']"
    inp_last_name = "//input[@name='lastName']"
    
    # Submit button for Edit form
    btn_submit = "//button[contains(@class, 'btn-success') and text()='Submit']"
    
    # Helper method to get option for specific department
    def get_department_option(self, department_name):
        return f"//select[@name='department']/option[text()='{department_name}']"
    
    def get_department_option_by_value(self, value):
        return f"//select[@name='department']/option[@value='{value}']" 