from src.actions.common.action_common import Common
from src.interfaces.demo_elements import DemoElements as elm_demo
from src.test_data.demo_test_data import DemoTestData as data_demo
from config.constants.settings import *
from src.test_data.common.data_common import *

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
}
Checklist_Sheet_Name = "Demo_Message"

class ActionDemo(Common):

    def verify_ui_message_page(self, testcase):
        try:
            mainChecklist = [
                "Verify that the button 'Add' is displayed",
                "Verify that the button 'Delete' is displayed",]
            subAutoTestCase = ''
            indexChl = 0

            subAutoTestCase += f"- Verify that the button 'Add' is displayed"

            # Implement logic check
            ...

            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            subAutoTestCase = ''

            subAutoTestCase += f"- Verify that the button 'Delete' is displayed"

            # Implement logic check here
            ...

            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            self.utils.page.extract_TestCaseFailed(e)