import requests
import unittest
from .conftest import client
from unittest import mock, TestCase
from unittest.mock import patch, Mock
from Python_Testing import server
from Python_Testing.server import loadClubs
from Python_Testing.server import loadCompetitions


# constants
PATH_COMPETITIONS_FILE = "tests/unit_test/competitions.json"
PATH_CLUBS_FILE = "tests/unit_tests/clubs.json"


# server.clubs = [
data_clubs = [
    {
        "name":"Héraclès_Temple",
        "email":"hercule@heavylift.gr",
        "points":"18"
    },
    {
        "name":"Popeye_Loft",
        "email": "pop@spinach.com",
        "points":"15"
    },
    {   "name":"Serena_Lounge",
        "email": "venus@sheace.us",
        "points":"14"
    }
]

server.competitions = [
    {
        "name": "Summer Meeting",
        "date": "2023-04-20 15:00:00",
        "numberOfPlaces": "35"
    },
    {
        "name": "Canadian Lifter",
        "date": "2023-11-20 18:30:00",
        "numberOfPlaces": "25"
    }
]
    
 

# ============ Logging ==============

def test_index_email_ok(client):
	response = client.get('/')
	assert response.status_code == 200
	data = response.data.decode()
	assert "Welcome" in data


def test_index_email_wrong(client):
	email = "unknown@email.com"
	response = client.post("/showSummary", data={"email": email})
	assert response.status_code == 200
	data = response.data.decode()
	assert "Wrong Email Try again" in data


def test_logout_page(client):
    response = client.get('/logout')
    data = response.data.decode()
    assert response.status_code == 302


# ====Test global Fonction load_clubs() & load_competitions() ====




def test_load_clubs_file_not_empty():
    """ Test that clubs database is not empty """
    clubs = open
    data_clubs = loadClubs()
    print('data0:', data_clubs[0]['email'])
    assert data_clubs[0]['email'] == 'john@simplylift.co'    
    assert data_clubs != ""


def test_load_competitions_file_not_empty():
    """ Test that clubs database is not empty """
    
    data_competitions = loadCompetitions()
    assert data_competitions != ""



# ====Test local Fonction load_clubs() & load_competitions() ====
