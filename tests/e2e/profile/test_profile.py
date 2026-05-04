from config.config import BASE_URL
from playwright.sync_api import expect


class TestProfile:
    def test_open_profile_from_dashboard_header(self, dashboard_page):
        dashboard_page.header.open_profile()
        expect(dashboard_page.page).to_have_url(f"{BASE_URL}/profile")