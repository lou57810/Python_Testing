import pytest
import requests
from bs4 import BeautifulSoup
import unittest
import json

from .conftest import client
from unittest import mock, TestCase
from unittest.mock import patch, Mock
from Python_Testing import server
from Python_Testing.server import loadClubs, clubs, competitions
from Python_Testing.server import loadCompetitions
from flask import Flask
import os



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
    response = client.get('/logout')
    data = response.data.decode()
    assert response.status_code == 302

"""
# ====Test global Fonction load_clubs() & load_competitions() ====

def test_load_clubs_file():
    # Test load function return true values
     
    data_clubs = loadClubs()
    assert data_clubs[0]['name'] == "Simply Lift"
    assert data_clubs[0]['email'] == 'john@simplylift.co'
    assert data_clubs[0]['points'] == "13"
    assert data_clubs[1]['name'] == "Iron Temple"
    assert data_clubs[1]['email'] == 'admin@irontemple.com'
    assert data_clubs[1]['points'] == "4"
    assert data_clubs[2]['name'] == "She Lifts"
    assert data_clubs[2]['email'] == 'kate@shelifts.co.uk'
    assert data_clubs[2]['points'] == "12"


def test_load_competitions_file():
    # Test load function return true values 
    data_competitions = loadCompetitions()
    assert data_competitions[0]['name'] == "Winter Meeting"
    assert data_competitions[0]['date'] == "2020-04-20 15:00:00"
    assert data_competitions[0]['numberOfPlaces'] == "28"
    assert data_competitions[1]['name'] == "HeroesLifter"
    assert data_competitions[1]['date'] == "2022-11-20 18:30:00"
    assert data_competitions[1]['numberOfPlaces'] == "18"


# ====Test local Fonction load_clubs() & load_competitions() ====

def test_local_loadClubs():
    pass
    
def test_local_loadCompetitions():
    pass
"""
# ================== Test load fct =====================

class TestLoadClubs(unittest.TestCase):
    @patch('Python_Testing.server.loadClubs')
    def test_load_clubs_response(self, mock_get_club_json):
        mock_get_club_json.return_value = [
    {
        "name": "Héraclès_Temple",
        "email": "hercule@heavylift.gr",
        "points": "18"
    },
    {
        "name": "Popeye_Loft",
        "email": "pop@spinach.com",
        "points": "15"
    },
    {
        "name": "Serena_Lounge",
        "email": "venus@sheace.us",
        "points": "14"
    }
]
        self.assertEqual(loadClubs(), clubs)


class TestLoadCompetitions(unittest.TestCase):
    @patch('Python_Testing.server.loadCompetitions')
    def test_load_competitions_response(self, mock_get_comp_json):
        mock_get_comp_json.return_value = [
        {
            "name": "Summer LiftFest",
            "date": "2023-04-20 15:00:00",
            "numberOfPlaces": "35"
        },
        {
            "name": "Canadian Lifter",
            "date": "2023-10-15 16:30:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Australian Lifter",
            "date": "2023-11-20 18:30:00",
            "numberOfPlaces": "11"
        }
    ]
        self.assertEqual(loadCompetitions(), competitions)


# =============== Test booking page ==================

def test_book_page_access_function(client):

    email = server.loadClubs()[0]['email']
    response = client.post("/showSummary", data={"email": email})

    data = response.data.decode()
    assert response.status_code == 200

    soup = BeautifulSoup(data, "html.parser")
    # print('email:', email)
    # print('response:', response)
    # print('data:', data)
    # print('soup:', soup.h2)

    assert soup.h2.get_text() == 'Welcome,' + ' ' + email + ' '


def test_purchase_page_access_function(client):
    club_name = server.loadClubs()[1]['name']
    comp_name = server.loadCompetitions()[1]['name']
    # response = client.post("/Iron Temple", data={"name": comp_name})
    response = client.get('/book/' + comp_name + '/' + club_name)
    print('response:', response)

    assert response.status_code == 200
    data = response.data.decode()

    soup = BeautifulSoup(data, "html.parser")
    assert soup.h2.get_text() == comp_name

    print('name:', comp_name)
    # print('response:', response)
    # print('data:', data)
    print('soup:', soup.h2)

 # ==== test booking messages of usage of points and places ====




