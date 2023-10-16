from bs4 import BeautifulSoup
import unittest

from unittest.mock import patch
from Python_Testing import server
from Python_Testing.server import loadClubs, clubs, competitions
from Python_Testing.tests.conftest import mock_clubs, mock_comps

from Python_Testing.server import loadCompetitions


# ============ Logging ==============

def test_index_email_ok(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert "Welcome to the GUDLFT Registration Portal!" in data


def test_index_email_wrong(client):
    email = "unknown@email.com"
    response = client.post("/showSummary", data={"email": email})
    assert response.status_code == 200
    data = response.data.decode()
    assert "Wrong Email Try again" in data


def test_logout_page(client):
    response = client.get('/logout', follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in data


# ================== Test load fct =====================

class TestLoadClubs(unittest.TestCase):

    @patch('Python_Testing.server.loadClubs')
    def test_load_clubs_response(self, mock_loadClubs):

        mock_loadClubs.return_value = mock_clubs
        self.assertEqual(loadClubs(), clubs)


class TestLoadCompetitions(unittest.TestCase):
    @patch('Python_Testing.server.loadCompetitions')
    def test_load_competitions_response(self, mock_loadCompetitions):
        mock_loadCompetitions.return_value = mock_comps
        self.assertEqual(loadCompetitions(), competitions)


# =============== Test access pages ==================
def test_book_page_access_function(client, mocker):

    mocker.patch.object(server, "clubs", mock_clubs)

    # email = "heracles@heavylift.gr"
    email = mock_clubs[0]['email']

    response = client.post("/showSummary", data={"email": email})

    data = response.data.decode()
    assert response.status_code == 200

    soup = BeautifulSoup(data, "html.parser")
    assert soup.h2.get_text() == 'Welcome,' + ' ' + email + ' '


def test_purchase_page_access_function(client, mocker):
    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[0]['name']
    comp_name = mock_comps[0]['name']
    response = client.get('/book/' + comp_name + '/' + club_name)

    assert response.status_code == 200
    data = response.data.decode()
    # print('data:', data)

    soup = BeautifulSoup(data, "html.parser")
    print('soupe:', soup.h2.get_text)
    assert soup.h2.get_text() == 'Welcome,  '


# ==== test booking messages of usage of points and places ====
def test_over_booked_places(client, mocker):
    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[0]['name']
    comp_name = mock_comps[2]['name']
    mock_places = int(mock_comps[2]['numberOfPlaces'])

    placesRequired = 12

    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": comp_name,
        "places": placesRequired})
    assert response.status_code == 200

    data = response.data.decode()
    print('Places disponibles:', mock_places)
    print('booked:', placesRequired)

    if int(placesRequired) > mock_places:
        assert "Not enough places ! Retry." in data
    else:
        assert "Great-booking complete!" in data


def test_over_loaded_points(client, mocker):
    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[2]['name']
    comp_name = mock_comps[0]['name']
    mock_points = int(mock_clubs[2]['points'])

    placesRequired = 15

    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": comp_name,
        "places": placesRequired})
    assert response.status_code == 200

    data = response.data.decode()

    if int(placesRequired) > mock_points:
        print("Not enough points ! Retry.")
        # soup = BeautifulSoup(data, "html.parser")
        assert "Not enough points ! Retry." in data


def test_retry_points(client, mocker):

    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[0]['name']
    comp_name = mock_comps[0]['name']
    mock_points = mock_clubs[0]['points']
    print('mock_points:', mock_points)
    max_booking_places = 12
    placesRequired = 12

    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": comp_name,
        "places": placesRequired})
    assert response.status_code == 200

    data = response.data.decode()
    print('Points disponibles:', mock_points)
    print('booked:', placesRequired)

    if int(placesRequired) <= max_booking_places:
        assert "<li>Great-booking complete!</li>" in data
        assert "Points available: 0" in data


def test_over_limit_twelve_points(client, mocker):

    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[2]['name']
    comp_name = mock_comps[0]['name']
    mock_points = mock_clubs[2]['points']
    print('mock_points:', mock_points)
    max_booking_places = 12
    placesRequired = 13

    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": comp_name,
        "places": placesRequired})
    assert response.status_code == 200

    data = response.data.decode()
    print('Points disponibles:', mock_points)
    print('booked:', placesRequired)

    if int(placesRequired) >= max_booking_places:
        print('You can\'t book more than 12 places ! Retry.')
        soup = BeautifulSoup(data, "html.parser")
        assert soup.li.get_text() == "You can't book more than 12 places ! Retry."


# ================ Dates test ========================
def test_post_booking(client, mocker):

    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    club_name = mock_clubs[0]['name']
    comp_name = mock_comps[0]['name']

    response = client.get('/book/' + comp_name + '/' + club_name)

    assert response.status_code == 200
    data = response.data.decode()

    assert "You cannot book places on post-dated competitions !" in data


# ================= Dashboard test =======================

def test_dashboard_page(client, mocker):
    mocker.patch.object(server, "clubs", mock_clubs)
    response = client.get('/dashboard')
    data = response.data.decode()
    assert response.status_code == 200
    assert mock_clubs[1]['name'] in data
    assert mock_clubs[1]['points'] == '9'
    print('\n', 'Club name:', mock_clubs[0]['name'], 'points:', mock_clubs[0]['points'], '\n',
          'Club name:', mock_clubs[1]['name'], 'points:', mock_clubs[1]['points'])
