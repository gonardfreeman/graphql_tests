import graphene
from menus.models import PageModel, MenuModel
from .data_handler import create_page, get_menu, get_page, menus, pages
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

import logging

logger = logging.getLogger(__name__)


class PageNode(DjangoObjectType):
    class Meta:
        model = PageModel
        interfaces = (graphene.relay.Node, )
        filter_fields = ['name', 'url', 'position', 'visible']

    @classmethod
    def get_node(cls, id, context, info):
        node = get_page(id)
        return node

    @classmethod
    def get_connection(cls):
        class CountableConnection(graphene.relay.Connection):
            total_count = graphene.Int()

            class Meta:
                name = '{}Connection'.format(cls._meta.name)
                node = cls

            @staticmethod  # Redundant since Graphene kinda does this automatically for all resolve_ methods.
            def resolve_total_count(root, args, context, info):
                return root.length

        return CountableConnection


class MenuNode(DjangoObjectType):
    class Meta:
        model = MenuModel
        interfaces = (graphene.relay.Node, )
        # filter_fields = {
        #     'page_id': ['exact'],
        #     'menu__name': ['istartswith', 'exact', 'icontains']
        # }

    @classmethod
    def get_node(cls, id, context, info):
        node = get_menu(id)
        return node

    @classmethod
    def get_connection(cls):
        class CountableConnection(graphene.relay.Connection):
            total_count = graphene.Int()

            class Meta:
                name = '{}Connection'.format(cls._meta.name)
                node = cls

            @staticmethod  # Redundant since Graphene kinda does this automatically for all resolve_ methods.
            def resolve_total_count(root, args, context, info):
                return root.length

        return CountableConnection


class Query(graphene.AbstractType):
    page = DjangoFilterConnectionField(PageNode)
    pages = DjangoFilterConnectionField(PageNode)
    menu = DjangoFilterConnectionField(MenuNode)
    menus = DjangoFilterConnectionField(MenuNode)

    def resolve_menus(self, args, context, info):
        return menus()

    def resolve_pages(self, args, context, info):
        logger.error(args)
        return pages()


class CreatePage(graphene.relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        url = graphene.String(required=True)
        position = graphene.Int(required=True)
        visible = graphene.Boolean(required=True)

    page = graphene.Field(PageNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, context):
        page = create_page(
            name=root.get('name'),
            url=root.get('url'),
            position=root.get('position'),
            visible=root.get('visible')
        )
        return CreatePage(page=page)


class Mutation(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')
    create_page = CreatePage.Field()
