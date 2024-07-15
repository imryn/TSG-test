from common.http_client import HttpClient

class CountryService(HttpClient):

    def __init__(self, countries_url):
        self.countries_url = countries_url

    def get_all_countries(self):
        response = self.get(f"{self.countries_url}/all")
        return response

    def get_country_by_name(self, country_name):
        response = self.get(f"{self.countries_url}/name/{country_name}")
        return response

    def get_a_country_by_code(self, code):
        response = self.get(f"{self.countries_url}/alpha/{code}")
        return response

    def get_countries_on_region(self, region_value):
        response = self.get(f"{self.countries_url}/region/{region_value}")
        return response