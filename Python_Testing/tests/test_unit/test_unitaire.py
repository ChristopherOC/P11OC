import pytest
from tests.mysetup import client, mock_data


@pytest.mark.usefixtures('client', 'mock_data')
class TestsUnitLogin:
    # Test la route de l'index
    def test_index(self, client):
        response = client.get('/')
        response_data = response.data.decode()
        assert response.status_code == 200
        assert '<h1>Welcome to the GUDLFT Registration Portal!</h1>' in response_data

    # Test le login avec des ID corrects
    def test_login(self, client):
        response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
        assert response.status_code == 200
        assert 'Welcome' in response.data.decode()
        assert 'john@simplylift.co ' in response.data.decode()

    # Test le login avec des ID incorrects
    def test_login_wrong_mail(self, client):
        email = 'testuser@fakemail.com'
        response = client.post('/showSummary', data={'email': email})
        assert response.status_code == 200
        assert 'Sorry, that email was not found' in response.data.decode()

    # Test la déconnexion
    def test_logout(self, client):
        response = client.get('/logout')
        assert response.status_code == 302

    # Test la route montrant le résumé des points des clubs
    def test_rankings(self, client):
        response = client.get('/show_points')
        response_data = response.data.decode()
        assert response.status_code == 200
        assert '<td>Club :</td>' in response_data
        assert '<td>Points :</td>' in response_data

# Classe pour tester la partie achat
@pytest.mark.usefixtures('client', 'mock_data')
class TestsUnitPurchase:
    # Test d'achat valid
    def test_purchase_places(self, client):
        response = client.post('/purchasePlaces', data={'club': 'Simply Lift',
                                                        'competition': 'Spring Festival', 'places': '1'
                                                        }
                               )
        assert response.status_code == 200
        assert 'Great-booking complete!' in response.data.decode()

    # Test d'achat de plus de 12 places
    def test_purchase_restrictions(self, client):
        response = client.post('/purchasePlaces', data={'club': 'Simply Lift',
                                                        'competition': 'Spring Festival', 'places': '13'
                                                        }
                               )
        assert response.status_code == 200
        assert 'book more than 12 points' in response.data.decode()

    # Test d'achat de place d'une compétition passée
    def test_purchase_past_competition(self, client):
        response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic',
                                                        'places': '1'})
        assert response.status_code == 200
        assert 'book for a past competition' in response.data.decode()
    
    # Test d'achat avec un solde insuffisant
    def test_not_enough_points(self, client):
        response = client.post('/purchasePlaces', data={'club': 'Iron Temple',
                                                        'competition': 'Spring Festival',
                                                        'places': '7'
                                                        }
                               )
        assert response.status_code == 200
        assert 'have enough points' in response.data.decode()
    
    def test_purchase_with_sufficient_points(self, client):
        club_name = 'Simply Lift'
        competition_name = 'Spring Festival'
        places = 1

        response = client.post('/purchasePlaces', data={'club': club_name,
                                                        'competition': competition_name,
                                                        'places': str(places)
                                                        }
                               )

        assert response.status_code == 200
        assert 'Great-booking complete!' in response.data.decode()