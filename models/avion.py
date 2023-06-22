from api_config import db


class Avion(db.Model):
    __tablename__ = "avion"
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50))
    color = db.Column(db.String(50))