class SubMenuElements:
    # Container elements
    div_sub_menu = "//div[@class='sub-menu-container']"
    div_image = "//div[@class='d-inline-block'][1]"
    img_domain = "//img[@src='Areas/Portal/www/dist/imgs/i_domain.jpg']"
    div_nav = "//div[@class='d-inline-block'][2]"
    
    # Navigation elements
    ul_nav = "//ul[@class='nav']"
    
    # Menu items
    li_affiliate_domain = "//li[@class='nav-item'][1]"
    lnk_affiliate_domain = "//a[@class='nav-link' and contains(@href, '/Portal/Domain')]"
    lnk_affiliate_domain_active = "//a[@class='nav-link active' and contains(@href, '/Portal/Domain')]"
    
    li_12bet_domains = "//li[@class='nav-item'][2]"
    lnk_12bet_domains = "//a[@class='nav-link' and contains(@href, '/Portal/MemberDomain')]"
    lnk_12bet_domains_active = "//a[@class='nav-link active' and contains(@href, '/Portal/MemberDomain')]"
    
    li_domain_control = "//li[@class='nav-item'][3]"
    lnk_domain_control = "//a[@class='nav-link' and contains(@href, '/Portal/DomainControl')]"
    lnk_domain_control_active = "//a[@class='nav-link active' and contains(@href, '/Portal/DomainControl')]"
    
    li_sub_aff_domain = "//li[@class='nav-item'][4]"
    lnk_sub_aff_domain = "//a[@class='nav-link' and contains(@href, '/Portal/SubAffDomain')]"
    lnk_sub_aff_domain_active = "//a[@class='nav-link active' and contains(@href, '/Portal/SubAffDomain')]"
    
    li_specific_domain_control = "//li[@class='nav-item'][5]"
    lnk_specific_domain_control = "//a[@class='nav-link' and contains(@href, '/Portal/SpecificDomainControl')]"
    lnk_specific_domain_control_active = "//a[@class='nav-link active' and contains(@href, '/Portal/SpecificDomainControl')]"
    
    # Helper methods for finding links by text
    def get_nav_link_by_text(self, text):
        return f"//a[contains(@class, 'nav-link') and text()='{text}']"
    
    def is_link_active(self, link_text):
        return f"//a[contains(@class, 'active') and text()='{link_text}']" 