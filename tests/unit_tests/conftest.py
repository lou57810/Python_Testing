import pytest
# from Python_Testing.tests.unit_tests import clubs
# from Python_Testing.tests.unit_tests import competitions

from Python_Testing.server import app


@pytest.fixture
def client():    
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client