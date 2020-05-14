import requests
from app import db
from app.models import Pokemon


def get_request(url):
    r = requests.get(url)
    return r.json()


def get_pokedex():
    return get_request('https://pokeapi.co/api/v2/pokedex/1')


def get_pokemon(pokemon):
    return get_request('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))


def check_database():
    pokemons = get_pokedex()['pokemon_entries']
    for pokemon in pokemons:
        check_id = Pokemon.query.filter_by(id=pokemon['entry_number']).first()
        if check_id is None:
            p_info = get_pokemon(pokemon['entry_number'])
            p_type1 = [t['type']['name'].capitalize() for t in p_info['types'] if t['slot'] == 1][0]
            try:
                p_type2 = [t['type']['name'].capitalize() for t in p_info['types'] if t['slot'] == 2][0]
            except IndexError:
                p_type2 = None
            ability_1 = None
            ability_2 = None
            ability_3 = None
            for ability in p_info['abilities']:
                if ability['slot'] == 3:
                    ability_3 = ability['ability']['name']
                elif ability['slot'] == 2:
                    ability_2 = ability['ability']['name']
                elif ability['slot'] == 1:
                    ability_1 = ability['ability']['name']
            p_stat_hp = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "hp"][0]
            p_stat_atk = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "attack"][0]
            p_stat_def = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "defense"][0]
            p_stat_spatk = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "special-attack"][0]
            p_stat_spdef = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "special-defense"][0]
            p_stat_spd = [s['base_stat'] for s in p_info['stats'] if s['stat']['name'] == "speed"][0]

            p = Pokemon(id=pokemon['entry_number'], name=pokemon['pokemon_species']['name'].capitalize(),
                        height=p_info['height'], weight=p_info['weight'], type1=p_type1, type2=p_type2,
                        sprites_back_default=p_info['sprites']['back_default'],
                        sprites_back_female=p_info['sprites']['back_female'],
                        sprites_back_shiny=p_info['sprites']['back_shiny'],
                        sprites_back_shiny_female=p_info['sprites']['back_shiny_female'],
                        sprites_front_default=p_info['sprites']['front_default'],
                        sprites_front_female=p_info['sprites']['front_female'],
                        sprites_front_shiny=p_info['sprites']['front_shiny'],
                        sprites_front_shiny_female=p_info['sprites']['front_shiny_female'], base_stat_hp=p_stat_hp,
                        base_stat_atk=p_stat_atk, base_stat_def=p_stat_def, base_stat_spatk=p_stat_spatk,
                        base_stat_spdef=p_stat_spdef, base_stat_speed=p_stat_spd, ability_1=ability_1,
                        ability_2=ability_2, ability_3=ability_3)
            print(p)
            db.session.add(p)
            db.session.commit()
