from datetime import datetime, timedelta

# Валидные тестовые данные пользователя для сохранения
def get_valid_data():
    return {
        "surname": "Иванов",
        "name": "Иван",
        "patronymic": "Иванович",
        "dateOfBirth": "2000-01-01",
        "sex": "m",
        "phone": "+7 (999) 123-45-67"
    }

INVALID_DATA = [
    # для полей surname/name/patronymic проверим мин/макс значения (анализ граничных значений)
    {
        "field": "surname",
        "value": "А",
        "description": "Too short"
    }, {
        "field": "surname",
        "value": "А" * 51,
        "description": "Too long"
    }, {
        "field": "name",
        "value": "А",
        "description": "Too short"
    }, {
        "field": "name",
        "value": "А" * 51,
        "description": "Too long"
    }, {
        "field": "patronymic",
        "value": "А",
        "description": "Too short"
    }, {
        "field": "patronymic",
        "value": "А" * 51,
        "description": "Too long"
    }, {
        "field": "sex",
        "value": "x",
        "description": "Invalid sex"
    }, {
        "field": "phone",
        "value": "89991234567",
        "description": "Invalid phone format"
    }, {
        "field": "phone",
        "value": "+7 (999) 123-456",
        "description": "Incomplete phone"
    },
]
# Невалидные тестовые данные пользователя для сохранения

# Анализ граничных значений для даты рождения
today = datetime.now()
future_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")
too_old_date = (today - timedelta(days=365 * 105)).strftime("%Y-%m-%d")
valid_date = (today - timedelta(days=365 * 25)).strftime("%Y-%m-%d")

DATE_DATA = [
    {
        "value": future_date,
        "description": "Future date",
        "valid": False
    }, {"value": too_old_date,
        "description": "Too old date",
        "valid": False
    }, {
        "value": valid_date,
        "description": "Valid date",
        "valid": True
    }, {
        "value": today.strftime("%Y-%m-%d"),
        "description": "Today",
        "valid": True
    },
]
