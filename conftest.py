import pytest
from services.country_service import CountryService
from common.enviroment_settings import EnvironmentSettings

@pytest.fixture(scope="session")
def env_vars():
    return EnvironmentSettings().get_env_variable_dict()

@pytest.fixture(scope="session")
def get_countries_service(env_vars):
    countries = CountryService(countries_url=env_vars['BASE_URL'])
    return countries