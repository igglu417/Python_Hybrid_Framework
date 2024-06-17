from datetime import datetime

import pytest

# Use basetest to optimize the fixtures used in all the test cases
# This is markers. It is used to signify that the class will refer to the "setup_and_teardown" fixture
@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:

    @staticmethod
    def generate_email_with_timestamp():
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "doe"+time_stamp+"@gmail.com"

