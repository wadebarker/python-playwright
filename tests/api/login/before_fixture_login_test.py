import pytest
from config.config import API_BASE_URL, loginCredentials


@pytest.mark.skip(reason="Исторический пример без фикстур; оставлен как reference.")
class TestLoginApiWithoutFixtures:
    def test_login_api_before_fixture(self):
        # Тест намеренно пропущен: рабочие API-тесты используют фикстуры из conftest.py.
        assert API_BASE_URL
        assert loginCredentials["email"]
