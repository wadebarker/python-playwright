from config.config import loginCredentials


class TestLoginApi:
    def test_login_returns_user(self, api_context):
        response = api_context.post(
            "/api/auth/login",
            data=loginCredentials
        )
        assert response.status == 200

        body = response.json()
        assert body["user"]["email"] == loginCredentials["email"]
        assert body["user"]["id"] > 0
