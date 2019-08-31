from invoke import task


@task
def black(c):
    """
        Run black
    """
    c.run("""find . | grep -E "(\.py$)" | xargs black""")  # noqa: W605


@task
def make_req(c):
    """
        Update requirements.txt
    """
    c.run("""pipenv run pip freeze > requirements.txt""")  # noqa: W605
