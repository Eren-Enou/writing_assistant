from ..extensions import db
from .associations import item_locations, item_events

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    item_type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=True)
    value = db.Column(db.Integer, nullable=True)
    enchantment = db.Column(db.String(50), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    owner = db.relationship('Character', backref=db.backref('item_owner', lazy=True))
    locations = db.relationship('Location', secondary=item_locations, backref=db.backref('item_locations', lazy=True))
    events = db.relationship('Event', secondary=item_events, backref=db.backref('item_events', lazy=True))
    
    def __repr__(self):
        return f'<Item {self.name}>'
