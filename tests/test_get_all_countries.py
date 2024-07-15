import pytest

''' send get request in order to get data on all countries '''
def test_retrive_all_countries(get_countries_service):
        get_countries = get_countries_service.get_all_countries()
        assert get_countries['statusCode'] == 200, f"countries was not return. look at {get_countries}"
        get_countries_response = get_countries['response']

        for country in get_countries_response:
            assert len(country['name']) != 0, f"the country does not have native name. {country}"
            assert len(country['translations']) != 0, f"the country does not have translations. {country}"
            assert len(country['region']) != 0, f"the country does not have region. {country}"