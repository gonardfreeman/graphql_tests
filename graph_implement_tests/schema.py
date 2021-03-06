import menus.schema
import graphene
from menus.schema import PageNode, MenuNode

from graphene_django.debug import DjangoDebug


class Query(menus.schema.Query, graphene.ObjectType):
    name = 'test'
    debug = graphene.Field(DjangoDebug, name='__debug')


schema = graphene.Schema(
    query=Query,
    mutation=menus.schema.Mutation,
    types=[PageNode, MenuNode]
)
