import time

from src.utils.services.utils import utilities
from config.constants.settings import *

from src.actions.common.action_common import Common
from src.interfaces.admin.customer.left_panel_elements import LeftPanelElements as elm_left_panel
from src.interfaces.admin.customer.submenu_elements import SubmenuElements as elm_submenu
from src.interfaces.admin.customer.statistics_elements import StatisticsElements as elm_statistics
from src.interfaces.admin.customer.click_statistics.submenu_elements import SubmenuElements as elm_submenu_click_statistics
from src.interfaces.admin.customer.click_statistics.referrers_elements import ReferrersElements as elm_referrers
from src.interfaces.admin.customer.click_statistics.landing_pages_elements import LandingPagesElements as elm_landing_pages
from src.interfaces.admin.customer.click_statistics.marketing_page_elements import MarketingPageElements as elm_marketing_page
from src.interfaces.admin.customer.statement_history.statement_history_elements import StatementHistoryElements as elm_statement_history
from src.interfaces.admin.customer.adjustment.adjustment_elements import AdjustmentElements as elm_adjustment
from src.interfaces.admin.customer.edit.edit_elements import EditElements as elm_edit_customer

class GetDataCustomer(Common):
    
    def get_data_referrers_in_customer(self,user_name, from_date, to_date, device_type):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.click_statistics)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu_click_statistics.li_referrers)
            super().select_date_picker(elm_referrers.div_from_date, from_date)
            super().select_date_picker(elm_referrers.div_to_date, to_date)
            self.utils.page.select_options(elm_referrers.sel_device, device_type)
            self.utils.page.click(elm_referrers.btn_search)
            self.utils.page.wait_load_page()
            data_table = []
            number_of_rows = self.utils.page.count_element("",f"{elm_referrers.div_table_first}//tbody/tr[not(contains(@class, 'first-row'))]")
            for i in range(1, number_of_rows + 1):
                site_urls = self.utils.page.get_text(f"{elm_referrers.tbl_site_urls}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[1]")
                total_click = self.utils.page.get_text(f"{elm_referrers.tbl_site_urls}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[2]")
                unique_click = self.utils.page.get_text(f"{elm_referrers.tbl_site_urls}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[3]")
                signups = self.utils.page.get_text(f"{elm_referrers.tbl_site_urls}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[4]")
                fdm = self.utils.page.get_text(f"{elm_referrers.tbl_site_urls}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[5]")
                data_table.append([site_urls, total_click, unique_click, signups, fdm])
            return data_table
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_landing_pages_in_customer(self, user_name, page_name="All", language="All", from_date=None, to_date=None, device_type="All"):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.click_statistics)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu_click_statistics.li_landing_pages)
            self.utils.page.select_options(elm_landing_pages.sel_page, page_name)
            self.utils.page.select_options(elm_landing_pages.sel_language, language)
            super().select_date_picker(elm_landing_pages.div_from_date, from_date)
            super().select_date_picker(elm_landing_pages.div_to_date, to_date)
            self.utils.page.select_options(elm_landing_pages.sel_device, device_type)
            self.utils.page.click(elm_landing_pages.btn_search)
            self.utils.page.wait_load_page()
            time.sleep(3)
            
            result = {
                "pages_data": [],
                "website_urls_data": {}
            }
            
            number_of_rows = self.utils.page.count_element("", f"{elm_landing_pages.tbl_pages}//tbody/tr[not(contains(@class, 'first-row'))]")
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_landing_pages.tbl_pages}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                page_name = self.utils.page.get_text(f"{row_selector}//td[1]")
                language = self.utils.page.get_text(f"{row_selector}//td[2]")
                total_click = self.utils.page.get_text(f"{row_selector}//td[3]")
                unique_click = self.utils.page.get_text(f"{row_selector}//td[4]")
                signups = self.utils.page.get_text(f"{row_selector}//td[5]")
                fdm = self.utils.page.get_text(f"{row_selector}//td[6]")
                
                page_data = {
                    "page_name": page_name,
                    "language": language,
                    "total_click": total_click,
                    "unique_click": unique_click,
                    "signups": signups,
                    "fdm": fdm
                }
                result["pages_data"].append(page_data)
                
                if page_name.lower() != "none":
                    try:
                        self.utils.page.click(f"{row_selector}//td[1]")
                        self.utils.page.wait_load_page()
                        time.sleep(1)
                        
                        website_urls = []
                        url_rows = self.utils.page.count_element("", f"{elm_landing_pages.tbl_website_url}//tbody/tr[not(contains(@class, 'first-row'))]")
                        
                        for j in range(1, url_rows + 1):
                            url_row_selector = f"{elm_landing_pages.tbl_website_url}//tbody/tr[not(contains(@class, 'first-row'))][{j}]"
                            website_url = self.utils.page.get_text(f"{url_row_selector}//td[1]")
                            total_clicks = self.utils.page.get_text(f"{url_row_selector}//td[2]")
                            unique_clicks = self.utils.page.get_text(f"{url_row_selector}//td[3]")
                            sign_up = self.utils.page.get_text(f"{url_row_selector}//td[4]")
                            url_fdm = self.utils.page.get_text(f"{url_row_selector}//td[5]")
                            
                            url_data = {
                                "website_url": website_url,
                                "total_clicks": total_clicks,
                                "unique_clicks": unique_clicks,
                                "sign_up": sign_up,
                                "fdm": url_fdm
                            }
                            website_urls.append(url_data)
                        
                        page_key = f"{page_name} - {language}"
                        result["website_urls_data"][page_key] = website_urls
                        
                        self.utils.page.click(f"{row_selector}//td[1]")
                        self.utils.page.wait_load_page()
                        time.sleep(1)
                    except Exception as click_error:
                        self.utils.page.extract_TestCaseFailed(f"Warning: Cannot get detail data for page {page_name}: {str(click_error)}")
                
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_marketing_pages_in_customer(self, user_name, language="All", from_date=None, to_date=None, include_inactive_tracking=False):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.click_statistics)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu_click_statistics.li_marketing_page)

            super().select_date_picker(elm_marketing_page.div_from_date, from_date)
            super().select_date_picker(elm_marketing_page.div_to_date, to_date)

            self.utils.page.select_options(elm_marketing_page.sel_language, language)

            if include_inactive_tracking:
                self.utils.page.click(elm_marketing_page.chk_include_inactive)

            self.utils.page.click(elm_marketing_page.btn_search)
            self.utils.page.wait_load_page()

            data_table = []
            number_of_rows = self.utils.page.count_element("",f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))]")

            for i in range(1, number_of_rows + 1):
                channel_name = self.utils.page.get_text(f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[1]")
                language = self.utils.page.get_text(f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[2]")
                total_click = self.utils.page.get_text(f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[3]")
                signups = self.utils.page.get_text(f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[4]")
                fdm = self.utils.page.get_text(f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]//td[5]")
                data_table.append([channel_name, language, total_click, signups, fdm])
                
            return data_table

        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_statistics_in_customer(self, user_name, month_date):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            super().select_month_picker(elm_statistics.inp_month, month_date)
            self.utils.page.wait_load_page()
            
            new_signups_month = self.utils.page.get_text(elm_statistics.td_new_signups_month)
            new_signups_total = self.utils.page.get_text(elm_statistics.td_new_signups_total)
            total_active_players_month = self.utils.page.get_text(elm_statistics.td_active_players_month)
            total_active_players_total = self.utils.page.get_text(elm_statistics.td_active_players_total)
            total_qualified_players_month = self.utils.page.get_text(elm_statistics.td_qualified_players_month)
            total_qualified_players_total = self.utils.page.get_text(elm_statistics.td_qualified_players_total)
            total_sub_affiliates_month = self.utils.page.get_text(elm_statistics.td_sub_affiliates_month)
            total_sub_affiliates_total = self.utils.page.get_text(elm_statistics.td_sub_affiliates_total)
            total_deposits_FDM_Deposit_month = self.utils.page.get_text(elm_statistics.td_deposits_month)
            total_deposits_FDM_Deposit_total = self.utils.page.get_text(elm_statistics.td_deposits_total)
            fdm_total_deposit_month = self.utils.page.get_text(elm_statistics.td_fdm_deposit_month)
            fdm_total_deposit_total = self.utils.page.get_text(elm_statistics.td_fdm_deposit_total)
            turnover_month = self.utils.page.get_text(elm_statistics.td_turnover_month)
            turnover_total = self.utils.page.get_text(elm_statistics.td_turnover_total)
            ggr_month = self.utils.page.get_text(elm_statistics.td_ggr_month)
            ggr_total = self.utils.page.get_text(elm_statistics.td_ggr_total)
            tracking_pc_month = self.utils.page.get_text(elm_statistics.td_tracking_pc_month)
            tracking_pc_total = self.utils.page.get_text(elm_statistics.td_tracking_pc_total)
            tracking_mobile_month = self.utils.page.get_text(elm_statistics.td_tracking_mobile_month)
            tracking_mobile_total = self.utils.page.get_text(elm_statistics.td_tracking_mobile_total)

            data = {
                "new_signups_month": new_signups_month,
                "new_signups_total": new_signups_total,
                "total_active_players_month": total_active_players_month,
                "total_active_players_total": total_active_players_total,
                "total_qualified_players_month": total_qualified_players_month,
                "total_qualified_players_total": total_qualified_players_total,
                "total_sub_affiliates_month": total_sub_affiliates_month,
                "total_sub_affiliates_total": total_sub_affiliates_total,
                "total_deposits_FDM_Deposit_month": total_deposits_FDM_Deposit_month,
                "total_deposits_FDM_Deposit_total": total_deposits_FDM_Deposit_total,
                "fdm_total_deposit_month": fdm_total_deposit_month,
                "fdm_total_deposit_total": fdm_total_deposit_total,
                "turnover_month": turnover_month,
                "turnover_total": turnover_total,
                "ggr_month": ggr_month,
                "ggr_total": ggr_total,
                "tracking_pc_month": tracking_pc_month,
                "tracking_pc_total": tracking_pc_total,
                "tracking_mobile_month": tracking_mobile_month,
                "tracking_mobile_total": tracking_mobile_total
            }
            
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_info_left_panel_customer(self, user_name):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            
            data = {
                "parent_affiliate": self.utils.page.get_text(elm_left_panel.btn_parent_affiliate),
                "affiliate": self.utils.page.get_text(elm_left_panel.lnk_affiliate),
                "affiliate_code": self.utils.page.get_text(elm_left_panel.div_affiliate_code_value),
                "first_name": self.utils.page.get_text(elm_left_panel.div_first_name_value),
                "last_name": self.utils.page.get_text(elm_left_panel.div_last_name_value),
                "gender": self.utils.page.get_text(elm_left_panel.div_gender_value),
                "contact_number": self.utils.page.get_text(elm_left_panel.div_contact_number_value),
                "msn_ym_qq": self.utils.page.get_text(elm_left_panel.div_msn_ym_qq_value),
                "approved_by": self.utils.page.get_text(elm_left_panel.div_approved_by_value),
                "target_country": self.utils.page.get_text(elm_left_panel.div_target_country_value),
                "language": self.utils.page.get_text(elm_left_panel.btn_language),
                "website_url": self.utils.page.get_text(elm_left_panel.lnk_website_url),
                "last_login": self.utils.page.get_text(elm_left_panel.div_last_login_value),
                "last_login_ip": self.utils.page.get_text(elm_left_panel.lnk_last_login_ip),
                "revenue_group": self.utils.page.get_text(elm_left_panel.btn_revenue_group),
                "balance_brought_forward": self.utils.page.get_text(elm_left_panel.div_balance_value),
                "affiliate_type": self.utils.page.get_text(elm_left_panel.btn_affiliate_type),
                "status": self.utils.page.get_text(elm_left_panel.btn_status),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_statement_history_in_customer(self, user_name, from_date, to_date, get_all=False):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.statement_history)
            self.utils.page.wait_load_page()
            
            super().select_date_picker(elm_statement_history.div_from_group, from_date)
            super().select_date_picker(elm_statement_history.div_to_group, to_date)
            
            if get_all:
                self.utils.page.click(elm_statement_history.chk_get_all)
            
            self.utils.page.click(elm_statement_history.btn_search)
            self.utils.page.wait_load_page()
            
            hierarchical_data = []
            flat_data = []
            
            current_parent_id = None
            current_parent_data = None
            
            number_of_rows = self.utils.page.count_element("", f"{elm_statement_history.div_body_content}//tbody/tr[not(contains(@class, 'first-row'))]")
            
            for i in range(1, number_of_rows + 1):
                row_base_selector = f"{elm_statement_history.div_body_content}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                
                row_class = self.utils.page.get_attribute(f"{row_base_selector}", "class")
                row_number = self.utils.page.get_text(f"{row_base_selector}/td[1]")
                
                has_expand_button = self.utils.page.does_element_exist(f"{row_base_selector}//span[contains(@class, 'caret')]")
                
                row_data = {
                    "id": row_number if row_number else "",
                    "date": self.utils.page.get_attribute(f"{row_base_selector}/td[2]", "title"),
                    "type": self.utils.page.get_attribute(f"{row_base_selector}/td[3]", "title"),
                    "amount": self.utils.page.get_attribute(f"{row_base_selector}/td[4]", "title"),
                    "status": self.utils.page.get_attribute(f"{row_base_selector}/td[5]", "title"),
                    "creator": self.utils.page.get_attribute(f"{row_base_selector}/td[6]", "title"),
                    "description": self.utils.page.get_attribute(f"{row_base_selector}/td[7]", "title"),
                    "row_class": row_class,
                    "is_parent": has_expand_button,
                    "is_child": not row_number and current_parent_data is not None,
                    "parent_id": current_parent_id
                }
                
                flat_data.append(row_data)
                
                if has_expand_button and row_number:
                    current_parent_id = row_number
                    current_parent_data = {
                        **row_data,
                        "children": []
                    }
                    
                    hierarchical_data.append(current_parent_data)
                    
                    expand_button_class = self.utils.page.get_attribute(f"{row_base_selector}//span[contains(@class, 'caret')]", "class")
                    
                    if expand_button_class and "collapsed" in expand_button_class:
                        try:
                            self.utils.page.click(f"{row_base_selector}//button")
                            self.utils.page.wait_load_page()
                            
                            new_number_of_rows = self.utils.page.count_element("", f"{elm_statement_history.div_body_content}//tbody/tr[not(contains(@class, 'first-row'))]")
                            
                            if new_number_of_rows > number_of_rows:
                                number_of_rows = new_number_of_rows
                        except Exception as click_error:
                            self.utils.page.extract_TestCaseFailed(f"Warning: Cannot expand row {row_number}: {click_error}")
            
                elif current_parent_data is not None and not row_number:
                    current_parent_data["children"].append(row_data)
            
            return {
                "hierarchical": hierarchical_data,
                "flat": flat_data
            }
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_personal_info_in_edit(self, username):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, username)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.edit)
            self.utils.page.wait_load_page()
            data = {
                "user_name": self.utils.page.get_text(elm_edit_customer.txt_username),
                "first_name": self.utils.page.get_text(elm_edit_customer.inp_first_name),
                "last_name": self.utils.page.get_text(elm_edit_customer.inp_last_name),
                "gender": self.utils.page.get_text(elm_edit_customer.sel_gender),
                "contact_number": self.utils.page.get_text(elm_edit_customer.inp_contact_number),
                "msn_ym_qq": self.utils.page.get_text(elm_edit_customer.inp_msn_ym_qq),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_data_additional_infomation_in_edit(self, username):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, username)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.utils.page.click(elm_submenu.edit)
            self.utils.page.wait_load_page()
            data = {
                "address": self.utils.page.get_text(elm_edit_customer.inp_address),
                "city": self.utils.page.get_text(elm_edit_customer.inp_city),
                "state": self.utils.page.get_text(elm_edit_customer.inp_state),
                "postcode": self.utils.page.get_text(elm_edit_customer.inp_postcode),
                "country": self.utils.page.get_text(elm_edit_customer.sel_country),
                "security_question": self.utils.page.get_text(elm_edit_customer.txt_security_question),
                "security_answer": self.utils.page.get_text(elm_edit_customer.txt_security_answer),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_email_format_preference_in_edit(self, username):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, username)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            data = {
                "email_format": self.utils.page.get_text(elm_edit_customer.sel_email_format),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_website_information_in_edit(self, username):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, username)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            data = {
                "website_url": self.utils.page.get_text(elm_edit_customer.txt_website_url),
                "no_site_description": self.utils.page.get_text(elm_edit_customer.txt_no_site_description),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_data_payment_information_in_edit(self, username):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, username)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            data = {
                "preferred_payment": self.utils.page.get_text(elm_edit_customer.sel_preferred_payment),
                "player_username": self.utils.page.get_text(elm_edit_customer.inp_player_username),
                "minimum_payment": self.utils.page.get_text(elm_edit_customer.txt_minimum_payment),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)