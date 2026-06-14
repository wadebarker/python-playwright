from playwright.sync_api import expect

class TestProfile:
    def test_profile_fields_visible(self, profile_page):
        profile_page.open()
        
        # Страница Профиль-Личная инмофрмация загружается и на ней в форме видны все элементы
        expect(profile_page.page.locator(profile_page.surname_input)).to_be_visible()
        expect(profile_page.page.locator(profile_page.name_input)).to_be_visible()
        expect(profile_page.page.locator(profile_page.patronymic_input)).to_be_visible()
        expect(profile_page.page.locator(profile_page.dob_input)).to_be_visible()
        expect(profile_page.page.locator(profile_page.sex_button)).toы_be_visible()
        expect(profile_page.page.locator(profile_page.phone_input)).to_be_visible()
        expect(profile_page.page.locator(profile_page.save_button)).to_be_visible()
