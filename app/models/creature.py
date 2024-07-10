from ..extensions import db
from .associations import creature_events, creature_factions, creature_locations

class Creature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('creature_world', lazy=True))
    species = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    role = db.Column(db.String(50), nullable=False)
    align = db.Column(db.String(50), nullable=False)
    abilities = db.Column(db.Text, nullable=True)
    weapons = db.Column(db.Text, nullable=True)
    armor = db.Column(db.Text, nullable=True)
    events = db.relationship('Event', secondary=creature_events, backref=db.backref('creature_events', lazy=True))
    factions = db.relationship('Faction', secondary=creature_factions, backref=db.backref('creature_factions', lazy=True))
    locations = db.relationship('Location', secondary=creature_locations, backref=db.backref('creature_locations', lazy=True))
    
    def __repr__(self):
        return f'<Creature {self.name}>'
