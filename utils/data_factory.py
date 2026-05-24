from faker import Faker
from datetime import datetime, timedelta

fake = Faker("ru_RU")


class LoginFactory:
    """Фабрика данных для логина"""
    @staticmethod
    def create_login():
        return {
            "email": fake.unique.email(),
            "password": fake.password(length=10)
        }


class RegistrationFactory:
    """Фабрика данных для регистрации"""
    @staticmethod
    def create_registration():
        password = fake.password(length=10)
        return {
            "email": fake.email(),
            "password": password,
            "confirm_password": password  # совпадает с password
        }

    @staticmethod
    def create_registration_with_mismatch():
        """Для негативного сценария, пароль не совпадает с confirm_password"""
        return {
            "email": fake.email(),
            "password": fake.password(length=10),
            "confirm_password": fake.password(length=10)
        }


class TodoFactory:
    """Фабрика данных для создания todo задач"""
    
    @staticmethod
    def create_todo(title_length=5, description_length=100, day_forward=1):
        """Создать простую todo задачу"""
        return {
            "title": fake.sentence(nb_words=title_length),
            "description": fake.text(max_nb_chars=description_length),
            "date": (datetime.now() + timedelta(days=day_forward)).strftime("%Y-%m-%d"),
            "time": "10:00"
        }

    @staticmethod
    def create_todo_with_custom_title(title):
        """Создать todo с определённым названием"""
        return {
            "title": title,
            "description": fake.text(max_nb_chars=100),
            "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "time": "10:00"
        }

    @staticmethod
    def create_multiple_todos(count=3):
        """Создать несколько todo задач"""
        return [TodoFactory.create_todo() for _ in range(count)]

    @staticmethod
    def create_todo_with_date(date_str):
        """Создать todo с определённой датой"""
        return {
            "title": fake.sentence(nb_words=5),
            "description": fake.text(max_nb_chars=100),
            "date": date_str,
            "time": "10:00"
        }

    @staticmethod
    def create_todo_minimal():
        """Создать минимальную todo (только название и дата)"""
        return {
            "title": fake.sentence(nb_words=3),
            "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "time": "09:00",
            "description": ""
        }

    @staticmethod
    def create_todo_with_long_title():
        """Создать todo с длинным названием"""
        return {
            "title": fake.sentence(nb_words=20),
            "description": fake.text(max_nb_chars=100),
            "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
            "time": "10:00"
        }