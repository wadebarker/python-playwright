from enum import Enum

import pytest


# Factory / Фабрика / Фарбичные методы
# используется для упраления конфигурациями, подключениями к БД (на разных стендах - разные креды)
# dev, stage, prod

# enum - enumerate - перечисления
class Environment(Enum):
    DEV = 'dev'
    STAGE = 'stage'
    PROD = 'prod'


class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token


class APIClientFactory:
    # словарь с конфигурациями для разных окружений
    config = {
        Environment.DEV: {
            'url': 'https://company-dev.com',
            'token': 'dev-token',
        },
        Environment.STAGE: {
            'url': 'https://company-stage.com',
            'token': 'stage-token',
        },
        Environment.PROD: {
            'url': 'https://company.com',
            'token': 'prod-token',
        }
    }

    @classmethod
    def create_client(cls, env: Environment) -> APIClient:
        configuration = cls.config.get(env)
        if not configuration:
            raise ValueError('Неподдерживаемое окружение')
        return APIClient(base_url=configuration['url'], token=configuration['token'])


# создание фикстур для каждого окружения в файле conftest
@pytest.fixture
def dev_api_client():
    return APIClientFactory.create_client(Environment.DEV)


@pytest.fixture
def stage_api_client():
    return APIClientFactory.create_client(Environment.STAGE)


@pytest.fixture
def prod_api_client():
    return APIClientFactory.create_client(Environment.PROD)


# пример использования в автотесте
def test_get_orders(dev_api_client):
    # пример с использование библиотеки requests/
    response = dev_api_client.get('/orders')
    assert response.status_code == 20