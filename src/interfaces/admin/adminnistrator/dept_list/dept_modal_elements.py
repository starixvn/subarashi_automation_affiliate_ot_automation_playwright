class DeptModalElements:
    # Modal container elements
    mdl_dept = "//div[@class='modal-dialog']"
    mdl_content = "//div[@class='modal-content']"
    mdl_header = "//div[@class='modal-header']"
    mdl_title = "//h5[@class='modal-title' and contains(text(), 'Add Department')]"
    icn_popup = "//span[@class='iconpopup']"
    btn_close = "//button[@class='close']"
    icn_close = "//button[@class='close']/span[@aria-hidden='true']"
    
    # Form container
    mdl_body = "//div[@class='modal-body']"
    div_body_wrapper = "//div[@class='modal-body-wrapper']"
    div_dept_form = "//div[@class='department-form-container']"
    frm_dept = "//form[contains(@class, 'mb-5')]"
    
    # Department name field
    div_dept_name = "//div[@class='mb-2 row form-group']"
    lbl_dept_name = "//label[@for='departmentName']"
    inp_dept_name = "//input[@name='departmentName']"
    
    # Description field
    div_description = "//div[@class='row form-group']"
    lbl_description = "//label[@for='description']"
    inp_description = "//input[@name='description']"
    
    # Action buttons
    btn_submit = "//button[contains(@class, 'btn-success') and text()='Submit']"
    btn_cancel = "//button[contains(@class, 'btn-info') and text()='Cancel']" 