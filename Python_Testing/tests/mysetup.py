import pytest
import server


@pytest.fixture
def client():
    client = server.app.test_client()
    return client


# Mock d'une compétition pour les tests
def mock_competitions():
    competitions = [
        {
            "name": "Spring Festival",
            "date": "2025-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
    return competitions


# Mock d'un club pour les tests
def mock_clubs():
    clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "500"
        }
    ]
    return clubs


@pytest.fixture
def mock_data(mocker):
    mocker.patch.object(server, 'competitions', mock_competitions())
    mocker.patch.object(server, 'clubs', mock_clubs())
    return mocker
