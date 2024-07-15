import pytest
from common.global_enum import GlobalEnum

''' send region to get request and make sure you get countries only related to the region '''
def test_get_countries_filtered_by_region(get_countries_service):
    countries_data = get_countries_service.get_countries_on_region(GlobalEnum.REGION.value)

    assert countries_data['statusCode'] == 200, f"do not get any countries. look at {countries_data}"

    countries_response = countries_data['response']

    for country in countries_response:
        assert country['region'].lower() == GlobalEnum.REGION.value, "one of the countries has deifferent region than" \
                                                                     f" filtered by the endpoint. {country}"

        assert len(country['name']['common']) != 0, f"one of the countries does not have name.common. look at {country}"

''' send invalid region and make sure you get an error '''
@pytest.mark.parametrize("region_value", ["TEST", "undefined", 0, None, 12.5])
def test_get_countries_related_to_invalid_region(get_countries_service, region_value):
    countries_data = get_countries_service.get_countries_on_region(region_value)
    assert countries_data['statusCode'] == 404, f"wrong status code. look at {countries_data}"

    countries_response = countries_data['response']
    assert countries_response['message'] == 'Not Found', f"wrong error message or not message at all. {countries_response}"

