from ..extensions import db

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    plot_id = db.Column(db.Integer, db.ForeignKey('plot.id'), nullable=False)
    plot = db.relationship('Plot', backref=db.backref('chapters', lazy=True))
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('chapters', lazy=True))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=True)
    location = db.relationship('Location', backref=db.backref('chapters', lazy=True))
    creature_id = db.Column(db.Integer, db.ForeignKey('creature.id'), nullable=True)
    creature = db.relationship('Creature', backref=db.backref('chapters', lazy=True))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=True)
    event = db.relationship('Event', backref=db.backref('chapters', lazy=True))
    magic_system_id = db.Column(db.Integer, db.ForeignKey('system.id'), nullable=True)
    magic_system = db.relationship('System', backref=db.backref('chapters', lazy=True))
    faction_id = db.Column(db.Integer, db.ForeignKey('faction.id'), nullable=True)
    faction = db.relationship('Faction', backref=db.backref('chapters', lazy=True))
    
    def __repr__(self):
        return f'<Chapter {self.title}>'

