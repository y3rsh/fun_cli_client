from dataclasses import dataclass


@dataclass
class Country:
    name: str
    capital: str
    alpha2Code: str
    alpha3Code: str
