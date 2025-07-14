from src.actions.common.action_common import Common
from src.interfaces.demo_elements import DemoElements as elm_demo
from src.test_data.demo_test_data import DemoTestData as data_demo
from config.constants.settings import *
from src.test_data.common.data_common import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.utils.services.utils import utilities

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
}
Checklist_Sheet_Name = "Demo"

data = {
    "message": data_demo.test_data,
}

class ActionDemo(Common):
    utils: 'utilities'

    def verify_ui_message_page(self, testcase):
        try:
            mainChecklist = [
                "Verify that the button 'Add' is displayed",
                "Verify that the add new message is success",]
            subAutoTestCase = ''
            indexChl = 0

            subAutoTestCase += f"- Verify that the button 'Add' is displayed \n"

            # Implement logic check
            super().selectMenu("Message")
            self.utils.page.wait_for_page_loaded()
            self.utils.page.verify_element_exist(elm_demo.btn_search)
            self.utils.page.click(elm_demo.btn_search)
            self.utils.page.wait_for_page_loaded()
            self.utils.page.verify_element_exist(elm_demo.btn_add)
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

            subAutoTestCase += f"- Verify that the add new message is success"

            # Implement logic check here
            self.utils.page.click(elm_demo.btn_add)
            self.utils.page.wait_for_page_loaded()
            self.utils.page.verify_element_exist(elm_demo.mdl_add_message)
            if data["message"]["important"] == "Yes":
                self.utils.page.click(elm_demo.chk_important)
            self.utils.page.input(elm_demo.txt_english, data["message"]["english"])
            self.utils.page.input(elm_demo.txt_indonesian, data["message"]["indonesian"])
            self.utils.page.input(elm_demo.txt_korean, data["message"]["korean"])
            self.utils.page.input(elm_demo.txt_thai, data["message"]["thai"])
            self.utils.page.input(elm_demo.txt_vietnamese, data["message"]["vietnamese"])
            self.utils.page.input(elm_demo.txt_chinese, data["message"]["chinese"])
            self.utils.page.click(elm_demo.btn_add_modal)
            elm_message_form = "//div[@class='message-form-container']/div"
            self.utils.page.wait_for_page_loaded(elm_message_form)
            message_text = self.utils.page.get_text(elm_message_form)
            self.utils.should_be_equal(message_text,"Add Successfully!")
            self.utils.page.wait_for_page_loaded()

            subAutoTestCase += f"- Verify that the message is display correctly"

            element_message = "//div[@class='body-content']//tr[not(contains(@class, 'first-row'))]"
            self.utils.page.click(f"{element_message}[1]/td[5]")
            self.utils.page.wait_for_page_loaded()
            self.utils.page.wait_for_element_ready(elm_demo.lbl_important)
            is_important = self.utils.page.get_element(elm_demo.chk_important).is_checked()
            if data["message"]["important"] == "Yes":
                self.utils.should_be_equal(is_important,True)
            else:
                self.utils.should_be_equal(is_important,False)
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_english).input_value(),data["message"]["english"])
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_indonesian).input_value(),data["message"]["indonesian"])
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_korean).input_value(),data["message"]["korean"])
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_thai).input_value(),data["message"]["thai"])
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_vietnamese).input_value(),data["message"]["vietnamese"])
            self.utils.should_be_equal(self.utils.page.get_element(elm_demo.txt_chinese).input_value(),data["message"]["chinese"])

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