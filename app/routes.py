from flask import render_template

from app import app
from app.models import Pokemon
from app.methods import check_database

@app.route('/')
@app.route('/dex')
def dex():
    check_database()
    pokemon_list = Pokemon.query.all()
    return render_template('dex.html', title='Entire National Dex', pokemons=pokemon_list)

@app.route('/<pokemon>')
def pokemon_page(pokemon):
    pokemon = Pokemon.query.filter_by(name=pokemon).first() or Pokemon.query.filter_by(id=pokemon).first()
    return render_template('pokemon.html', title=pokemon, pokemon=pokemon)
