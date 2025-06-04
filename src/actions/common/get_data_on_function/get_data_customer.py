import time
import json
import re

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
from test_data.admin.customer.click_statistics.landing_pages.landing_pages import LANDING_PAGE_STATISTICS_API, LANDING_PAGE_DETAILS_API, DEVICE_TYPE_MAPPING, REQUIRED_HEADERS, REQUEST_BODY_TEMPLATE, DETAILS_REQUEST_BODY_TEMPLATE
from test_data.admin.customer.affiliate_info import AFFILIATE_INFO_API, AFFILIATE_INFO_HEADERS, AFFILIATE_INFO_REQUEST_TEMPLATE
from test_data.admin.customer.click_statistics.referrers.referrers import REFERRERS_API, REFERRERS_DETAILS_API, REFERRERS_REQUIRED_HEADERS, REFERRERS_REQUEST_BODY_TEMPLATE, REFERRERS_DETAILS_REQUEST_BODY_TEMPLATE
from test_data.admin.customer.click_statistics.marketing_page.marketing_pages import MARKETING_PAGES_API, MARKETING_PAGES_REQUIRED_HEADERS, MARKETING_PAGES_REQUEST_BODY_TEMPLATE

class GetDataCustomer(Common):
    
    def get_data_referrers_in_customer(self, user_name, from_date=None, to_date=None, device_type="All", get_detail=True):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_for_element_ready(elm_submenu.click_statistics, visible=True, enabled=True)
            time.sleep(2)
            self.utils.page.click_with_retry(elm_submenu.click_statistics)
            self.utils.page.wait_for_element_ready(elm_submenu_click_statistics.li_referrers, visible=True, enabled=True)
            self.utils.page.click_with_retry(elm_submenu_click_statistics.li_referrers)
            self.utils.page.wait_for_element_ready(elm_referrers.div_from_date, visible=True, enabled=True)
            super().select_date_picker(elm_referrers.div_from_date, from_date)
            super().select_date_picker(elm_referrers.div_to_date, to_date)
            self.utils.page.select_options(elm_referrers.sel_device, device_type)
            self.utils.page.click(elm_referrers.btn_search)
            self.utils.page.wait_for_element_ready(elm_referrers.div_table_first, visible=True, enabled=True)
            
            result = {
                "site_urls_data": [],
                "website_urls_data": {},
                "has_data": True
            }
            
            no_data_message = self.utils.page.count_element("", f"//*[contains(text(), 'There is no information available')]")
            if no_data_message > 0:
                result["has_data"] = False
                return result
            
            self.utils.page.wait_for_network_idle()
            self.utils.page.wait_for_element_ready(elm_referrers.div_table_first, visible=True, enabled=True)
            
            number_of_rows = self.utils.page.count_element("", f"{elm_referrers.div_table_first}//tbody/tr[not(contains(@class, 'first-row'))]")
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_referrers.div_table_first}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                
                self.utils.page.wait_for_element_ready(f"{row_selector}//td[1]", timeout=10)
                
                site_url = self.utils.page.get_text(f"{row_selector}//td[1]")
                total_click = self.utils.page.get_text(f"{row_selector}//td[2]")
                unique_click = self.utils.page.get_text(f"{row_selector}//td[3]")
                signups = self.utils.page.get_text(f"{row_selector}//td[4]")
                fdm = self.utils.page.get_text(f"{row_selector}//td[5]")
                
                site_data = {
                    "site_url": site_url,
                    "total_click": total_click,
                    "unique_click": unique_click,
                    "signups": signups,
                    "fdm": fdm
                }
                result["site_urls_data"].append(site_data)
                
                if get_detail and site_url.lower() != "none":
                    detail_button = f"{row_selector}//button"
                    if self.utils.page.does_element_exist(detail_button):
                        try:
                            self.utils.page.click_with_retry(detail_button, max_attempts=3)
                            
                            self.utils.page.wait_for_element_ready(elm_referrers.tbl_website_url, timeout=10)
                            time.sleep(2)
                            
                            website_urls = []
                            url_rows = self.utils.page.count_element("", f"{elm_referrers.tbl_website_url}//tbody/tr[not(contains(@class, 'first-row'))]")
                            
                            for j in range(1, url_rows + 1):
                                url_row_selector = f"{elm_referrers.tbl_website_url}//tbody/tr[not(contains(@class, 'first-row'))][{j}]"
                                
                                self.utils.page.wait_for_element_ready(f"{url_row_selector}//td[1]", timeout=5)
                                
                                website_url = self.utils.page.get_text(f"{url_row_selector}//td[1]")
                                time.sleep(0.2)
                                total_clicks = self.utils.page.get_text(f"{url_row_selector}//td[2]")
                                time.sleep(0.2)
                                unique_clicks = self.utils.page.get_text(f"{url_row_selector}//td[3]")
                                time.sleep(0.2)
                                sign_up = self.utils.page.get_text(f"{url_row_selector}//td[4]")
                                time.sleep(0.2)
                                url_fdm = self.utils.page.get_text(f"{url_row_selector}//td[5]")
                                
                                url_data = {
                                    "website_url": website_url,
                                    "total_clicks": total_clicks,
                                    "unique_clicks": unique_clicks,
                                    "sign_up": sign_up,
                                    "fdm": url_fdm
                                }
                                website_urls.append(url_data)
                            
                            result["website_urls_data"][site_url] = website_urls
                            
                            self.utils.page.click_with_retry(f"{row_selector}//td[1]")
                            
                        except Exception as click_error:
                            self.utils.page.extract_TestCaseFailed(f"Warning: Cannot get detail data for site {site_url}: {str(click_error)}")
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_landing_pages_in_customer(self, user_name, page_name="All", language="All", from_date=None, to_date=None, device_type="All", get_detail=True):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            time.sleep(2)
            self.utils.page.wait_for_element_ready(elm_submenu.click_statistics, visible=True, enabled=True)
            self.utils.page.click_with_retry(elm_submenu.click_statistics)
            time.sleep(2)
            self.utils.page.wait_for_element_ready(elm_submenu_click_statistics.li_landing_pages, visible=True, enabled=True)
            self.utils.page.click_with_retry(elm_submenu_click_statistics.li_landing_pages)
            self.utils.page.wait_for_element_ready(elm_landing_pages.sel_page, visible=True, enabled=True)
            self.utils.page.select_options(elm_landing_pages.sel_page, page_name)
            self.utils.page.select_options(elm_landing_pages.sel_language, language)
            super().select_date_picker(elm_landing_pages.div_from_date, from_date)
            super().select_date_picker(elm_landing_pages.div_to_date, to_date)
            self.utils.page.select_options(elm_landing_pages.sel_device, device_type)
            self.utils.page.click(elm_landing_pages.btn_search)
            time.sleep(2)
            
            result = {
                "pages_data": [],
                "website_urls_data": {},
                "has_data": True
            }
            
            no_data_message = self.utils.page.count_element("", f"//*[contains(text(), 'There is no information available')]")
            if no_data_message > 0:
                result["has_data"] = False
                return result
            
            self.utils.page.wait_for_network_idle()
            
            number_of_rows = self.utils.page.count_element("", f"{elm_landing_pages.tbl_pages}//tbody/tr[not(contains(@class, 'first-row'))]")
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_landing_pages.tbl_pages}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                page_name = self.utils.page.get_text(f"{row_selector}//td[1]")
                time.sleep(0.2)
                language = self.utils.page.get_text(f"{row_selector}//td[2]")
                time.sleep(0.2)
                total_click = self.utils.page.get_text(f"{row_selector}//td[3]")
                time.sleep(0.2)
                unique_click = self.utils.page.get_text(f"{row_selector}//td[4]")
                time.sleep(0.2)
                signups = self.utils.page.get_text(f"{row_selector}//td[5]")
                time.sleep(0.2)
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
                
                if get_detail and page_name.lower() != "none":
                    try:
                        self.utils.page.click(f"{row_selector}//button")
                        self.utils.page.wait_load_page()
                        time.sleep(2)
                        
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
                        time.sleep(2)
                    except Exception as click_error:
                        self.utils.page.extract_TestCaseFailed(f"Warning: Cannot get detail data for page {page_name}: {str(click_error)}")
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_marketing_pages_in_customer(self, user_name, language="All", from_date=None, to_date=None, include_inactive_tracking=False, get_detail=True):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            time.sleep(3)
            self.utils.page.click(elm_submenu.click_statistics)
            self.utils.page.wait_load_page()
            time.sleep(2.5)
            self.utils.page.click(elm_submenu_click_statistics.li_marketing_page)
            self.utils.page.wait_load_page()
            time.sleep(3)
            super().select_date_picker(elm_marketing_page.div_from_date, from_date)
            super().select_date_picker(elm_marketing_page.div_to_date, to_date)
            self.utils.page.select_options(elm_marketing_page.sel_language, language)

            if include_inactive_tracking:
                self.utils.page.click(elm_marketing_page.chk_include_inactive)

            self.utils.page.click(elm_marketing_page.btn_search)
            self.utils.page.wait_load_page()
            time.sleep(3)
            
            result = {
                "channels_data": [],
                "channel_details_data": {},
                "has_data": True
            }

            no_data_message = self.utils.page.count_element("", f"//*[contains(text(), 'There is no information available')]")
            if no_data_message > 0:
                result["has_data"] = False
                return result

            rows = self.utils.page.count_element("", f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))]")
            i = 1
            
            while i <= rows:
                row_selector = f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                
                first_cell = self.utils.page.get_text(f"{row_selector}/td[1]").strip()
                
                if first_cell.isdigit():
                    channel_row_number = first_cell
                    channel_name = self.utils.page.get_text(f"{row_selector}/td[2]").strip()
                    time.sleep(0.2)
                    language = self.utils.page.get_text(f"{row_selector}/td[3]").strip()
                    time.sleep(0.2)
                    total_click = self.utils.page.get_text(f"{row_selector}/td[4]").strip()
                    time.sleep(0.2)
                    unique_click = self.utils.page.get_text(f"{row_selector}/td[5]").strip()
                    time.sleep(0.2)
                    signups = self.utils.page.get_text(f"{row_selector}/td[6]").strip()
                    time.sleep(0.2)
                    fdm = self.utils.page.get_text(f"{row_selector}/td[7]").strip()
                    
                    channel_key = f"{channel_row_number} - {channel_name}"
                    
                    channel_data = {
                        "channel_name": channel_name,
                        "language": language,
                        "total_click": total_click,
                        "unique_click": unique_click,
                        "signups": signups,
                        "fdm": fdm
                    }
                    result["channels_data"].append(channel_data)
                    
                    can_expand = self.utils.page.count_element("", f"{row_selector}/td[2]//*[contains(@class, 'caret')]") > 0
                    
                    if get_detail and can_expand:
                        try:
                            self.utils.page.click(f"{row_selector}/td[2]")
                            self.utils.page.wait_load_page()
                            time.sleep(3)
                            
                            new_rows = self.utils.page.count_element("", f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))]")
                            details_count = new_rows - rows
                            
                            detail_urls = []
                            
                            for j in range(1, details_count + 1):
                                detail_row_selector = f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))][{i + j}]"
                                
                                url = self.utils.page.get_text(f"{detail_row_selector}/td[1]").strip()
                                time.sleep(0.2)
                                url_language = self.utils.page.get_text(f"{detail_row_selector}/td[2]").strip()
                                time.sleep(0.2)
                                url_total_clicks = self.utils.page.get_text(f"{detail_row_selector}/td[3]").strip()
                                time.sleep(0.2)
                                url_unique_clicks = self.utils.page.get_text(f"{detail_row_selector}/td[4]").strip()
                                time.sleep(0.2)
                                url_signups = self.utils.page.get_text(f"{detail_row_selector}/td[5]").strip()
                                time.sleep(0.2)
                                url_fdm = self.utils.page.get_text(f"{detail_row_selector}/td[6]").strip()
                                
                                url_data = {
                                    "url": url,
                                    "language": url_language,
                                    "total_clicks": url_total_clicks,
                                    "unique_clicks": url_unique_clicks,
                                    "signups": url_signups,
                                    "fdm": url_fdm
                                }
                                detail_urls.append(url_data)
                            
                            result["channel_details_data"][channel_key] = detail_urls
                            
                            self.utils.page.click(f"{row_selector}/td[2]")
                            self.utils.page.wait_load_page()
                            time.sleep(3)
                            
                            rows = self.utils.page.count_element("", f"{elm_marketing_page.tbl_marketing}//tbody/tr[not(contains(@class, 'first-row'))]")
                        
                        except Exception as click_error:
                            self.utils.page.extract_TestCaseFailed(f"Warning: Cannot get detail data for channel {channel_name}: {str(click_error)}")
                    i += 1
                else:
                    i += 1
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_statistics_in_customer(self, user_name, month_date):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, user_name)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_load_page()
            self.playwright.wait_for_load_state("domcontentloaded")
            time.sleep(3)
            super().select_month_picker(elm_statistics.inp_month, month_date)
            self.utils.page.wait_load_page()
            time.sleep(3)
            
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
            time.sleep(3)
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
            time.sleep(3)
            self.utils.page.click(elm_submenu.statement_history)
            self.utils.page.wait_load_page()
            time.sleep(3)
            super().select_date_picker(elm_statement_history.div_from_group, from_date)
            super().select_date_picker(elm_statement_history.div_to_group, to_date)
            
            if get_all:
                self.utils.page.click(elm_statement_history.chk_get_all)
            
            self.utils.page.click(elm_statement_history.btn_search)
            self.utils.page.wait_load_page()
            time.sleep(3)
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
            time.sleep(3)
            self.utils.page.click(elm_submenu.edit)
            self.utils.page.wait_load_page()
            time.sleep(3)
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
            time.sleep(3)
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
            time.sleep(3)
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
            time.sleep(3)
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
            time.sleep(3)
            data = {
                "preferred_payment": self.utils.page.get_text(elm_edit_customer.sel_preferred_payment),
                "player_username": self.utils.page.get_text(elm_edit_customer.inp_player_username),
                "minimum_payment": self.utils.page.get_text(elm_edit_customer.txt_minimum_payment),
            }
            return data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_landing_pages_via_api(self, user_name, page_name="All", language="All", from_date=None, to_date=None, device_type="All"):
        try:
            if not hasattr(self, 'utils') or not hasattr(self.utils, 'api'):
                self.utils.page.extract_TestCaseFailed("API client not initialized. Please ensure login_admin() was called first.")
            
            aff_id = self._get_affiliate_id(user_name)
            if not aff_id:
                self.utils.page.extract_TestCaseFailed(f"Could not find affiliate ID for username: {user_name}")
            
            current_url = self.utils.page.get_current_url()
            base_url = re.match(r'(https?://[^/]+)', current_url).group(1)
            
            list_api_url = f"{base_url}{LANDING_PAGE_STATISTICS_API}"
            details_api_url = f"{base_url}{LANDING_PAGE_DETAILS_API}"
            
            csrf_token = self._get_csrf_token()
            headers = REQUIRED_HEADERS.copy()
            headers["X-Requested-With"] = "XMLHttpRequest"
            if csrf_token:
                headers["__RequestVerificationToken"] = csrf_token
            
            device_type_value = DEVICE_TYPE_MAPPING.get(device_type, -1)
            
            list_request_body = REQUEST_BODY_TEMPLATE.copy()
            list_request_body.update({
                "deviceType": device_type_value,
                "fromDate": from_date,
                "toDate": to_date,
                "selectedPage": "" if page_name == "All" else page_name,
                "languageCode": "" if language == "All" else language,
                "affId": aff_id
            })
            
            list_response = self.utils.api.post(
                url=list_api_url,
                data=list_request_body,
                header=headers
            )
            
            if list_response.status != 200:
                self.utils.page.extract_TestCaseFailed(f"API request failed with status code: {list_response.status}")
            
            list_data = self.utils.api.extract_response_json(list_response)
            
            result = {
                "pages_data": [],
                "website_urls_data": {},
                "has_data": True
            }
            
            if not list_data or not isinstance(list_data, list) or len(list_data) == 0:
                result["has_data"] = False
                return result
            
            for page_item in list_data:
                page_data = {
                    "page_name": page_item.get("Page", ""),
                    "language": page_item.get("LanguageCode", ""),
                    "total_click": str(page_item.get("TotalClick", 0)),
                    "unique_click": str(page_item.get("UniqueClick", 0)),
                    "signups": str(page_item.get("Signups", 0)),
                    "fdm": str(page_item.get("Fdm", 0))
                }
                result["pages_data"].append(page_data)
                
                if page_data["page_name"] and page_data["language"]:
                    page_key = f"{page_data['page_name']} - {page_data['language']}"
                    
                    details_request_body = DETAILS_REQUEST_BODY_TEMPLATE.copy()
                    details_request_body.update({
                        "deviceType": device_type_value,
                        "fromDate": from_date,
                        "toDate": to_date,
                        "selectedPage": page_data["page_name"],
                        "languageCode": page_data["language"],
                        "affId": aff_id,
                        "pageIndex": 1,
                        "pageSize": 20
                    })

                    details_response = self.utils.api.post(
                        url=details_api_url,
                        data=details_request_body,
                        header=headers
                    )
                    
                    if details_response.status == 200:
                        details_data = self.utils.api.extract_response_json(details_response)
                        
                        if details_data and "MainData" in details_data:
                            result["website_urls_data"][page_key] = []
                            
                            for url_item in details_data["MainData"]:
                                url_data = {
                                    "website_url": url_item.get("WebsiteUrl", ""),
                                    "total_clicks": str(url_item.get("TotalClick", 0)),
                                    "unique_clicks": str(url_item.get("UniqueClick", 0)),
                                    "sign_up": str(url_item.get("Signups", 0)),
                                    "fdm": str(url_item.get("Fdm", 0))
                                }
                                result["website_urls_data"][page_key].append(url_data)
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def _get_affiliate_id(self, username):
        try:
            current_url = self.utils.page.get_current_url()
            base_url = re.match(r'(https?://[^/]+)', current_url).group(1)
            api_url = f"{base_url}{AFFILIATE_INFO_API}"
            
            csrf_token = self._get_csrf_token()
            headers = AFFILIATE_INFO_HEADERS.copy()
            headers["X-Requested-With"] = "XMLHttpRequest"
            
            if csrf_token:
                headers["__RequestVerificationToken"] = csrf_token
            
            request_body = AFFILIATE_INFO_REQUEST_TEMPLATE.copy()
            request_body["affUsername"] = username
            
            response = self.utils.api.post(
                url=api_url,
                data=request_body,
                header=headers
            )
            
            if response.status != 200:
                self.utils.page.extract_TestCaseFailed(f"API request failed with status code: {response.status}, Response: {response.text}")
                return None
            
            response_data = self.utils.api.extract_response_json(response)
            
            if response_data and "AffId" in response_data:
                return response_data["AffId"]
            
            self.utils.page.extract_TestCaseFailed(f"AffId not found in API response for username: {username}")
            return None
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(f"Failed to get affiliate ID: {str(e)}")
            return None
            
    def _get_csrf_token(self):
        try:
            form_token = self.utils.page.page.evaluate("""
                () => {
                    // Tìm input token trong form
                    const tokenInput = document.querySelector('input[name="__RequestVerificationToken"]');
                    if (tokenInput && tokenInput.value) return tokenInput.value;
                    return null;
                }
            """)
            
            return form_token
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(f"Failed to get CSRF token: {str(e)}")
            return None

    def get_data_referrers_via_api(self, user_name, from_date=None, to_date=None, device_type="All"):
        """
        Get referrers data via API instead of UI interaction
        
        Args:
            user_name (str): Affiliate username
            from_date (str): Start date in MM/DD/YYYY format
            to_date (str): End date in MM/DD/YYYY format
            device_type (str): Device type filter ('All', 'PC / Laptop', or 'Mobile')
            
        Returns:
            dict: Formatted referrers data including site_urls_data and website_urls_data
        """
        try:
            if not hasattr(self, 'utils') or not hasattr(self.utils, 'api'):
                self.utils.page.extract_TestCaseFailed("API client not initialized. Please ensure login_admin() was called first.")
            
            aff_id = self._get_affiliate_id(user_name)
            if not aff_id:
                self.utils.page.extract_TestCaseFailed(f"Could not find affiliate ID for username: {user_name}")
            
            current_url = self.utils.page.get_current_url()
            base_url = re.match(r'(https?://[^/]+)', current_url).group(1)
            
            list_api_url = f"{base_url}{REFERRERS_API}"
            details_api_url = f"{base_url}{REFERRERS_DETAILS_API}"
            
            csrf_token = self._get_csrf_token()
            headers = REFERRERS_REQUIRED_HEADERS.copy()
            headers["X-Requested-With"] = "XMLHttpRequest"
            if csrf_token:
                headers["__RequestVerificationToken"] = csrf_token
            
            device_type_value = DEVICE_TYPE_MAPPING.get(device_type, -1)
            
            list_request_body = REFERRERS_REQUEST_BODY_TEMPLATE.copy()
            list_request_body.update({
                "deviceType": device_type_value,
                "fromDate": from_date,
                "toDate": to_date,
                "affId": aff_id
            })
            
            list_response = self.utils.api.post(
                url=list_api_url,
                data=list_request_body,
                header=headers
            )
            
            if list_response.status != 200:
                self.utils.page.extract_TestCaseFailed(f"API request failed with status code: {list_response.status}")
            
            list_data = self.utils.api.extract_response_json(list_response)
            
            result = {
                "site_urls_data": [],
                "website_urls_data": {},
                "has_data": True
            }
            
            if not list_data or not isinstance(list_data, list) or len(list_data) == 0:
                result["has_data"] = False
                return result
            
            for site_item in list_data:
                site_data = {
                    "site_url": site_item.get("ReferrerUrl", ""),
                    "total_click": str(site_item.get("TotalClick", 0)),
                    "unique_click": str(site_item.get("UniqueClick", 0)),
                    "signups": str(site_item.get("Signups", 0)),
                    "fdm": str(site_item.get("Fdm", 0))
                }
                result["site_urls_data"].append(site_data)
                
                if site_data["site_url"] and site_data["site_url"].lower() != "none":
                    referrer_url = site_data["site_url"]
                    
                    details_request_body = REFERRERS_DETAILS_REQUEST_BODY_TEMPLATE.copy()
                    details_request_body.update({
                        "deviceType": device_type_value,
                        "fromDate": from_date,
                        "toDate": to_date,
                        "referrerUrl": referrer_url,
                        "affId": aff_id,
                        "pageIndex": 1,
                        "pageSize": 20
                    })

                    details_response = self.utils.api.post(
                        url=details_api_url,
                        data=details_request_body,
                        header=headers
                    )
                    
                    if details_response.status == 200:
                        details_data = self.utils.api.extract_response_json(details_response)
                        
                        if details_data and "MainData" in details_data:
                            result["website_urls_data"][referrer_url] = []
                            
                            for url_item in details_data["MainData"]:
                                url_data = {
                                    "website_url": url_item.get("WebsiteUrl", ""),
                                    "total_clicks": str(url_item.get("TotalClick", 0)),
                                    "unique_clicks": str(url_item.get("UniqueClick", 0)),
                                    "sign_up": str(url_item.get("Signups", 0)),
                                    "fdm": str(url_item.get("Fdm", 0))
                                }
                                result["website_urls_data"][referrer_url].append(url_data)
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def get_data_marketing_pages_via_api(self, user_name, language="All", from_date=None, to_date=None, include_inactive_tracking=False):
        try:
            if not hasattr(self, 'utils') or not hasattr(self.utils, 'api'):
                self.utils.page.extract_TestCaseFailed("API client not initialized. Please ensure login_admin() was called first.")
            
            aff_id = self._get_affiliate_id(user_name)
            if not aff_id:
                self.utils.page.extract_TestCaseFailed(f"Could not find affiliate ID for username: {user_name}")
            
            current_url = self.utils.page.get_current_url()
            base_url = re.match(r'(https?://[^/]+)', current_url).group(1)
            
            api_url = f"{base_url}{MARKETING_PAGES_API}"
            
            csrf_token = self._get_csrf_token()
            headers = MARKETING_PAGES_REQUIRED_HEADERS.copy()
            headers["X-Requested-With"] = "XMLHttpRequest"
            if csrf_token:
                headers["__RequestVerificationToken"] = csrf_token
            
            language_code = "" if language == "All" else language
            
            request_body = MARKETING_PAGES_REQUEST_BODY_TEMPLATE.copy()
            request_body.update({
                "affId": aff_id,
                "fromDate": from_date,
                "toDate": to_date,
                "languageCodes": language_code,
                "includedInActive": include_inactive_tracking
            })
            
            response = self.utils.api.post(
                url=api_url,
                data=request_body,
                header=headers
            )
            
            if response.status != 200:
                self.utils.page.extract_TestCaseFailed(f"API request failed with status code: {response.status}")
            
            response_data = self.utils.api.extract_response_json(response)
            
            result = {
                "channels_data": [],
                "channel_details_data": {},
                "has_data": True
            }
            
            if not response_data or not isinstance(response_data, list) or len(response_data) == 0:
                result["has_data"] = False
                return result
            
            channel_number = 0
            for channel_group in response_data:
                if not channel_group or len(channel_group) == 0:
                    continue
                
                channel_number += 1
                
                first_item = channel_group[0]
                channel_name = first_item.get("ChannelName", "")
                
                total_click = sum(item.get("TotalClick", 0) for item in channel_group)
                unique_click = sum(item.get("UniqueClick", 0) for item in channel_group)
                signups = sum(item.get("Signups", 0) for item in channel_group)
                fdm = sum(item.get("Fdm", 0) for item in channel_group)
                
                language = next((item.get("MarketName", "") for item in channel_group if item.get("MarketName")), "")
                
                channel_data = {
                    "channel_name": channel_name,
                    "language": language,
                    "total_click": str(total_click),
                    "unique_click": str(unique_click),
                    "signups": str(signups),
                    "fdm": str(fdm)
                }
                result["channels_data"].append(channel_data)
                
                channel_key = f"{channel_number} - {channel_name}"
                result["channel_details_data"][channel_key] = []
                
                for url_item in channel_group:
                    url_data = {
                        "url": url_item.get("WebsiteUrl", ""),
                        "language": url_item.get("MarketName", ""),
                        "total_clicks": str(url_item.get("TotalClick", 0)),
                        "unique_clicks": str(url_item.get("UniqueClick", 0)),
                        "signups": str(url_item.get("Signups", 0)),
                        "fdm": str(url_item.get("Fdm", 0))
                    }
                    result["channel_details_data"][channel_key].append(url_data)
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)