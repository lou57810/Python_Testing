import json
from flask import Flask, render_template, request, redirect, flash, url_for
from pathlib import Path
from datetime import datetime


# import sys
# from pprint import pprint
# pprint(sys.path)
# project_dir = Path(__file__).parent
# print('project_dir:', project_dir)

def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        # print('listclubs:', listOfClubs)
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        # print('listCompetitions:', listOfCompetitions)
        return listOfCompetitions


app = Flask(__name__)
#  app.config['DEBUG'] = True
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        error_message = "Wrong Email Try again!"
        return render_template('index.html', error_message=error_message)


# Affichage des compétitions en lice et du formulaire de réservation (booking)
@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]

    print('found:', foundCompetition['date'])
    date = datetime.strptime(foundCompetition['date'], "%Y-%m-%d %H:%M:%S")
    if foundClub and foundCompetition:
        if datetime.now() > date:
            flash("You cannot book places on post-dated competitions !")
            return render_template('welcome.html', club=club, competitions=competitions)

        return render_template('booking.html', club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]

    placesRequired = int(request.form['places'])
    number_of_places = int(competition['numberOfPlaces'])
    points = int(club['points'])

    if placesRequired > number_of_places:
        flash("Not enough places ! Retry.")
        return render_template('welcome.html', club=club, competitions=competitions)
    if placesRequired > points:
        flash("Not enough points ! Retry.")
        return render_template('welcome.html', club=club, competitions=competitions)
    if placesRequired > 12:
        flash("You can't book more than 12 places ! Retry.")
        return render_template('welcome.html', club=club, competitions=competitions)
    else:
        club['points'] = int(club['points']) - placesRequired
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        print('Points, PlacesDispos:', club['points'], int(competition['numberOfPlaces']))
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/dashboard')
def display_datas():
    if clubs != None:
        return render_template('dashboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
