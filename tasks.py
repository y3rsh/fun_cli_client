from invoke import task


@task
def black(c):
    """
        Run black
    """
    c.run("""find . | grep -E "(\.py$)" | xargs black""")  # noqa: W605
