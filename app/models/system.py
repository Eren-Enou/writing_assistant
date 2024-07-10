from ..extensions import db
from .associations import system_worlds

class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rules = db.Column(db.Text, nullable=True)
    basis = db.Column(db.Text, nullable=True)
    worlds = db.relationship('World', secondary=system_worlds, backref=db.backref('system_worlds', lazy=True))

    
    def __repr__(self):
        return f'<MagicSystem {self.name}>'
