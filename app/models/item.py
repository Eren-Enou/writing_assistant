from ..extensions import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=True)
    value = db.Column(db.Integer, nullable=True)
    enchantment = db.Column(db.String(50), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)
    owner = db.relationship('Character', backref=db.backref('items', lazy=True))
    
    def __repr__(self):
        return f'<Item {self.name}>'
