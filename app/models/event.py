from ..extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    location = db.relationship('Location', backref=db.backref('event_locations', lazy=True))
    faction_id = db.Column(db.Integer, db.ForeignKey('faction.id'), nullable=True)
    faction = db.relationship('Faction', backref=db.backref('events', lazy=True))
    plot_id = db.Column(db.Integer, db.ForeignKey('plot.id'), nullable=True)
    plot = db.relationship('Plot', backref=db.backref('events', lazy=True))
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('events', lazy=True))

    
    def __repr__(self):
        return f'<Event {self.name}>'
