class EditElements:
    
    # Personal Information section
    # ------------ Labels ------------
    lbl_username = "//label[@for='username']"
    lbl_first_name = "//label[@for='firstName']"
    lbl_last_name = "//label[@for='lastName']"
    lbl_gender = "//label[contains(@class, 'col-form-label') and text()='Gender']"
    lbl_email = "//label[@for='email']"
    lbl_contact_number = "//label[@for='phone']"
    lbl_msn_ym_qq = "//label[@for='MSN/YM/QQ']"
    
    # ------------ Input fields ------------
    txt_username = "//p[contains(@class, 'form-control-plaintext')]"
    inp_first_name = "//input[@id='firstName']"
    inp_last_name = "//input[@id='lastName']"
    rdo_male = "//div[@class='d-inline-block mr-3 form-check']/label/input"
    rdo_female = "//div[@class='d-inline-block form-check']/label/input"
    inp_email = "//input[@id='email']"
    inp_contact_number = "//input[@id='phone']"
    inp_msn_ym_qq = "//input[@id='MSN/YM/QQ']"
    
    # Additional Information section
    # ------------ Labels ------------
    lbl_address = "//label[@for='address']"
    lbl_city = "//label[@for='city']"
    lbl_state = "//label[@for='state']"
    lbl_postcode = "//label[@for='postcode']"
    lbl_country = "//label[@for='country']"
    lbl_security_question = "//label[@for='question']"
    lbl_security_answer = "//label[@for='answer']"
    
    # ------------ Input fields ------------
    inp_address = "//input[@id='address']"
    inp_city = "//input[@id='city']"
    inp_state = "//input[@id='state']"
    inp_postcode = "//input[@id='postcode']"
    sel_country = "//select[@id='country']"
    txt_security_question = "//label[@for='question']/following-sibling::div/p"
    txt_security_answer = "//label[@for='answer']/following-sibling::div/p"
    
    # Email Format Preference section
    rdo_plain_text = "//div[contains(@class, 'form-check')]//input[@type='radio' and @checked]"
    rdo_html_format = "//div[contains(@class, 'form-check')]//input[@type='radio' and not(@checked)]"
    
    # Website Information section
    rdo_have_website = "//input[@type='radio' and following-sibling::text()[contains(., 'I have my own website')]]"
    rdo_no_website = "//input[@type='radio' and following-sibling::text()[contains(., 'I don')]]"
    lbl_website_url = "//label[@for='siteUrl']"
    inp_website_url = "//input[@name='siteUrl']"
    btn_add_url = "//button[text()='Add Url']"
    
    lbl_no_site_description = "//label[@for='noSiteDescription']"
    txt_no_site_description = "//textarea[@id='noSiteDescription']"
    
    # Payment Information section
    lbl_preferred_payment = "//label[@for='preferredPayment']"
    lbl_player_username = "//label[@for='playerUsername']"
    sel_preferred_payment = "//select[@id='preferredPayment']"
    inp_player_username = "//input[@id='playerUsername']"
    txt_minimum_payment = "//span[contains(@class, 'input-item') and contains(text(), 'Minimum payment')]"
    
    # Submit button
    btn_submit = "//button[contains(@class, 'btn-success') and text()='Submit']"
    
    # Utility methods for dynamic options
    @staticmethod
    def get_country_option(country_value):
        """Returns XPath selector for a specific country option"""
        return f"//select[@id='country']/option[@value='{country_value}']" 