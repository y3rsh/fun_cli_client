# find country

## Setup

1. Have Python 3
    - pyenv suggested
1. Have latest pip
    - `pip install -U pip`
1. Have pipenv
    - `pip install -U pipenv`
1. Install the dependencies.  Let pipenv handle the virtual environment
    - `pipenv install`
    - To activate this project's virtualenv, run `pipenv shell`
    - Run a command inside the virtualenv with `pipenv run`

## linting and formatting

```shell
pipenv run invoke black
pipenv run flake8
```

## run the code

```shell
pipenv run python find_country.py
```

## run the tests

```shell
pipenv run pytest
```

## Things not addressed

- the set of special characters to reject is not completely vetted
- I am not preventing emoji input
- not handling interrupts or EOF
- performance - if had more time I would probably do an async call to the api for both code and name at the same time
- with more time I would mock the http layer with a tool like httpretty so I could have unit tests of the controller and data mapping layers
  - this would be especially important there were any complexity in mapping the api response to objects
- I would add pytest-cov and pytest-html for coverage and pretty html test reports
