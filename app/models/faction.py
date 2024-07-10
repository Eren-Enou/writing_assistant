from ..extensions import db

class Faction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('factions', lazy=True))
    is_neutral = db.Column(db.Boolean, default=False)
    is_good = db.Column(db.Boolean, default=False)
    is_evil = db.Column(db.Boolean, default=False)
    is_chaotic = db.Column(db.Boolean, default=False)
    is_lawful = db.Column(db.Boolean, default=False)
    alignment = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return f'<Faction {self.name}>'
