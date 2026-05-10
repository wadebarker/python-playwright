from pages.BasePage import BasePage


class CreateTodoComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.title_input = "input[name='title']"
        self.description_input = "textarea[name='description']"
        self.date_input = "#date-input-create"
        self.time_input = "#time-input-create-how"
        self.reset_button = "button[type='reset']"
        self.submit_button = "button[type='submit']"
        self.form_container = ".CreateTodo_create__form__"

    def wait_for_form(self, timeout=5000):
        self.page.locator(self.title_input).wait_for(state="visible", timeout=timeout)
        return self

    def fill_title(self, title):
        self.page.locator(self.title_input).fill(title)
        return self

    def fill_description(self, description):
        self.page.locator(self.description_input).fill(description)
        return self

    def fill_date(self, date):
        self.page.locator(self.date_input).fill(date)
        return self

    def fill_time(self, time):
        self.page.locator(self.time_input).fill(time)
        return self

    def submit(self):
        self.page.locator(self.submit_button).click()
        self.page.wait_for_load_state("networkidle")
        return self

    def reset(self):
        self.page.locator(self.reset_button).click()
        return self

    def create_todo(self, title, date, time, description=""):
        self.fill_title(title)
        if description:
            self.fill_description(description)
        self.fill_date(date)
        self.fill_time(time)
        self.submit()
        return self
