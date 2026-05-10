from pages.BasePage import BasePage


class TodoListComponent(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.todo_items = ".mt-2\\.5"  # Экранирование
        self.todo_title_locator = ".TodoItem_content__J_7bo"
        self.todo_time_locator = ".TodoItem_time__WctFj"
        self.todo_date_locator = ".TodoItem_title__6L8Cp"
        self.todo_item = ".TodoItem_item__"
        self.empty_list_message = ".empty_list_message"

    def wait_for_todo_list(self, timeout=5000):
        self.page.locator(self.todo_items).wait_for(state="visible", timeout=timeout)
        return self

    def get_todo_count(self):
        return self.page.locator(self.todo_title_locator).count()

    def get_todo_titles(self):
        return self.page.locator(self.todo_title_locator).all_inner_texts()

    def get_todo_dates(self):
        return self.page.locator(self.todo_date_locator).all_inner_texts()

    def get_todo_times(self):
        return self.page.locator(self.todo_time_locator).all_inner_texts()

    def todo_exists(self, title):
        return title in self.get_todo_titles()

    def get_todo_by_index(self, index):
        items = self.page.locator(self.todo_title_locator).all()
        if index < len(items):
            return items[index].inner_text()
        return None

    def is_empty(self):
        return self.get_todo_count() == 0
