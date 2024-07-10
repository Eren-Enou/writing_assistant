from ..extensions import db

class Relationship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character1_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    character2_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    relationship_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    level = db.Column(db.Integer, nullable=True)
    is_romantic = db.Column(db.Boolean, nullable=True)
    is_supportive = db.Column(db.Boolean, nullable=True)
    is_rival = db.Column(db.Boolean, nullable=True)
    is_ally = db.Column(db.Boolean, nullable=True)
    is_conflict = db.Column(db.Boolean, nullable=True)

    character1 = db.relationship('Character', foreign_keys=[character1_id], backref=db.backref('relationships1', lazy=True))
    character2 = db.relationship('Character', foreign_keys=[character2_id], backref=db.backref('relationships2', lazy=True))
    
    def __repr__(self):
        return f'<Relationship {self.character1.name} - {self.character2.name}>'
