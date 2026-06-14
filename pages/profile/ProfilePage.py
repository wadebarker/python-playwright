from pages.BasePage import BasePage
from config.config import BASE_URL

class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.wrapper = ".Personal_wrapper__osRLL"
        self.form = f"{self.wrapper} .Personal_form__ll2V6"
        
        self.surname_input = f"{self.form} input[name='surname']"
        self.name_input = f"{self.form} input[name='name']"
        self.patronymic_input = f"{self.form} input[name='patronymic']"
        self.dob_input = f"{self.form} input[name='dateOfBirth']"
        self.sex_button = f"{self.form} button[name='sex']"
        self.phone_input = f"{self.form} input[name='phone']"
        self.save_button = f"{self.form} button[type='submit']"

    def open(self):
        self.goto(f"{BASE_URL}/profile")

    def fill_form(self, surname=None, name=None, patronymic=None, dob=None, phone=None, sex=None):
        if surname:
            self.page.fill(self.surname_input, surname)
        if name:
            self.page.fill(self.name_input, name)
        if patronymic:
            self.page.fill(self.patronymic_input, patronymic)
        if dob:
            self.page.fill(self.dob_input, dob)
        if phone:
            self.page.fill(self.phone_input, phone)
        if sex:
            self.page.click(self.sex_button)

    def submit(self):
        self.page.click(self.save_button)
