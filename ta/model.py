from ta import db

class TextEntry(db.Model):
    __tablename__ = 'ta_stats'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    result = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<TextEntry {self.text}>'
