class TestTodosApiGet:
    def test_get_todos_list(self, authorized_api):
        response = authorized_api.get("/api/todos")
        assert response.status == 200

        data = response.json()
        assert isinstance(data, list)