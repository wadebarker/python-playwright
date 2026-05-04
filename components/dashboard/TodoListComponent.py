from pages.BasePage import BasePage


class TodoListComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        #
        self.todo_items = ".mt-2\\.5" # экранирую 5
        self.todo_title_locator = ".TodoItem_content__J_7bo"
        self.todo_time_locator = ".TodoItem_time__WctFj"
        self.todo_date_locator = ".TodoItem_title__6L8Cp"

    def get_todo_titles(self):
        return self.page.locator(self.todo_title_locator).all_inner_texts()

    def get_todo_dates(self):
        return self.page.locator(self.todo_date_locator).all_inner_texts()

    def get_todo_times(self):
        return self.page.locator(self.todo_time_locator).all_inner_texts()

    def todo_exists(self, title):
        return title in self.get_todo_titles()
