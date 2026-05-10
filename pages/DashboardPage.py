from pages.BasePage import BasePage
from config.config import BASE_URL
from components.dashboard.HeaderComponent import HeaderComponent
from components.dashboard.CreateTodoComponent import CreateTodoComponent
from components.dashboard.TodoListComponent import TodoListComponent


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header = HeaderComponent(self.page)
        self.create_todo = CreateTodoComponent(self.page)
        self.todo_list = TodoListComponent(self.page)
        self.dashboard_wrapper = ".Todos_wrapper__TUagW"

    def open(self):
        self.goto(f"{BASE_URL}/")
        self.wait_for_dashboard_load()
        return self

    def wait_for_dashboard_load(self, timeout=5000):
        self.page.locator(self.dashboard_wrapper).wait_for(state="visible", timeout=timeout)
        self.header.wait_for_header(timeout)
        self.create_todo.wait_for_form(timeout)
        self.todo_list.wait_for_todo_list(timeout)
        return self


