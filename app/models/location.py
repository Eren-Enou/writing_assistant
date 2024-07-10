from ..extensions import db
from .associations import location_residents, location_factions, location_events, location_plots

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('locations', lazy=True))
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    residents = db.relationship("Character", secondary=location_residents, backref="locations")
    factions = db.relationship("Faction", secondary=location_factions, backref="locations")
    events = db.relationship("Event", secondary=location_events, backref="event_locations")
    plots = db.relationship("Plot", secondary=location_plots, backref="plot_locations")

    
    def __repr__(self):
        return f'<Location {self.name}>'
