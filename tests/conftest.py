import pytest
# import Python_Testing.server
from Python_Testing.server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True    # For better error reports
    with app.test_client() as client:
        yield client


mock_clubs = [
    {
        "name": "Héraclès_Temple",
        "email": "heracles@heavylift.gr",
        "points": "12"
    },
    {
        "name": "Popeye_Loft",
        "email": "popeye@spinach.com",
        "points": "9"
    },
    {
        "name": "Serena_Queen",
        "email": "serena@queenace.us",
        "points": "14"
    },
    {
        "name": "TestClub",
        "email": "testclub@mysite.com",
        "points": "9"
    }
]
# mocker_clubs = [Club(**club) for club in mock_clubs]

mock_comps = [
        {
            "name": "Summer LiftTest",
            "date": "2023-04-20 15:00:00",
            "numberOfPlaces": "35"
        },
        {
            "name": "Canadian Lifter",
            "date": "2023-10-30 16:30:00",
            "numberOfPlaces": "9"
        },
        {
            "name": "Australian Lifter",
            "date": "2023-11-20 18:30:00",
            "numberOfPlaces": "11"
        }
    ]
