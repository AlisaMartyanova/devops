import pytest
from app_python.app import app
# from flaskr import create_app

"""Initialize the testing environment

Creates an app for testing that has the configuration flag ``TESTING`` set to
``True``.

"""

@pytest.fixture
def client():
    """Configures the app for testing

    Sets app config variable ``TESTING`` to ``True``

    :return: App for testing
    """
    # app = create_app()
    #app.config['TESTING'] = True
    client = app.test_client()

    yield client