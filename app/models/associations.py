from ..extensions import db

location_residents = db.Table('location_residents',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
)

location_factions = db.Table('location_factions',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True),
)

location_events = db.Table('location_events',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
)

location_plots = db.Table('location_plots',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('plot_id', db.Integer, db.ForeignKey('plot.id'), primary_key=True),
)
