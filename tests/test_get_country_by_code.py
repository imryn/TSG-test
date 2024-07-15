import pytest
from common.global_enum import GlobalEnum

''' send code represnt a country and get data on it '''
@pytest.mark.parametrize('country_code',["PF","258","PYF"])
def test_retrive_country_by_code(get_countries_service, country_code):
    country_data = get_countries_service.get_a_country_by_code(country_code)

    assert country_data['statusCode'] == 200 , f"country was not return. look at {country_data}"

    country_response = country_data['response']
    for item in country_response:
        assert item['name']['common'] == GlobalEnum.COUNTRY_NAME_COMMON.value, f"wrong name.common value. " \
                                                                               f"look at {country_response}"
        if len(item['altSpellings']) != 0:
            for alt, alt_spel_in_response in zip(GlobalEnum.COUNTRY_ALT_SPEELING.value, item['altSpellings']):
                assert alt == alt_spel_in_response, f"one of the alt spellings does not exist. {country_response}"
        else:
            raise Exception(f"no altSpellings. look at {country_response}")

        assert item['languages']["fra"] == GlobalEnum.DEFAULT_COUNTRY_NAME.value, f"another languages value or not exist." \
                                                                                     f"look at {country_response}"

''' send invalid code and check you get an error '''
@pytest.mark.parametrize('country_code',["KING", None, "undefined", 0, "kjfdklsj633", 167.4])
def test_send_invalid_code_and_do_not_get_country(get_countries_service, country_code):
    country_data = get_countries_service.get_a_country_by_code(country_code)
    assert country_data['statusCode'] == 400 , f"country was return or wrong status code. look at {country_data}"

    conutry_response = country_data['response']
    assert conutry_response['message'] == "Bad Request", f"wrong error message. or no message at all. {conutry_response}"