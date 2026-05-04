from utils.data_factory import RegistrationFactory

NEGATIVE_REGISTER_CASES = [
    {
        "title": "Поле ввода почты не заполнено",
        "email": "",
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": RegistrationFactory.create_registration()["confirm_password"],
        "error_message": "Почта - обязательное поле",
    },
    {
        "title": "Поле ввода пароля не заполнено",
        "email": RegistrationFactory.create_registration()["email"],
        "password": "",
        "confirm_password": RegistrationFactory.create_registration()["confirm_password"],
        "error_message": "Пароль - обязательное поле",
    },
    {
        "title": "Поле ввода подтверждения пароля не заполнено",
        "email": RegistrationFactory.create_registration()["email"],
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": "",
        "error_message": "Повторите пароль",
    },
    {
        "title": "Невалидный email",
        "email": "invalid_email",
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": RegistrationFactory.create_registration()["password"],
        "error_message": "Введите правильную почту",
    },
    # Проверка длины email
    {
        "title": "Email слишком короткий",
        "email": RegistrationFactory.create_registration()["email"][:5],
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": RegistrationFactory.create_registration()["password"],
        "error_message": "Введите правильную почту",
    },
    {
        "title": "Email слишком длинный",
        "email": RegistrationFactory.create_registration()["email"] + "x" * 50,
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": RegistrationFactory.create_registration()["password"],
        "error_message": "Максимум 50 символов",
    },
    # Проверка длины пароля
    {
        "title": "Пароль слишком короткий",
        "email": RegistrationFactory.create_registration()["email"],
        "password": RegistrationFactory.create_registration()["password"][:5],
        "confirm_password": RegistrationFactory.create_registration()["password"][:5],
        "error_message": "Минимум 6 символов",
    },
    {
        "title": "Пароль слишком длинный",
        "email": RegistrationFactory.create_registration()["email"],
        "password": RegistrationFactory.create_registration()["password"] + "x" * 50,
        "confirm_password": RegistrationFactory.create_registration()["password"],
        "error_message": "Максимум 50 символов",
    },
    # Несовпадение пароля и подтверждения
    {
        "title": "Пароль и подтверждение не совпадают",
        "email": RegistrationFactory.create_registration()["email"],
        "password": RegistrationFactory.create_registration()["password"],
        "confirm_password": RegistrationFactory.create_registration_with_mismatch()["confirm_password"],
        "error_message": "Пароли не совпадают",
    }
]