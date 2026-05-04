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

    def create_todo(self, title, date, time, description=""):
        self.page.locator(self.title_input).fill(title)
        if description:
            self.page.locator(self.description_input).fill(description)
        self.page.locator(self.date_input).fill(date)
        self.page.locator(self.time_input).fill(time)
        self.page.locator(self.submit_button).click()
