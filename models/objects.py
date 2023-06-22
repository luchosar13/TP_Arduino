from graphene_sqlalchemy import (
    SQLAlchemyObjectType,
)
from graphene import (
    # Int
    String
)
from models.avion import Avion as AvionModel
# from models.user import User as UserModel
from models.piloto import Piloto as PilotoModel

from models.hangar import Hangar as HangarModel

class Piloto(SQLAlchemyObjectType):
    class Meta:
        model = PilotoModel
    name = String(description='representa el nombre del piloto')

class Avion(SQLAlchemyObjectType):
    class Meta:
        model = AvionModel

class Hangar(SQLAlchemyObjectType):
    class Meta:
        model = HangarModel