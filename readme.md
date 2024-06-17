RUN ALLURE Allure:

run tests with : 
pytest -v -s --alluredir="./report"

check logs in directory of generated reports: 
allure serve "./report"