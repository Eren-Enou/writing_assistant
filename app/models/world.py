from ..extensions import db

class World(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    history = db.Column(db.Text, nullable=True)
    time_period = db.Column(db.String(50), nullable=True)
    setting = db.Column(db.String(50), nullable=True)
    temperature = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    flora = db.Column(db.Text, nullable=True)
    fauna = db.Column(db.Text, nullable=True)
    magical_system = db.Column(db.String(100), nullable=True)
    
    def __repr__(self):
        return f'<World {self.name}>'
