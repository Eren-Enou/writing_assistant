from ..extensions import db
from .associations import location_chapters, creature_chapters, event_chapters, system_chapters, faction_chapters

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    plot_id = db.Column(db.Integer, db.ForeignKey('plot.id'), nullable=False)
    plot = db.relationship('Plot', backref=db.backref('chapter_plot', lazy=True))
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('chapter_world', lazy=True))
    locations = db.relationship('Location', secondary=location_chapters, backref=db.backref('chapter_locations', lazy=True))
    creatures = db.relationship('Creature', secondary=creature_chapters, backref=db.backref('chapter_creatures', lazy=True))
    events = db.relationship('Event', secondary=event_chapters, backref=db.backref('chapter_events', lazy=True))
    magic_systems = db.relationship('System', secondary=system_chapters, backref=db.backref('chapter_systems', lazy=True))
    factions = db.relationship('Faction', secondary=faction_chapters, backref=db.backref('chapter_factions', lazy=True))

    
    def __repr__(self):
        return f'<Chapter {self.title}>'

