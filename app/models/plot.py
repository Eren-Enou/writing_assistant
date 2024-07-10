from ..extensions import db

class Plot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=True)
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    world = db.relationship('World', backref=db.backref('plots', lazy=True))
    status = db.Column(db.String(50), nullable=True)
    genre = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    word_count = db.Column(db.Integer, nullable=True)
    reading_time = db.Column(db.Integer, nullable=True)
    published_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Plot {self.title}>'
