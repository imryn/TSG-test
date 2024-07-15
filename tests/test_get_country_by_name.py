import pytest
from common.global_enum import GlobalEnum

''' send valid country name and get data on it '''
def test_get_country_by_its_name(get_countries_service):
    country_data = get_countries_service.get_country_by_name(GlobalEnum.DEFAULT_COUNTRY_NAME.value)
    assert country_data['statusCode'] == 200, f"country was not return. look at {country_data}"

    country_response = country_data['response']
    for country in country_response:
        assert len(country['name']['common']) != 0, f"wrong common value. look at {country}"
        assert len(country['altSpellings']) != 0 , f"the country does not have altSpellings. look at {country}"\
                                                   f"look at {country}."
        assert len(country['translations']) != 0, f"the country does not have translations. look at {country}."

''' send invalid country name and check you get correct error '''
@pytest.mark.parametrize("country_name", ["FRankfvdsfsds", None, "undefined", 0, "french4454"])
def test_get_country_with_invalid_country_name(get_countries_service, country_name):
    country = get_countries_service.get_country_by_name(country_name)

    assert country['statusCode'] == 404, f"country return or get another status code. or wrong status. {country}"
    country_response = country['response']
    assert country_response['message'] == 'Not Found', f"wrong error message. or no message at all. look at {country}"

    fdfd