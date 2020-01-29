import pytest
from searcher.app import create_app


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope='session')
def db_engine(app):
    """
    Setup the database for a test session and drop all tables after the
    session ends. It is not intended to be used on tests functions,
    use `db_session` instead.
    """
    pass


@pytest.fixture()
def db_session(app, db_engine, request):
    """
    Creates a new database transaction for the test and roll it back
    when the test is completed
    """
    pass
