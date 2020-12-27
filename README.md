# Centime

1- To run the test use below command from project directory 
    pytest -v --html=daily_report.html
    pytest --html=daily_report.html 

2- For allure reporting run the below command from project directory
    pytest --alluredir="Allure_report" ./test_dailyapi.py
    allure serve "Allure_report"

