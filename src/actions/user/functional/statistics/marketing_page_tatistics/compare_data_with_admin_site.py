from config.constants.settings import *
env = ENVIRONMENT
import inspect
from datetime import datetime, timedelta

from src.actions.common.action_common import Common
from src.test_data.common.data_common import *
from src.actions.user.functional.statistics.marketing_page_tatistics.get_data_marketing_pages import GetDataMarketingPages
from src.actions.user.functional.statistics.referrers_statistics.get_data_referrers import GetDataReferrers
from src.actions.user.functional.statistics.landing_pages_statistics.get_data_landing_pages import GetDataLandingPages

from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_month import DataMarketingPagesLastMonth
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_week import DataMarketingPagesLastWeek
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_yesterday import DataMarketingPagesYesterday

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

    def load_baseline_data(self):
        return {
            "yesterday": DataMarketingPagesYesterday.data_marketing_pages_yesterday,
            "last_week": DataMarketingPagesLastWeek.data_marketing_pages_last_week,
            "last_month": DataMarketingPagesLastMonth.data_marketing_pages_last_month,
        }

    @staticmethod
    def clear_cache():
        CompareDataWithAdminSite._cache_data = None
        CompareDataWithAdminSite._cache_username = None

    def preload_all_data(self):
        if CompareDataWithAdminSite._cache_data is not None:
            return CompareDataWithAdminSite._cache_data, CompareDataWithAdminSite._cache_username
        
        cache = {"user_marketing_pages": {}, "user_referrers": {}, "user_landing_pages": {}}
        
        baseline_last_month = self.baseline_data["last_month"]
        username = baseline_last_month["metadata"]["filters"]["username"]
        
        self.sso_login(username)
        
        get_data_marketing_pages = GetDataMarketingPages(self.utils)
        get_data_referrers = GetDataReferrers(self.utils)
        get_data_landing_pages = GetDataLandingPages(self.utils)
        
        for period, baseline in self.baseline_data.items():
            metadata = baseline["metadata"]
            from_date = metadata["period"]["from_date"]
            to_date = metadata["period"]["to_date"]
            
            user_data = get_data_marketing_pages.get_data_marketing_pages_user_site(
                from_date=from_date, to_date=to_date, get_detail=True
            )
            cache["user_marketing_pages"][period] = user_data
            
            referrers_data = get_data_referrers.get_data_referrers_user_site(
                from_date=from_date, to_date=to_date, device_type="All", get_detail=False
            )
            cache["user_referrers"][period] = referrers_data
            
            landing_pages_data = get_data_landing_pages.get_data_landing_pages_user_site(
                from_date=from_date, to_date=to_date, device_type="All", get_detail=False
            )
            cache["user_landing_pages"][period] = landing_pages_data
        
        CompareDataWithAdminSite._cache_data = cache
        CompareDataWithAdminSite._cache_username = username
        return cache, username

    def parse_int(self, value):
        try:
            if value is None or value == "" or str(value).lower() == "none":
                return 0
            return int(str(value).replace(",", ""))
        except (ValueError, TypeError):
            return 0

    def compare_marketing_data_accuracy(self, baseline_data, user_data):
        mismatches = []
        
        if not baseline_data.get("metadata", {}).get("has_data", True):
            if user_data.get("has_data", True):
                mismatches.append(f"Baseline has no data but user site returned data")
            return mismatches
        
        if not user_data.get("has_data", True):
            mismatches.append(f"User site has no data but baseline expects data")
            return mismatches
        
        baseline_channels = baseline_data.get("channels_data", [])
        user_channels = user_data.get("channels_data", [])
        
        if len(baseline_channels) != len(user_channels):
            mismatches.append(f"Channel count mismatch: Baseline={len(baseline_channels)}, User={len(user_channels)}")
        
        for baseline_channel in baseline_channels:
            channel_name = baseline_channel["channel_name"]
            language = baseline_channel["language"]
            user_channel = None
            
            for uc in user_channels:
                if uc["channel_name"] == channel_name and uc["language"] == language:
                    user_channel = uc
                    break
            
            if not user_channel:
                mismatches.append(f"Channel '{channel_name} - {language}' not found in user data")
                continue
            
            for field in ["total_click", "unique_click", "signups", "fdm"]:
                baseline_val = self.parse_int(baseline_channel[field])
                user_val = self.parse_int(user_channel[field])
                
                if baseline_val != user_val:
                    mismatches.append(f"Channel '{channel_name} - {language}' {field}: Baseline={baseline_val}, User={user_val}")
        
        baseline_details = baseline_data.get("channel_details_data", {})
        user_details = user_data.get("channel_details_data", {})
        
        for channel_key, baseline_urls in baseline_details.items():
            if channel_key not in user_details:
                mismatches.append(f"Channel detail data for '{channel_key}' not found in user data")
                continue
            
            user_urls = user_details[channel_key]
            
            if len(baseline_urls) != len(user_urls):
                mismatches.append(f"URL count for channel '{channel_key}': Baseline={len(baseline_urls)}, User={len(user_urls)}")
            
            for baseline_url in baseline_urls:
                url = baseline_url["url"]
                user_url = None
                
                for uu in user_urls:
                    if uu["url"] == url:
                        user_url = uu
                        break
                
                if not user_url:
                    mismatches.append(f"URL '{url}' not found in user data for channel '{channel_key}'")
                    continue
                
                for field in ["total_clicks", "unique_clicks", "signups", "fdm"]:
                    baseline_val = self.parse_int(baseline_url.get(field, 0))
                    user_val = self.parse_int(user_url.get(field, 0))
                    
                    if baseline_val != user_val:
                        mismatches.append(f"URL '{url}' {field}: Baseline={baseline_val}, User={user_val}")
        
        return mismatches

    def _verify_cross_table_comparison(self, testcase, marketing_field, compare_table, compare_field, checklist_text):
        cache, username = self.preload_all_data()
        
        mainChecklist = [checklist_text]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period, baseline in self.baseline_data.items():
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                display_marketing = marketing_field.replace("_", " ").title()
                display_compare = compare_field.replace("_", " ").title()
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} {display_marketing} vs {compare_table.title()} {display_compare}"
                subAutoTestCase += f"\n     + Username: {username}"
                
                marketing_total = 0
                for channel in baseline.get("channels_data", []):
                    marketing_total += self.parse_int(channel.get(marketing_field, 0))
                
                compare_total = 0
                if compare_table == "referrers":
                    compare_data = cache["user_referrers"][period]
                    if compare_data.get("has_data", True):
                        for site_data in compare_data.get("site_urls_data", []):
                            compare_total += self.parse_int(site_data.get(compare_field, 0))
                else:
                    compare_data = cache["user_landing_pages"][period]
                    if compare_data.get("has_data", True):
                        for page_data in compare_data.get("pages_data", []):
                            compare_total += self.parse_int(page_data.get(compare_field, 0))
                
                if marketing_total == compare_total:
                    subAutoTestCase += f"\n     + {display_marketing}/{display_compare} match: {marketing_total}"
                else:
                    subAutoTestCase += f"\n     + {display_marketing}/{display_compare} mismatch: Marketing={marketing_total}, {compare_table.title()}={compare_total}"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def verify_page_filter_functionality(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Marketing Page data displays correctly according to the date picker."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period, baseline in self.baseline_data.items():
                user_data = cache["user_marketing_pages"][period]
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} date picker accuracy"
                
                from_date = baseline["metadata"]["period"]["from_date"]
                to_date = baseline["metadata"]["period"]["to_date"]
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {from_date}"
                subAutoTestCase += f"\n     + To Date: {to_date}"
                
                mismatches = self.compare_marketing_data_accuracy(baseline, user_data)
                
                if mismatches:
                    subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found"
                    for mismatch in mismatches[:3]:
                        subAutoTestCase += f"\n       - {mismatch}"
                    if len(mismatches) > 3:
                        subAutoTestCase += f"\n       - ... and {len(mismatches) - 3} more"
                else:
                    subAutoTestCase += f"\n     + Verified: All marketing pages data matches for period"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def verify_language_filter_functionality(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Marketing Page data displays correctly according to the Language filter."]
        indexChl = 0
        
        try:
            subAutoTestCase = '- Verify language filter functionality'
            
            baseline = self.baseline_data["last_month"]
            user_data = cache["user_marketing_pages"]["last_month"]
            
            subAutoTestCase += f"\n     + Username: {username}"
            
            available_languages = set()
            for channel_key, url_details in baseline.get("channel_details_data", {}).items():
                for url_data in url_details:
                    lang = url_data.get("language", "")
                    if lang and lang.strip() and lang.lower() not in ["none", "-", "null"]:
                        available_languages.add(lang)
            
            if available_languages:
                test_language = list(available_languages)[0]
                subAutoTestCase += f"\n     + Testing language filter with: '{test_language}'"
                
                language_match_count = 0
                total_urls_checked = 0
                
                for channel_key, url_details in user_data.get("channel_details_data", {}).items():
                    for url_data in url_details:
                        total_urls_checked += 1
                        url_lang = url_data.get("language", "").strip()
                        if url_lang.lower() == test_language.lower() or not url_lang:
                            language_match_count += 1
                
                if total_urls_checked > 0:
                    match_percentage = (language_match_count / total_urls_checked) * 100
                    subAutoTestCase += f"\n     + Language filter verification: {language_match_count}/{total_urls_checked} URLs verified ({match_percentage:.1f}%)"
                else:
                    subAutoTestCase += f"\n     + No URL details found for language filter verification"
            else:
                subAutoTestCase += "\n     + No valid languages found in baseline data for testing"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def verify_sub_data_table_display(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the sum of the collapsed data equals the data in the expanded section."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period, baseline in self.baseline_data.items():
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} collapsed/expanded data match"
                subAutoTestCase += f"\n     + Username: {username}"
                
                channels_data = baseline.get("channels_data", [])
                channel_details_data = baseline.get("channel_details_data", {})
                
                mismatches = []
                
                for channel in channels_data:
                    channel_name = channel["channel_name"]
                    
                    matching_detail_key = None
                    for detail_key in channel_details_data.keys():
                        if detail_key.endswith(f" - {channel_name}"):
                            matching_detail_key = detail_key
                            break
                    
                    if not matching_detail_key:
                        continue
                    
                    channel_total_clicks = self.parse_int(channel["total_click"])
                    channel_unique_clicks = self.parse_int(channel["unique_click"])
                    channel_signups = self.parse_int(channel["signups"])
                    channel_fdm = self.parse_int(channel["fdm"])
                    
                    detail_total_clicks = 0
                    detail_unique_clicks = 0
                    detail_signups = 0
                    detail_fdm = 0
                    
                    for url_data in channel_details_data[matching_detail_key]:
                        detail_total_clicks += self.parse_int(url_data.get("total_clicks", 0))
                        detail_unique_clicks += self.parse_int(url_data.get("unique_clicks", 0))
                        detail_signups += self.parse_int(url_data.get("signups", 0))
                        detail_fdm += self.parse_int(url_data.get("fdm", 0))
                    
                    if channel_total_clicks != detail_total_clicks:
                        mismatches.append(f"Total clicks mismatch for '{channel_name}'")
                    if channel_unique_clicks != detail_unique_clicks:
                        mismatches.append(f"Unique clicks mismatch for '{channel_name}'")
                    if channel_signups != detail_signups:
                        mismatches.append(f"Signups mismatch for '{channel_name}'")
                    if channel_fdm != detail_fdm:
                        mismatches.append(f"FDM mismatch for '{channel_name}'")
                
                if mismatches:
                    subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found"
                else:
                    subAutoTestCase += f"\n     + Verified: All collapsed data equals expanded section"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def verify_total_clicks_match_referrers(self, testcase):
        self._verify_cross_table_comparison(testcase, "total_click", "referrers", "total_click", "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Referrers.")

    def verify_total_clicks_match_landing_pages(self, testcase):
        self._verify_cross_table_comparison(testcase, "total_click", "landing_pages", "total_click", "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Landing Pages.")

    def verify_signups_match_referrers(self, testcase):
        self._verify_cross_table_comparison(testcase, "signups", "referrers", "signups", "Verify that the Signups on the Marketing Page equal the Signups of Referrers.")

    def verify_signups_match_landing_pages(self, testcase):
        self._verify_cross_table_comparison(testcase, "signups", "landing_pages", "signups", "Verify that the Signups on the Marketing Page equal the Signups of Landing Pages.")

    def verify_fdm_match_referrers(self, testcase):
        self._verify_cross_table_comparison(testcase, "fdm", "referrers", "fdm", "Verify that the FDM on the Marketing Page equals the FDM of Referrers.")

    def verify_fdm_match_landing_pages(self, testcase):
        self._verify_cross_table_comparison(testcase, "fdm", "landing_pages", "fdm", "Verify that the FDM on the Marketing Page equals the FDM of Landing Pages.")

    def verify_total_clicks_has_unique_clicks(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that if there is data in the Total Clicks column, the Unique Click column also contains data."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            
            for period, baseline in self.baseline_data.items():
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify {period.replace('_', ' ')} Total/Unique Clicks relationship"
                subAutoTestCase += f"\n     + Username: {username}"
                
                violations = []
                
                for channel in baseline.get("channels_data", []):
                    channel_name = channel["channel_name"]
                    total_clicks = self.parse_int(channel["total_click"])
                    unique_clicks = self.parse_int(channel["unique_click"])
                    
                    if total_clicks > 0 and unique_clicks == 0:
                        violations.append(f"Channel '{channel_name}' has Total Clicks but no Unique Clicks")
                
                for channel_key, url_details in baseline.get("channel_details_data", {}).items():
                    for url_data in url_details:
                        url = url_data.get("url", "")
                        total_clicks = self.parse_int(url_data.get("total_clicks", 0))
                        unique_clicks = self.parse_int(url_data.get("unique_clicks", 0))
                        
                        if total_clicks > 0 and unique_clicks == 0:
                            violations.append(f"URL has Total Clicks but no Unique Clicks")
                
                if violations:
                    subAutoTestCase += f"\n     + Failed: {len(violations)} violations found"
                else:
                    subAutoTestCase += f"\n     + Verified: All Total Clicks have corresponding Unique Clicks"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e) 