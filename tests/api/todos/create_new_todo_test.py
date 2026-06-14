# from faker import Faker
#
# fake = Faker()
#
#
# class TestTodosApiCreate:
#     def test_create_todo(self, authorized_api):
#         payload = {
#             "title": fake.sentence(nb_words=3),
#             "description": fake.text(max_nb_chars=200),
#             "date": fake.date(),
#             "time": fake.time(pattern="%H:%M"),
#             "checked": fake.boolean()
#         }
#
#         response = authorized_api.post("/api/todos/create", data=payload)
#         assert response.status == 201
#
#         body = response.json()
#         assert body["title"] == payload["title"]
#         assert body["description"] == payload["description"]
#         assert body["date"] == payload["date"]
#         assert body["time"] == payload["time"]
#         assert body["checked"] == payload["checked"]
#         assert "id" in body and body["id"] > 0
#         assert "userId" in body and body["userId"] > 0
