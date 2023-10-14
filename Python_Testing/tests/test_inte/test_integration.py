from tests.mysetup import client, mock_data
import pytest
import server


@pytest.fixture
def client():
    client = server.app.test_client()
    return client


class TestIntegration:
    def test_integration(self, client):
        # Test loadClubs and loadCompetitions
        response = client.get('/')
        assert response.status_code == 200

        # Test index
        response = client.get('/')
        assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response.data.decode()

        # Test showSummary
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200
        assert 'Welcome' in response.data.decode()

        # Test reservation
        response = client.get('/book/Spring Festival/Simply Lift')
        assert response.status_code == 200

        # Test purchasePlaces restriction de nombre
        response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '13'})
        assert response.status_code == 200
        assert 'book more than 12 points' in response.data.decode()

        # Test purchasePlaces si on a pas assez de points
        response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Spring Festival', 'places': '7'})
        assert response.status_code == 200
        assert 'have enough points' in response.data.decode()

        # Test purchasePlaces pour les compétitions passées
        response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic', 'places': '1'})
        assert response.status_code == 200
        assert 'book for a past competition' in response.data.decode()

        # Test logout
        response = client.get('/logout')
        assert response.status_code == 302
