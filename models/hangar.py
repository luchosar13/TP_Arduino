from api_config import db

class Hangar(db.Model):
    __tablename__ = "hangar"
    id = db.Column(db.Integer, primary_key=True)
    sector = db.Column(db.String(50))
    aeropuerto = db.Column(db.String(500))
    avion_fk = db.Column(db.Integer, db.ForeignKey("avion.id"))
    avion = db.relationship('Avion')