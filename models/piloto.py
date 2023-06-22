from api_config import db


class Piloto(db.Model):
    __tablename__ = "piloto"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(500))
    email  = db.Column(db.String(150), nullable=True)
    avion_fk = db.Column(db.Integer, db.ForeignKey("avion.id"))
    avion = db.relationship('Avion', backref='pilotos_avion')

