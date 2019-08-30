import requests

HEADERS = {"Accept": "application/json", "Content-type": "application/json"}


class CountryClient:
    def __init__(self):
        self.base_url = "https://restcountries.eu/rest/v2"
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    def get_by_name(self, name: str):
        endpoint = f"{self.base_url}/name/{name}?fullText=true"
        return self.session.get(endpoint, timeout=5)

    def get_by_code(self, code: str):
        endpoint = f"{self.base_url}/alpha/{code}"
        return self.session.get(endpoint, timeout=5)
