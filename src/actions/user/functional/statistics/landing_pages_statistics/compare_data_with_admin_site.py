from config.constants.settings import *
env = ENVIRONMENT
import inspect
from datetime import datetime, timedelta

from src.actions.common.action_common import Common
from src.test_data.common.data_common import *
from src.actions.user.functional.statistics.landing_pages_statistics.get_data_landing_pages import GetDataLandingPages
from src.actions.user.functional.statistics.referrers_statistics.get_data_referrers import GetDataReferrers
from src.actions.user.functional.statistics.marketing_page_tatistics.get_data_marketing_pages import GetDataMarketingPages

from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday import DataLandingPagesYesterday
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday_by_desktop import DataLandingPagesYesterdayByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday_by_mobile import DataLandingPagesYesterdayByMobile
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week import DataLandingPagesLastWeek
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week_by_desktop import DataLandingPagesLastWeekByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week_by_mobile import DataLandingPagesLastWeekByMobile
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month import DataLandingPagesLastMonth
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month_by_desktop import DataLandingPagesLastMonthByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month_by_mobile import DataLandingPagesLastMonthByMobile

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"

class CompareDataWithAdminSite(Common):
    _cache_data = None
    _cache_username = None
    
    def __init__(self):
        super().__init__()
        self.baseline_data = self.load_baseline_data()

    @staticmethod
    def clear_cache():
        CompareDataWithAdminSite._cache_data = None
        CompareDataWithAdminSite._cache_username = None

    def load_baseline_data(self):
        return {
            "yesterday_All": DataLandingPagesYesterday().data_landing_pages_yesterday,
            "yesterday_PC / Laptop": DataLandingPagesYesterdayByDesktop().data_landing_pages_yesterday_by_desktop,
            "yesterday_Mobile": DataLandingPagesYesterdayByMobile().data_landing_pages_yesterday_by_mobile,
            "last_week_All": DataLandingPagesLastWeek().data_landing_pages_last_week,
            "last_week_PC / Laptop": DataLandingPagesLastWeekByDesktop().data_landing_pages_last_week_by_desktop,
            "last_week_Mobile": DataLandingPagesLastWeekByMobile().data_landing_pages_last_week_by_mobile,
            "last_month_All": DataLandingPagesLastMonth().data_landing_pages_last_month,
            "last_month_PC / Laptop": DataLandingPagesLastMonthByDesktop().data_landing_pages_last_month_by_desktop,
            "last_month_Mobile": DataLandingPagesLastMonthByMobile().data_landing_pages_last_month_by_mobile,
        }

    def parse_int(self, value):
        try:
            if value is None or value == "" or str(value).lower() == "none":
                return 0
            return int(str(value).replace(",", ""))
        except (ValueError, TypeError):
            return 0

    def preload_all_data(self):
        if CompareDataWithAdminSite._cache_data is not None:
            return CompareDataWithAdminSite._cache_data, CompareDataWithAdminSite._cache_username
        
        cache = {"user_landing_pages": {}, "user_referrers": {}, "user_marketing_pages": {}}
        
        baseline_last_month = self.baseline_data["last_month_All"]
        username = baseline_last_month["metadata"]["filters"]["username"]
        
        self.sso_login(username)
        
        get_data_landing_pages = GetDataLandingPages(self.utils)
        get_data_referrers = GetDataReferrers(self.utils)
        get_data_marketing_pages = GetDataMarketingPages(self.utils)
        
        processed_periods = set()
        
        for period_device, baseline in self.baseline_data.items():
            period, device = period_device.split("_", 1)
            
            metadata = baseline["metadata"]
            from_date = metadata["period"]["from_date"]
            to_date = metadata["period"]["to_date"]
            
            user_data = get_data_landing_pages.get_data_landing_pages_user_site(
                from_date=from_date, to_date=to_date, device_type=device, get_detail=True
            )
            cache["user_landing_pages"][period_device] = user_data
            
            referrers_data = get_data_referrers.get_data_referrers_user_site(
                from_date=from_date, to_date=to_date, device_type=device, get_detail=False
            )
            cache["user_referrers"][period_device] = referrers_data
            
            if device == "All" and period not in processed_periods:
                marketing_data = get_data_marketing_pages.get_data_marketing_pages_user_site(
                    from_date=from_date, to_date=to_date, get_detail=False
                )
                cache["user_marketing_pages"][period] = marketing_data
                processed_periods.add(period)
        
        CompareDataWithAdminSite._cache_data = cache
        CompareDataWithAdminSite._cache_username = username
        return cache, username

    def compare_data_accuracy(self, baseline_data, user_data, data_type):
        mismatches = []
        
        if not baseline_data.get("metadata", {}).get("has_data", True):
            if user_data.get("has_data", True):
                mismatches.append(f"Baseline has no data but user site returned data")
            return mismatches
        
        if not user_data.get("has_data", True):
            mismatches.append(f"User site has no data but baseline expects data")
            return mismatches
        
        baseline_pages = baseline_data.get("pages_data", [])
        user_pages = user_data.get("pages_data", [])
        
        if len(baseline_pages) != len(user_pages):
            mismatches.append(f"Page count mismatch: Baseline={len(baseline_pages)}, User={len(user_pages)}")
        
        for baseline_page in baseline_pages:
            page_name = baseline_page["page_name"]
            language = baseline_page["language"]
            user_page = None
            
            for up in user_pages:
                if up["page_name"] == page_name and up["language"] == language:
                    user_page = up
                    break
            
            if not user_page:
                mismatches.append(f"Page '{page_name} - {language}' not found in user data")
                continue
            
            for field in ["total_click", "unique_click", "signups", "fdm"]:
                baseline_val = self.parse_int(baseline_page[field])
                user_val = self.parse_int(user_page[field])
                
                if baseline_val != user_val:
                    mismatches.append(f"Page '{page_name} - {language}' {field}: Baseline={baseline_val}, User={user_val}")
        
        baseline_websites = baseline_data.get("website_urls_data", {})
        user_websites = user_data.get("website_urls_data", {})
        
        for page_key, baseline_urls in baseline_websites.items():
            if page_key not in user_websites:
                mismatches.append(f"Website data for page '{page_key}' not found in user data")
                continue
            
            user_urls = user_websites[page_key]
            
            if len(baseline_urls) != len(user_urls):
                mismatches.append(f"Website count for page '{page_key}': Baseline={len(baseline_urls)}, User={len(user_urls)}")
            
            for baseline_url in baseline_urls:
                website_url = baseline_url["website_url"]
                user_url = None
                
                for uu in user_urls:
                    if uu["website_url"] == website_url:
                        user_url = uu
                        break
                
                if not user_url:
                    mismatches.append(f"Website '{website_url}' not found in user data for page '{page_key}'")
                    continue
                
                for field in ["total_clicks", "unique_clicks", "signups", "fdm"]:
                    baseline_val = self.parse_int(baseline_url.get(field, 0))
                    user_val = self.parse_int(user_url.get(field, 0))
                    
                    if baseline_val != user_val:
                        mismatches.append(f"Website '{website_url}' {field}: Baseline={baseline_val}, User={user_val}")
        
        return mismatches

    def verify_date_picker_accuracy(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Landing Pages data displays correctly according to the date picker."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device, baseline in self.baseline_data.items():
                period, device = period_device.split("_", 1)
                user_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} date picker accuracy"
                
                from_date = baseline["metadata"]["period"]["from_date"]
                to_date = baseline["metadata"]["period"]["to_date"]
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + Period: {from_date} to {to_date}"
                subAutoTestCase += f"\n     + Device: {device}"
                
                mismatches = self.compare_data_accuracy(baseline, user_data, "date_picker")
                
                if not mismatches:
                    subAutoTestCase += f"\n     + Date picker accuracy verified - all data matches baseline"
                else:
                    subAutoTestCase += f"\n     + Date picker accuracy failed - {len(mismatches)} mismatches:"
                    for mismatch in mismatches[:3]:
                        subAutoTestCase += f"\n       - {mismatch}"
                    if len(mismatches) > 3:
                        subAutoTestCase += f"\n       - ... and {len(mismatches) - 3} more"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_device_filter_accuracy(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Landing Pages data displays correctly according to the Device filter."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} device filter accuracy"
                
                all_data = cache["user_landing_pages"][f"{period}_All"]
                desktop_data = cache["user_landing_pages"][f"{period}_PC / Laptop"]
                mobile_data = cache["user_landing_pages"][f"{period}_Mobile"]
                
                all_total = sum(self.parse_int(p["total_click"]) for p in all_data.get("pages_data", []))
                desktop_total = sum(self.parse_int(p["total_click"]) for p in desktop_data.get("pages_data", []))
                mobile_total = sum(self.parse_int(p["total_click"]) for p in mobile_data.get("pages_data", []))
                
                all_signups = sum(self.parse_int(p["signups"]) for p in all_data.get("pages_data", []))
                desktop_signups = sum(self.parse_int(p["signups"]) for p in desktop_data.get("pages_data", []))
                mobile_signups = sum(self.parse_int(p["signups"]) for p in mobile_data.get("pages_data", []))
                
                all_fdm = sum(self.parse_int(p["fdm"]) for p in all_data.get("pages_data", []))
                desktop_fdm = sum(self.parse_int(p["fdm"]) for p in desktop_data.get("pages_data", []))
                mobile_fdm = sum(self.parse_int(p["fdm"]) for p in mobile_data.get("pages_data", []))
                
                subAutoTestCase += f"\n     + Total Clicks - All: {all_total}, Desktop: {desktop_total}, Mobile: {mobile_total}"
                subAutoTestCase += f"\n     + Signups - All: {all_signups}, Desktop: {desktop_signups}, Mobile: {mobile_signups}"
                subAutoTestCase += f"\n     + FDM - All: {all_fdm}, Desktop: {desktop_fdm}, Mobile: {mobile_fdm}"
                
                breakdown_errors = []
                
                if all_total != desktop_total + mobile_total:
                    breakdown_errors.append(f"Total Clicks: {all_total} ≠ {desktop_total} + {mobile_total}")
                
                if all_signups != desktop_signups + mobile_signups:
                    breakdown_errors.append(f"Signups: {all_signups} ≠ {desktop_signups} + {mobile_signups}")
                
                if all_fdm != desktop_fdm + mobile_fdm:
                    breakdown_errors.append(f"FDM: {all_fdm} ≠ {desktop_fdm} + {mobile_fdm}")
                
                if not breakdown_errors:
                    subAutoTestCase += f"\n     + Device breakdown accurate: All = Desktop + Mobile"
                else:
                    subAutoTestCase += f"\n     + Device breakdown errors:"
                    for error in breakdown_errors:
                        subAutoTestCase += f"\n       - {error}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_page_filter_accuracy(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Landing Pages data displays correctly according to the Page filter."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device, baseline in self.baseline_data.items():
                period, device = period_device.split("_", 1)
                user_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} page filter accuracy"
                
                baseline_pages = baseline.get("pages_data", [])
                user_pages = user_data.get("pages_data", [])
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + Pages found: Baseline={len(baseline_pages)}, User={len(user_pages)}"
                
                page_mismatches = []
                for baseline_page in baseline_pages:
                    page_name = baseline_page["page_name"]
                    language = baseline_page["language"]
                    
                    user_page_found = any(
                        up["page_name"] == page_name and up["language"] == language 
                        for up in user_pages
                    )
                    
                    if not user_page_found:
                        page_mismatches.append(f"Page '{page_name} - {language}' not found in user data")
                
                if not page_mismatches:
                    subAutoTestCase += f"\n     + Page filter accuracy verified - all pages match"
                else:
                    subAutoTestCase += f"\n     + Page filter accuracy failed - {len(page_mismatches)} mismatches:"
                    for mismatch in page_mismatches[:3]:
                        subAutoTestCase += f"\n       - {mismatch}"
                    if len(page_mismatches) > 3:
                        subAutoTestCase += f"\n       - ... and {len(page_mismatches) - 3} more"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_language_filter_accuracy(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Landing Pages data displays correctly according to the Language filter."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device, baseline in self.baseline_data.items():
                period, device = period_device.split("_", 1)
                user_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} language filter accuracy"
                
                baseline_languages = set(p["language"] for p in baseline.get("pages_data", []))
                user_languages = set(p["language"] for p in user_data.get("pages_data", []))
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + Languages: Baseline={len(baseline_languages)}, User={len(user_languages)}"
                
                language_mismatches = []
                for lang in baseline_languages:
                    if lang not in user_languages:
                        language_mismatches.append(f"Language '{lang}' not found in user data")
                
                if not language_mismatches:
                    subAutoTestCase += f"\n     + Language filter accuracy verified - all languages match"
                else:
                    subAutoTestCase += f"\n     + Language filter accuracy failed - {len(language_mismatches)} mismatches:"
                    for mismatch in language_mismatches:
                        subAutoTestCase += f"\n       - {mismatch}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)



    def verify_total_clicks_vs_referrers(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Total Clicks for Landing Pages equal the Total Clicks for Referrers."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                referrers_data = cache["user_referrers"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} Total Clicks: Landing Pages vs Referrers"
                
                landing_total = sum(self.parse_int(p["total_click"]) for p in landing_data.get("pages_data", []))
                referrers_total = sum(self.parse_int(s["total_click"]) for s in referrers_data.get("site_urls_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_total}, Referrers: {referrers_total}"
                
                if landing_total == referrers_total:
                    subAutoTestCase += f"\n     + Total Clicks match"
                else:
                    subAutoTestCase += f"\n     + Total Clicks mismatch - difference: {abs(landing_total - referrers_total)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_total_clicks_vs_marketing_pages(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Total Clicks for Landing Pages equal the Total Clicks for Marketing Pages."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} Total Clicks: Landing Pages vs Marketing Pages"
                
                landing_data = cache["user_landing_pages"][f"{period}_All"]
                marketing_data = cache["user_marketing_pages"].get(period, {"channels_data": []})
                
                landing_total = sum(self.parse_int(p["total_click"]) for p in landing_data.get("pages_data", []))
                marketing_total = sum(self.parse_int(c["total_click"]) for c in marketing_data.get("channels_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_total}, Marketing Pages: {marketing_total}"
                
                if landing_total == marketing_total:
                    subAutoTestCase += f"\n     + Total Clicks match"
                else:
                    subAutoTestCase += f"\n     + Total Clicks mismatch - difference: {abs(landing_total - marketing_total)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_signups_vs_referrers(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Signups for Landing Pages equal the Signups for Referrers."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                referrers_data = cache["user_referrers"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} Signups: Landing Pages vs Referrers"
                
                landing_signups = sum(self.parse_int(p["signups"]) for p in landing_data.get("pages_data", []))
                referrers_signups = sum(self.parse_int(s["signups"]) for s in referrers_data.get("site_urls_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_signups}, Referrers: {referrers_signups}"
                
                if landing_signups == referrers_signups:
                    subAutoTestCase += f"\n     + Signups match"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch - difference: {abs(landing_signups - referrers_signups)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_signups_vs_marketing_pages(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Signups for Landing Pages equal the Signups for Marketing Pages."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} Signups: Landing Pages vs Marketing Pages"
                
                landing_data = cache["user_landing_pages"][f"{period}_All"]
                marketing_data = cache["user_marketing_pages"].get(period, {"channels_data": []})
                
                landing_signups = sum(self.parse_int(p["signups"]) for p in landing_data.get("pages_data", []))
                marketing_signups = sum(self.parse_int(c["signups"]) for c in marketing_data.get("channels_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_signups}, Marketing Pages: {marketing_signups}"
                
                if landing_signups == marketing_signups:
                    subAutoTestCase += f"\n     + Signups match"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch - difference: {abs(landing_signups - marketing_signups)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_fdm_vs_referrers(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the FDM for Landing Pages equals the FDM for Referrers."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                referrers_data = cache["user_referrers"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} FDM: Landing Pages vs Referrers"
                
                landing_fdm = sum(self.parse_int(p["fdm"]) for p in landing_data.get("pages_data", []))
                referrers_fdm = sum(self.parse_int(s["fdm"]) for s in referrers_data.get("site_urls_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_fdm}, Referrers: {referrers_fdm}"
                
                if landing_fdm == referrers_fdm:
                    subAutoTestCase += f"\n     + FDM match"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch - difference: {abs(landing_fdm - referrers_fdm)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_fdm_vs_marketing_pages(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the FDM for Landing Pages equals the FDM for Marketing Pages."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} FDM: Landing Pages vs Marketing Pages"
                
                landing_data = cache["user_landing_pages"][f"{period}_All"]
                marketing_data = cache["user_marketing_pages"].get(period, {"channels_data": []})
                
                landing_fdm = sum(self.parse_int(p["fdm"]) for p in landing_data.get("pages_data", []))
                marketing_fdm = sum(self.parse_int(c["fdm"]) for c in marketing_data.get("channels_data", []))
                
                subAutoTestCase += f"\n     + Landing Pages: {landing_fdm}, Marketing Pages: {marketing_fdm}"
                
                if landing_fdm == marketing_fdm:
                    subAutoTestCase += f"\n     + FDM match"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch - difference: {abs(landing_fdm - marketing_fdm)}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_sub_data_table_display(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that when clicking on a Page (if not None), the sub‑data table is displayed."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} sub-data table display"
                
                clickable_pages = 0
                sub_tables = 0
                
                for page_data in landing_data.get("pages_data", []):
                    page_name = page_data["page_name"]
                    language = page_data["language"]
                    page_key = f"{page_name} - {language}"
                    
                    if page_name and page_name.lower() != "none" and page_name.strip() != "":
                        clickable_pages += 1
                        if page_key in landing_data.get("website_urls_data", {}):
                            sub_tables += 1
                
                subAutoTestCase += f"\n     + Clickable pages: {clickable_pages}, Sub-tables found: {sub_tables}"
                
                if clickable_pages == 0:
                    subAutoTestCase += f"\n     + No clickable pages available (all are 'none' or empty)"
                elif sub_tables == clickable_pages:
                    subAutoTestCase += f"\n     + Sub-data tables displayed correctly for all clickable pages"
                elif sub_tables > 0:
                    subAutoTestCase += f"\n     + Sub-data tables displayed for {sub_tables}/{clickable_pages} clickable pages"
                else:
                    subAutoTestCase += f"\n     + No sub-data tables found despite having clickable pages"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_sub_data_table_values_match(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the values in the sub‑data table match the corresponding row in the main table."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} sub-data values match main table"
                
                mismatches = 0
                checked = 0
                total_websites = 0
                
                for page_data in landing_data.get("pages_data", []):
                    page_name = page_data["page_name"]
                    language = page_data["language"]
                    page_key = f"{page_name} - {language}"
                    
                    if page_name and page_name.lower() != "none" and page_key in landing_data.get("website_urls_data", {}):
                        checked += 1
                        main_total = self.parse_int(page_data["total_click"])
                        main_signups = self.parse_int(page_data["signups"])
                        main_fdm = self.parse_int(page_data["fdm"])
                        
                        website_data = landing_data["website_urls_data"][page_key]
                        total_websites += len(website_data)
                        
                        sub_total = sum(self.parse_int(w.get("total_clicks", 0)) for w in website_data)
                        sub_signups = sum(self.parse_int(w.get("signups", 0)) for w in website_data)
                        sub_fdm = sum(self.parse_int(w.get("fdm", 0)) for w in website_data)
                        
                        site_mismatches = []
                        if main_total != sub_total:
                            site_mismatches.append(f"Total Clicks: {main_total} vs {sub_total}")
                        if main_signups != sub_signups:
                            site_mismatches.append(f"Signups: {main_signups} vs {sub_signups}")
                        if main_fdm != sub_fdm:
                            site_mismatches.append(f"FDM: {main_fdm} vs {sub_fdm}")
                        
                        if site_mismatches:
                            mismatches += 1
                
                subAutoTestCase += f"\n     + Checked: {checked} pages with {total_websites} total websites"
                subAutoTestCase += f"\n     + Pages with mismatches: {mismatches}"
                
                if mismatches == 0 and checked > 0:
                    subAutoTestCase += f"\n     + All sub-data values match main table (excluding unique clicks)"
                elif checked == 0:
                    subAutoTestCase += f"\n     + No sub-data available for verification"
                else:
                    subAutoTestCase += f"\n     + Sub-data mismatches detected in {mismatches}/{checked} pages"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def verify_total_unique_clicks_relationship(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that if there is data in the Total Clicks column, then the Unique Click column also contains data."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            violations = 0
            total_checked = 0
            total_pages = 0
            
            for period_device in self.baseline_data.keys():
                period, device = period_device.split("_", 1)
                
                landing_data = cache["user_landing_pages"][period_device]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {device} Total/Unique Clicks relationship"
                
                period_violations = 0
                period_checked = 0
                period_pages = len(landing_data.get("pages_data", []))
                total_pages += period_pages
                
                for page_data in landing_data.get("pages_data", []):
                    total_clicks = self.parse_int(page_data["total_click"])
                    unique_clicks = self.parse_int(page_data["unique_click"])
                    page_name = page_data["page_name"]
                    language = page_data["language"]
                    
                    if total_clicks > 0:
                        period_checked += 1
                        total_checked += 1
                        if unique_clicks == 0:
                            period_violations += 1
                            violations += 1
                            subAutoTestCase += f"\n       VIOLATION: '{page_name} - {language}' has Total Clicks ({total_clicks}) but no Unique Clicks"
                        elif unique_clicks > total_clicks:
                            period_violations += 1
                            violations += 1
                            subAutoTestCase += f"\n       VIOLATION: '{page_name} - {language}' has Unique Clicks ({unique_clicks}) > Total Clicks ({total_clicks})"
                
                subAutoTestCase += f"\n     + Pages with Total Clicks: {period_checked}/{period_pages}"
                subAutoTestCase += f"\n     + Violations found: {period_violations}"
                
                if period_violations == 0 and period_checked > 0:
                    subAutoTestCase += f"\n     + All pages with Total Clicks have valid Unique Clicks"
                elif period_checked == 0:
                    subAutoTestCase += f"\n     + No pages have Total Clicks data"
            
            subAutoTestCase += f"\n\nOVERALL SUMMARY:"
            subAutoTestCase += f"\n+ Total pages checked: {total_pages}"
            subAutoTestCase += f"\n+ Pages with Total Clicks: {total_checked}"
            subAutoTestCase += f"\n+ Total violations: {violations}"
            
            if violations == 0:
                subAutoTestCase += f"\n+ All data passes Total/Unique Clicks relationship validation"
            else:
                subAutoTestCase += f"\n+ Data integrity issues detected!"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, 
                subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e) 