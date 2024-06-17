import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from Utilities import ReadConfigurations



@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test_case",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

# ue this set and teardown as a centralized unit to be used in every browser invocation
@pytest.fixture()
def setup_and_teardown(request):
    global driver
    driver = None
    try:
        select_browser = ReadConfigurations.read_configuration("basic", "browser")
        if select_browser.__eq__("chrome"):
            driver = webdriver.Chrome()
        elif select_browser.__eq__("edge"):
            driver = webdriver.Edge()
        elif select_browser.__eq__("firefox"):
            driver = webdriver.Firefox()
        else:
            print("Select either chrome, edge or firefox.")
    except:
        print("Error in invoking web browser")
    driver.maximize_window()
    test_url = ReadConfigurations.read_configuration("basic", "url")
    driver.get(test_url)
    request.cls.driver = driver  # use request to use driver on cls(class) level
    yield
    driver.quit()
