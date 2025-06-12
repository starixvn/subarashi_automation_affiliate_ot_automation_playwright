class HeaderElements:

    # Header top container
    div_header_top = "//div[@class='header-top']"
    div_page_container = "//div[@class='header-top']/div[@class='page-container']"
    div_logo_lang = "//div[@class='header-top']/div[@class='page-container']/div[@class='logo-lang']"
    
    # Logo section
    div_logo = "//div[@class='header-top']//div[@class='logo']"
    a_logo_link = "//div[@class='header-top']//div[@class='logo']/a"
    img_logo = "//div[@class='header-top']//div[@class='logo']/a/img"
    
    # Login section
    div_login = "//div[@class='header-top']//div[@class='login']"
    div_user_signup = "//div[@class='header-top']//div[@class='login']/div[@class='user-signup']"
    div_group_auth_login = "//div[@class='group-auth-login']"
    div_user_login = "//div[@id='userLogin']"
    input_verification_token = "//input[@name='__RequestVerificationToken']"
    input_public_key = "//input[@id='PublicKey']"
    a_btn_login = "//a[@class='btn-auth btn-login'][@id='mobileLogin']"
    a_btn_signup = "//a[@class='btn-auth btn-signup']"
    a_btn_logout = "//div[@class='group-auth-login']/a[contains(text(), 'Logout')]"
    a_my_account = "//div[@class='group-auth-login']/a[contains(text(), 'My Account')]"
    
    # Language selection
    div_language_container = "//div[@class='language-container']"
    div_language_selection = "//div[@class='language-selection']"
    btn_select_language = "//button[@class='select-language'][@id='selectedLanguage']"
    span_flag = "//button[@class='select-language']/span/i[@class='flag']"
    span_lang_name = "//button[@class='select-language']/span/span[@class='name-lang']"
    i_caret = "//button[@class='select-language']/i[@class='caret']"
    div_language_list_wrapper = "//div[@class='language-list-wrapper'][@id='languageList']"
    ul_language_list = "//ul[@class='list-unstyled language-list']"