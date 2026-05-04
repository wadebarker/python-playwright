from faker import Faker

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