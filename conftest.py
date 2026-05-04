import pytest
import allure
from playwright.sync_api import sync_playwright, Playwright


from pages.LoginPage import LoginPage
from pages.profile.ProfileAuthPage import ProfileAuthPage
from pages.RegisterPage import RegisterPage
from pages.DashboardPage import DashboardPage
from config.config import API_BASE_URL, loginCredentials


@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


# Фикстура page автоматически создаст новую вкладку браузера и закроет её после теста
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="function")
def login_page(page):
    lp = LoginPage(page)
    yield lp


@pytest.fixture(scope="function")
def register_page(page):
    rp = RegisterPage(page)
    yield rp


# Фикстура авторизации
@pytest.fixture
def authorized_page(page):
    login_page = LoginPage(page)
    login_page.login(loginCredentials["email"], loginCredentials["password"])
    page.locator(".Todos_wrapper__TUagW").wait_for(state="visible", timeout=5000)
    return page


# Фикстура для DashboardPage
@pytest.fixture
def dashboard_page(authorized_page):
    return DashboardPage(authorized_page)


@pytest.fixture
def profile_auth_page(authorized_page):
    return ProfileAuthPage(authorized_page)


# Фикстура для добавления скриншотов
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # запускаем только на setup и call стадиях
    if report.when in ("setup", "call"):

        # проверяем есть ли фикстура page
        page = None
        if "page" in item.funcargs:
            page = item.funcargs["page"]

        if page is None:
            return

        # Скриншот при успехе + при падении
        if report.failed or report.when == "call":
            try:
                screenshot = page.screenshot()
                allure.attach(
                    screenshot,
                    name=f"screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass


# Фикстуры для тестирования API

# api_context — создаёт API контекст Playwright
@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(base_url=API_BASE_URL)
    yield context
    context.dispose()


# access_token — получает токен через логин
@pytest.fixture(scope="session")
def access_token(api_context):
    response = api_context.post(
        "/api/auth/login",
        data=loginCredentials
    )

    body = response.json()
    token = body.get("accessToken")
    if not token:
        pytest.fail(f"Не удалось получить accessToken из ответа login API: {body}")
    return token


# Фикстура, создающая API-контекст с заголовком Authorization:
@pytest.fixture(scope="session")
def authorized_api(playwright: Playwright, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    context = playwright.request.new_context(base_url=API_BASE_URL, extra_http_headers=headers)
    yield context
    context.dispose()

