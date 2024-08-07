import pytest

''' send get request in order to get data on all countries '''
def test_retrive_all_countries(get_countries_service):
        get_countries = get_countries_service.get_all_countries()
        assert get_countries['statusCode'] == 200, f"countries was not return. look at {get_countries}"
        get_countries_response = get_countries['response']
        countries_without_data = []
        for country in get_countries_response:
            if len(country['name']) == 0 or len(country['translations']) == 0 or len(country['region']) == 0:
                countries_without_data.append(country)

        if len(countries_without_data)!=0:
            raise Exception(f"missing data for one of the countries. look at {countries_without_data}")