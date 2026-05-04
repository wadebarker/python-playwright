class TestDashboard:
    def test_dashboard_components_visible(self, dashboard_page):
        assert dashboard_page.header.is_visible(dashboard_page.header.search_input), "Header не виден"
        assert dashboard_page.create_todo.is_visible(dashboard_page.create_todo.title_input), "Форма создания задачи не видна"
        assert dashboard_page.todo_list.is_visible(dashboard_page.todo_list.todo_items), "Список задач не виден"