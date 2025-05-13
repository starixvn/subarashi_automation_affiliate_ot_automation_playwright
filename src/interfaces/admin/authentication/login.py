class LoginElements:
    # Root and container elements
    div_root = "//div[@id='root']"
    div_app_container = "//div[@class='app-container']"
    div_login_container = "//div[@class='login-container']"

    # Loader elements
    div_loader = "//div[@class='loader']"
    div_backdrop = "//div[@class='backdrop']"
    div_spinner = "//div[@class='spinner']"
    div_spinner_items = "//div[@class='spinner']/div"

    # Login form container
    div_lgrp = "//div[@class='lgRp']"
    div_login_header = "//div[@class='login-header']"
    txt_welcome = "//div[@class='login-header']//div[1]/div[1]"
    spn_login = "//div[@class='login-header']//span"
    txt_signin = "//div[@class='login-header']//p"
    div_war_box = "//div[@class='war-box']"

    # Form elements
    frm_login = "//form[@class='form-login']"
    div_form_groups = "//form[@class='form-login']/div[@class='form-group']"
    lbl_username = "//label[@for='userName']"
    inp_username = "//input[@id='userName']"
    lbl_password = "//label[@for='passWord']"
    inp_password = "//input[@id='password']"
    div_button_container = "//div[@class='bt']"
    btn_login = "//a[@class='bt-login']"

    # Footer elements
    div_footer = "//div[@class='foot']"
    spn_copyright = "//span[@class='foot-rp']"