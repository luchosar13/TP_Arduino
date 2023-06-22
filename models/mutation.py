from graphene import (
    ObjectType,
    Mutation,
    Int,
    String,
    Field,
)

from api_config import (
    db,
)

from .objects import (
    Piloto,
    Avion,
    Hangar
)

from .piloto import Piloto as PilotoModel
from .avion import Avion as AvionModel
from .hangar import Hangar as HangarModel


class createPiloto(Mutation):
    class Arguments:
        name = String(required=True)
        last_name = String(required=True)
        email = String(required=False)
    
    piloto = Field(lambda: Piloto)

    def mutate(self, info, name, last_name, email=None):
        piloto = PilotoModel(name=name, last_name=last_name, email=email)

        db.session.add(piloto)
        db.session.commit()

        return createPiloto(piloto=piloto)

class updatePiloto(Mutation):
    class Arguments:
        piloto_id = Int(required=True)
        email = String()
        name = String()
        last_name = String()

    piloto = Field(lambda: Piloto)

    def mutate(self, info, piloto_id, email=None, name=None, last_name=None):
        piloto = PilotoModel.query.get(piloto_id)
        if piloto:
            if email:
                piloto.email = email
            if name:
                piloto.name = name
            if last_name:
                piloto.last_name = last_name
            db.session.add(piloto)
            db.session.commit()

        return updatePiloto(piloto=piloto)


class deletePiloto(Mutation):
    class Arguments:
        piloto_id = Int(required=True)

    piloto = Field(lambda: Piloto)

    def mutate(self, info, piloto_id):
        piloto = PilotoModel.query.get(piloto_id)
        if piloto:
            db.session.delete(piloto)
            db.session.commit()

        return deletePiloto(piloto=piloto)
    
class create_Avion(Mutation):
    class Arguments:
        modelo = String(required=True)
        color = String(required=False)
    
    avion = Field(lambda: Avion)

    def mutate(self, info, modelo, color):
        avion = AvionModel(modelo=modelo, color=color)

        db.session.add(avion)
        db.session.commit()

        return createPiloto(avion=avion)
    
class create_Hangar(Mutation):
    class Arguments:
        sector = String(required=True)
        aeropuerto = String(required=True)
    
    hangar = Field(lambda: Hangar)

    def mutate(self, info, sector, aeropuerto):
        hangar = AvionModel(sector=sector, aeropuerto=aeropuerto)

        db.session.add(hangar)
        db.session.commit()

        return create_Hangar(hangar=hangar)

class Mutation(ObjectType):
    create_piloto = createPiloto.Field()
    update_piloto = updatePiloto.Field()
    delete_piloto = deletePiloto.Field()
    create_avion = create_Avion.Field()
    create_hangar = create_Hangar.Field()