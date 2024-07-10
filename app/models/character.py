from ..extensions import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    race = db.Column(db.String(80), nullable=False)
    class_ = db.Column(db.String(80), nullable=False)
    deity = db.Column(db.String(80), nullable=True)
    age = db.Column(db.Integer, nullable=False)
    alignment = db.Column(db.String(10), nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    dexterity = db.Column(db.Integer, nullable=False)
    constitution = db.Column(db.Integer, nullable=False)
    intelligence = db.Column(db.Integer, nullable=False)
    wisdom = db.Column(db.Integer, nullable=False)
    charisma = db.Column(db.Integer, nullable=False)
    experience_points = db.Column(db.Integer, nullable=False)
    background = db.Column(db.Text, nullable=False)
    personality = db.Column(db.Text, nullable=False)
    ideal = db.Column(db.Text, nullable=False)
    bonds = db.Column(db.Text, nullable=False)
    flaws = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Character {self.name}>'
