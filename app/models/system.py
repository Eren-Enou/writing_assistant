from ..extensions import db

class System(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rules = db.Column(db.Text, nullable=True)
    basis = db.Column(db.Text, nullable=True)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('magic_systems', lazy=True))
    
    def __repr__(self):
        return f'<MagicSystem {self.name}>'
