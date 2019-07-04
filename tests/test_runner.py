import pytest
import find_country
from country import Country


@pytest.mark.unit
@pytest.mark.parametrize(
    "user_input, to_continue, value",
    [
        ("quit", False, "kill"),
        ("q", False, "kill"),
        ("exit", False, "kill"),
        ("", True, "empty input"),
        ("   ", True, "empty input"),
        ("@", True, "garbage input"),
        ("*", True, "garbage input"),
        ("!", True, "garbage input"),
        (">", True, "garbage input"),
    ],
)
def test_handlers(monkeypatch, user_input, to_continue, value):
    monkeypatch.setattr("builtins.input", lambda x: user_input)
    out = find_country.process(find_country.invalid_chars())
    assert out["continue"] is to_continue
    assert out["value"] == value


@pytest.mark.functional
@pytest.mark.parametrize(
    "user_input, to_continue, value",
    [
        (
            "us",
            True,
            Country(
                name="United States of America",
                capital="Washington, D.C.",
                alpha2Code="US",
                alpha3Code="USA",
            ),
        ),
        (
            "Côte d'Ivoire",
            True,
            Country(
                name="Côte d'Ivoire",
                capital="Yamoussoukro",
                alpha2Code="CI",
                alpha3Code="CIV",
            ),
        ),
        (
            "Tanzania, United Republic of",
            True,
            Country(
                name="Tanzania, United Republic of",
                capital="Dodoma",
                alpha2Code="TZ",
                alpha3Code="TZA",
            ),
        ),
        (
            "Virgin Islands (British)",
            True,
            Country(
                name="Virgin Islands (British)",
                capital="Road Town",
                alpha2Code="VG",
                alpha3Code="VGB",
            ),
        ),
        (
            "BLM",
            True,
            Country(
                name="Saint Barthélemy",
                capital="Gustavia",
                alpha2Code="BL",
                alpha3Code="BLM",
            ),
        ),
        ("578", True, "not found"),
        ("Divided states", True, "not found"),
    ],
)
def test_valid(monkeypatch, user_input, to_continue, value):
    monkeypatch.setattr("builtins.input", lambda x: user_input)
    out = find_country.process(find_country.invalid_chars())
    assert out["continue"] is to_continue
    assert out["value"] == value
