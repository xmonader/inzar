import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType



class Query(graphene.ObjectType):
    node = relay.Node.Field()


    def resolve_objects(self, args, context, info):
        query = Link.get_query(context)
        return query.all()


schema = graphene.Schema(query=Query, types=[])