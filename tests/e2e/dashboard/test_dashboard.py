import allure
from playwright.sync_api import expect
from config.config import BASE_URL
from utils.data_factory import TodoFactory


@allure.feature("Dashboard")
@allure.story("Dashboard Page Display")
class TestDashboardPageDisplay:
    """Tests for dashboard page display and components visibility"""

    @allure.title("All dashboard components are visible")
    @allure.description("Verify that header, create todo form, and todo list are visible on dashboard")
    def test_dashboard_components_visible(self, dashboard_page):
        """Verify all main components are visible"""
        assert dashboard_page.header.is_visible(dashboard_page.header.search_input), "Header not visible"
        assert dashboard_page.create_todo.is_visible(dashboard_page.create_todo.title_input), "Create todo form not visible"
        assert dashboard_page.todo_list.is_visible(dashboard_page.todo_list.todo_items), "Todo list not visible"


@allure.feature("Dashboard")
@allure.story("Header Component")
class TestHeaderComponent:
    """Tests for header component functionality"""

    @allure.title("Search input is accessible")
    @allure.description("Verify that search input field is visible and accessible")
    def test_search_input_accessible(self, dashboard_page):
        """Verify search input is visible and can be interacted with"""
        dashboard_page.header._for_headewaitr()
        search_value = dashboard_page.header.get_search_value()
        assert search_value == "", "Search input should be empty initially"

    @allure.title("User can search todos")
    @allure.description("Verify that user can type in search field and search value is retained")
    def test_search_todo(self, dashboard_page):
        """Verify search functionality"""
        search_text = "Test Search"
        dashboard_page.header.search(search_text)
        result = dashboard_page.header.get_search_value()
        assert result == search_text, f"Search input should contain '{search_text}'"

    @allure.title("Clear search input")
    @allure.description("Verify that search input can be cleared")
    def test_clear_search(self, dashboard_page):
        """Verify clearing search input"""
        dashboard_page.header.search("Some text")
        dashboard_page.header.clear_search()
        result = dashboard_page.header.get_search_value()
        assert result == "", "Search input should be empty after clearing"

    @allure.title("Profile link is accessible")
    @allure.description("Verify that profile link is visible and clickable")
    def test_profile_link_visible(self, dashboard_page):
        """Verify profile link is accessible"""
        assert dashboard_page.header.is_visible(dashboard_page.header.profile_link), "Profile link should be visible"

    @allure.title("Logout button is accessible")
    @allure.description("Verify that logout button is visible")
    def test_logout_button_visible(self, dashboard_page):
        """Verify logout button is visible"""
        assert dashboard_page.header.is_visible(dashboard_page.header.logout_button), "Logout button should be visible"


@allure.feature("Dashboard")
@allure.story("Create Todo Component")
class TestCreateTodoComponent:
    """Tests for creating new todos"""

    @allure.title("Create todo form fields are visible")
    @allure.description("Verify that all form fields for creating todo are visible")
    def test_create_todo_form_fields_visible(self, dashboard_page):
        """Verify all form fields are visible"""
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.title_input), "Title input not visible"
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.description_input), "Description input not visible"
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.date_input), "Date input not visible"
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.time_input), "Time input not visible"
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.submit_button), "Submit button not visible"
        assert dashboard_page.create_todo.is_visible(
            dashboard_page.create_todo.reset_button), "Reset button not visible"

    @allure.title("Fill individual form fields")
    @allure.description("Verify that each form field can be filled independently")
    def test_fill_individual_fields(self, dashboard_page):
        """Verify filling individual form fields"""
        dashboard_page.create_todo.fill_title("Test Title")
        dashboard_page.create_todo.fill_description("Test Description")

        title_value = dashboard_page.page.locator(dashboard_page.create_todo.title_input).input_value()
        description_value = dashboard_page.page.locator(dashboard_page.create_todo.description_input).input_value()

        assert title_value == "Test Title", "Title field should contain 'Test Title'"
        assert description_value == "Test Description", "Description field should contain 'Test Description'"

    @allure.title("Reset form clears all fields")
    @allure.description("Verify that reset button clears all form fields")
    def test_reset_form_clears_fields(self, dashboard_page):
        """Verify form reset clears all fields"""
        # Fill form
        dashboard_page.create_todo.fill_title("Test Title")
        dashboard_page.create_todo.fill_description("Test Description")

        # Reset form
        dashboard_page.create_todo.reset()

        # Verify fields are empty
        title_value = dashboard_page.page.locator(dashboard_page.create_todo.title_input).input_value()
        description_value = dashboard_page.page.locator(dashboard_page.create_todo.description_input).input_value()

        assert title_value == "", "Title field should be empty after reset"
        assert description_value == "", "Description field should be empty after reset"

    @allure.title("Create simple todo with required fields")
    @allure.description("Create a todo with title, date and time")
    def test_create_simple_todo(self, dashboard_page):
        """Verify creating a simple todo"""
        todo_data = TodoFactory.create_todo_minimal()

        dashboard_page.create_todo.create_todo(
            title=todo_data["title"],
            date=todo_data["date"],
            time=todo_data["time"]
        )

        # Verify todo was created
        assert dashboard_page.todo_list.todo_exists(todo_data["title"]), "Todo should exist after creation"

    @allure.title("Create todo with description")
    @allure.description("Create a todo with title, description, date and time")
    def test_create_todo_with_description(self, dashboard_page):
        """Verify creating todo with description"""
        todo_data = TodoFactory.create_todo()

        dashboard_page.create_todo.create_todo(
            title=todo_data["title"],
            description=todo_data["description"],
            date=todo_data["date"],
            time=todo_data["time"],
        )

        # Verify todo was created
        assert dashboard_page.todo_list.todo_exists(todo_data["title"]), "Todo with description should exist after creation"


@allure.feature("Dashboard")
@allure.story("Todo List Component")
class TestTodoListComponent:
    """Tests for todo list display and interaction"""

    @allure.title("Get todo list count")
    @allure.description("Verify that todo list count can be retrieved")
    def test_get_todo_count(self, dashboard_page):
        """Verify getting todo count"""
        count = dashboard_page.todo_list.get_todo_count()
        assert isinstance(count, int), "Todo count should be an integer"
        assert count >= 0, "Todo count should not be negative"

    @allure.title("Get all todo titles")
    @allure.description("Verify that all todo titles can be retrieved")
    def test_get_todo_titles(self, dashboard_page):
        """Verify getting all todo titles"""
        titles = dashboard_page.todo_list.get_todo_titles()
        assert isinstance(titles, list), "Todo titles should be a list"
        # Even if empty, it should be a valid list
        assert titles is not None, "Todo titles should not be None"

        """Verify getting all todo dates"""
        dates = dashboard_page.todo_list.get_todo_dates()
        assert isinstance(dates, list), "Todo dates should be a list"

        """Verify getting all todo times"""
        times = dashboard_page.todo_list.get_todo_times()
        assert isinstance(times, list), "Todo times should be a list"

    @allure.title("Get todo by index")
    @allure.description("Verify that todo can be retrieved by its index")
    def test_get_todo_by_index(self, dashboard_page):
        """Verify getting todo by index"""
        todo_data = TodoFactory.create_todo_minimal()

        # Create a todo
        dashboard_page.create_todo.create_todo(
            title=todo_data["title"],
            date=todo_data["date"],
            time=todo_data["time"]
        )

        # Get first todo (most recently created should be first or visible)
        first_todo = dashboard_page.todo_list.get_todo_by_index(0)
        assert first_todo is not None, "Should be able to get todo by index"
        assert isinstance(first_todo, str), "Todo should be a string"


@allure.feature("Dashboard")
@allure.story("Dashboard Integration")
class TestDashboardIntegration:
    """Integration tests for dashboard functionality"""

    @allure.title("Create multiple todos and verify they appear in list")
    @allure.description("Create multiple todos and verify all are displayed in the list")
    def test_create_and_display_multiple_todos(self, dashboard_page):
        """Verify creating and displaying multiple todos"""
        todos = TodoFactory.create_multiple_todos(count=2)

        for todo in todos:
            dashboard_page.create_todo.create_todo(
                title=todo["title"],
                date=todo["date"],
                time=todo["time"],
                description=todo["description"]
            )

        # Verify all todos exist in the list
        for todo in todos:
            assert dashboard_page.todo_list.todo_exists(todo["title"]), f"Todo '{todo['title']}' should exist in list"

    @allure.title("Create todo and search for it")
    @allure.description("Create a todo and then search for it using the search feature")
    def test_create_todo_and_search(self, dashboard_page):
        """Verify creating todo and then searching for it"""
        todo_data = TodoFactory.create_todo_with_custom_title("Unique Test Todo Search")

        # Create todo
        dashboard_page.create_todo.create_todo(
            title=todo_data["title"],
            date=todo_data["date"],
            time=todo_data["time"]
        )

        # Search for todo
        dashboard_page.header.search(todo_data["title"])

        # Wait for search results
        dashboard_page.page.wait_for_load_state("networkidle")

        # Verify todo still exists (search should filter or show it)
        assert dashboard_page.todo_list.todo_exists(todo_data["title"]), "Todo should be found in search"

    @allure.title("Form fields maintain fluent interface")
    @allure.description("Verify that component methods support method chaining")
    def test_fluent_interface(self, dashboard_page):
        """Verify fluent interface works"""
        todo_data = TodoFactory.create_todo()

        # Test method chaining
        result = dashboard_page.create_todo.fill_title(todo_data["title"]).fill_description(todo_data["description"])
        assert result is not None, "Methods should support chaining"