import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime


#  Permet de charger les données des clubs depuis le fichier clubs.json
def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


#  Permet de charger les données des
#  compétitions depuis le fichier compétitions.json
def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


#  Création de l'app flask
app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


#  Route de la page principale
@app.route('/')
def index():
    return render_template('index.html')


#  Route menant au tableau de bord
@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',
                               club=club, competitions=competitions)
    except IndexError:
        flash('Sorry, that email was not found')
        return render_template('index.html')



#  Route permettant de réserver des places à
#  une compétition pour le club connecté
@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',
                               club=foundClub,
                               competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club,
                               competitions=competitions)


#  Route permettant de réserver les places
@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    date = datetime.strptime(competition['date'], "%Y-%m-%d %H:%M:%S")
    book_authorized = True

    if placesRequired > 12:  # Restriction du nombre
        flash('You can\'t book more than 12 points')
        book_authorized = False
    if date < datetime.now():  # Restriction du temps
        flash('You can\'t book for a past competition')
        book_authorized = False
    if book_authorized:  # Réservation des places réussie
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        club['points'] = int(club['points']) - placesRequired
        success_message = 'Great-booking complete!'
        return render_template('welcome.html', club=club,
                               competitions=competitions,
                               success_message=success_message)
    else:
        return render_template('welcome.html',
                               club=club, competitions=competitions)


# TODO: Add route for points display

#  Route permettant d'accéder au tableau des points
@app.route('/show_points', methods=['GET'])
def show_points():
    return render_template('pointTable.html',
                           clubs=clubs, competitions=competitions)


#  Route permettant de se déconnecter
@app.route('/logout')
def logout():
    return redirect(url_for('index'))
