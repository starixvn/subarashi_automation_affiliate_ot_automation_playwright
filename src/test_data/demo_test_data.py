from datetime import datetime

class DemoTestData:
    test_data = {
        "creator": "AAVictor",
        "07/01/2025 06:12:02": "123456",
        "message": "test213",
        "important": "Yes",
        "updated_by": "AAVictor",
        "updated_date": "07/01/2025 06:12:39",
    }
    # API request templates
    api_templates = {
        "create_message": {
            "method": "POST",
            "headers": {"content-type": "application/json"},
            "body": {
                "message": "test message",
                "priority": "high",
                "recipient": "all"
            }
        }
    }
    # Headers templates
    REQUIRED_HEADERS = {
        "content-type": "application/json;charset=UTF-8",
        "accept": "application/json, text/plain, */*"
    }

    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    @classmethod
    def get_test_data(cls, scenario="default"):
        base_data = {
            "creator": "AAVictor",
            "created_date": cls.get_current_timestamp(),
            "message": "test message"
        }
        scenarios = {
            "urgent": {**base_data, "priority": "urgent", "important": "Yes"},
            "normal": {**base_data, "priority": "normal", "important": "No"}
        }
        return scenarios.get(scenario, base_data)