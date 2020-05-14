from app import db


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    type1 = db.Column(db.String(64))
    type2 = db.Column(db.String(64))
    base_stat_hp = db.Column(db.Integer)
    base_stat_speed = db.Column(db.Integer)
    base_stat_spdef = db.Column(db.Integer)
    base_stat_spatk = db.Column(db.Integer)
    base_stat_atk = db.Column(db.Integer)
    base_stat_def = db.Column(db.Integer)
    ability_1 = db.Column(db.String(64))
    ability_2 = db.Column(db.String(64))
    ability_3 = db.Column(db.String(64))
    sprites_back_default = db.Column(db.String(255))
    sprites_back_female = db.Column(db.String(255))
    sprites_back_shiny = db.Column(db.String(255))
    sprites_back_shiny_female = db.Column(db.String(255))
    sprites_front_default = db.Column(db.String(255))
    sprites_front_female = db.Column(db.String(255))
    sprites_front_shiny = db.Column(db.String(255))
    sprites_front_shiny_female = db.Column(db.String(255))

    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)
