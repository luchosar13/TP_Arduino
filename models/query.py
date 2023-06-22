from graphene import (
    ObjectType,
    Field,
    String,
    Boolean,
    List,
    Int
)

from .piloto import Piloto as PilotoModel
from .objects import Piloto, Avion, Hangar
from .avion import Avion as AvionModel
from .hangar import Hangar as HangarModel


class Query(ObjectType):
    pilotos = List(lambda: Piloto, last_name=String(), id=Int(), has_email=Boolean(), order_by_name=Boolean())
    aviones = List(lambda: Avion)
    avion = Field(lambda: Avion, id=Int())
    hangares = List(lambda: Hangar)
    hangar = Field(lambda: Hangar, id=Int())


    def resolve_pilotos(self, info, id=None, last_name=None, has_email=None, order_by_name=None):
        query = Piloto.get_query(info=info)
        if id:
            query = query.filter(PilotoModel.id==id)
        if last_name:
            query = query.filter(PilotoModel.last_name==last_name)
        if has_email is not None:
            if has_email:
                query = query.filter(PilotoModel.email != None)
            else:
                query = query.filter(PilotoModel.email == None)
        if order_by_name:
            query = query.order_by(PilotoModel.name)
        return query.all()
    
    def resolve_aviones(self, info):
        query = Avion.get_query(info=info)
        return query.all()
    
    def resolve_avion(self, info, id):
        avio = AvionModel.query.get(id)
        return avio
    
    def resolve_hangares(self, info):
        query = Hangar.get_query(info=info)
        return query.all()
    
    def resolve_hangar(self, info, id):
        hang = HangarModel.query.get(id)
        return hang