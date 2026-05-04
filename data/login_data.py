from config.config import loginCredentials
from utils.data_factory import LoginFactory


NEGATIVE_LOGIN_CASES = [
    {
        "title": "valid email wrong password",
        "email": loginCredentials["email"],  # используем валидный email из конфига
        "password": LoginFactory.create_login()["password"],  # генерируем случайный пароль
        "error": "Неверная почта или пароль",
    }, {
        "title": "non existing email",
        "email": LoginFactory.create_login()["email"],  # случайный email
        "password": loginCredentials["password"],  # правильный пароль из конфига
        "error": "Неверная почта или пароль",
    }, {
        "title": "invalid email format",
        "email": "invalid_email_format",
        "password": loginCredentials["password"],
        "error": "Введите правильную почту",
    }, {
        "title": "email too short",
        "email": LoginFactory.create_login()["email"][:5],  # берем первые 5 символов
        "password": loginCredentials["password"],
        "error": "Введите правильную почту",
    }, {
        "title": "email too long",
        "email": LoginFactory.create_login()["email"] + "x" * 50,  # делаем длиннее 50 символов
        "password": loginCredentials["password"],
        "error": "Максимум 50 символов",
    }, {
        "title": "empty email",
        "email": "",
        "password": loginCredentials["password"],
        "error": "Почта - обязательное поле",
    }, {
        "title": "empty password",
        "email": loginCredentials["email"],
        "password": "",
        "error": "Пароль - обязательное поле",
    }, {
        "title": "password too short",
        "email": loginCredentials["email"],
        "password": LoginFactory.create_login()["password"][:5],  # берем 5 символа для негативного теста
        "error": "Минимум 6 символов",
    }, {
        "title": "password too long",
        "email": loginCredentials["email"],
        "password": LoginFactory.create_login()["password"] + "x" * 50,  # делаем >50 символов
        "error": "Максимум 50 символов",
    }
]