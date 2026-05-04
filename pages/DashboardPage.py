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

    def open(self):
        self.goto(f"{BASE_URL}/")


