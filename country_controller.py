import json
import requests
from country import Country
import country_client


class CountryController:
    def __init__(self):
        self.client = country_client.CountryClient()

    def process_response(self, response: requests.Response):
        # print(response.status_code)
        # print(response.text)
        if response.status_code > 200:
            return None
        if response.status_code == 200:
            country_json = json.loads(response.text)
            if len(country_json) == 1:
                country_json = country_json[0]
            return Country(
                country_json["name"],
                country_json["capital"],
                country_json["alpha2Code"],
                country_json["alpha3Code"],
            )

    def resolve_country(self, name_or_code: str):
        response = self.client.get_by_name(name_or_code)
        country_holder = self.process_response(response)
        if country_holder:
            # name was matched
            return country_holder
        else:
            response = self.client.get_by_code(name_or_code)
            return self.process_response(response)
