Для добавления Allure отчётов используем команду:
pip install allure-pytest

Для запуска тестов и формирования отчётов:
pytest --alluredir=allure-results 

Для просмотра отчётов:
allure serve allure-results