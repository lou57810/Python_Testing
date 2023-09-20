import pytest

from bs4 import BeautifulSoup
from Python_Testing import server
from Python_Testing.tests.conftest import client
from Python_Testing.tests.conftest import mock_clubs, mock_comps


def test_server_sequence(client, mocker):
    # Logging avec un club enregistré.
    mocker.patch.object(server, "clubs", mock_clubs)
    mocker.patch.object(server, "competitions", mock_comps)

    email = mock_clubs[3]['email']
    response = client.post("/showSummary", data={"email": email})
    data = response.data.decode()

    # Vérifier la redirection vers la page sommaire
    assert response.status_code == 200
    soup = BeautifulSoup(data, "html.parser")
    assert soup.h2.get_text() == 'Welcome,' + ' ' + email + ' '

    # Verifier la redirection vers la page competition
    club_name = mock_clubs[3]['name']
    comp_name = mock_comps[1]['name']

    response = client.get('/book/' + comp_name + '/' + club_name)

    assert response.status_code == 200
    data = response.data.decode()

    soup = BeautifulSoup(data, "html.parser")
    print('soupe:', soup.h2.get_text)
    assert soup.h2.get_text() == comp_name

    # Verifier l'envoi et la cohérence des datas
    placesRequired = 9
    response = client.post("/purchasePlaces", data={
        "club": club_name,
        "competition": comp_name,
        "places": placesRequired})
    assert response.status_code == 200
    data = response.data.decode()
    assert "Great-booking complete!" in data
    assert "Points available: 0" in data

    response = client.get('/logout', follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert "Welcome to the GUDLFT Registration Portal!" in data



