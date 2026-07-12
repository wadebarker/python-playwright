from abc import ABC, abstractmethod


# POM - page object model
# разделение бизнес логики теста и логики взаимодействия со страницей (UI)

# Базовый класс (инкапсуляция базовой навигации по странице и работе с браузером)

# ABC - ABstact Class - класс, от которого можно только наследоваться, но не создавать экземпляры
class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver


    def open(self, url):
        self.driver.get(url)
        return self


    # абстрактный метод - это метод, у которого нет реализации и она будет предоставлена в классах наследниках
    @abstractmethod
    def get_page_url(self):
        pass


class LoginPage(BasePage):
    # инкапсуляция локаторов
    EMAIL_INPUT = 'input[type="email"]'
    PASSWORD_INPUT = 'input[type="password"]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    RESET_BUTTON = 'button[type="reset"]'


    def get_page_url(self):
        return '/auth/login'


    def login(self, email, password):
        self.driver.find_element(self.EMAIL_INPUT).fill(email)
        self.driver.find_element(self.PASSWORD_INPUT).fill(password)
        self.driver.find_element(self.SUBMIT_BUTTON).click()
        return '...логика автотеста...'
