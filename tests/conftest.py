import pytest
# import Python_Testing.server
from Python_Testing.server import app

@pytest.fixture
def client():    
    app.config["TESTING"] = True
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
            "date": "2023-10-15 16:30:00",
            "numberOfPlaces": "9"
        },
        {
            "name": "Australian Lifter",
            "date": "2023-11-20 18:30:00",
            "numberOfPlaces": "11"
        }
    ]
"""
mocker_comps = [Competition(**comp) for comp in mock_comps]

mocker_data = Data(None, None)
mocker_data.clubs = [Club(**club) for club in mock_clubs]
mocker_data.competitions = [Competition(**comp) for comp in mock_comps]


@pytest.fixture
def app(mocker):
    mocker.patch.object(server, "COMPETITIONS", test_comp())
    mocker.patch.object(server, "CLUBS", test_club())
    return create_app({"TESTING": True})


@pytest.fixture
def loadLocalClubJson():
    w_dir = os.path.abspath('.')
    if os.path.isfile(os.path.join(w_dir)):
        print('os.path')
        print(w_dir)
        return os.path
"""