from .models import PageModel, MenuModel


def create_page(name, url, position, visible):
    new_page = PageModel(
        name=name,
        url=url,
        position=position,
        visible=visible
    )
    new_page.save()
    return new_page


def get_menu(_id):
    return MenuModel.objects.get(pk=_id)


def menus():
    return MenuModel.objects.all()


def get_page(_id):
    return PageModel.objects.get(pk=_id)


def pages():
    return PageModel.objects.all()