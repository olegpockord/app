from django import template
from django.utils.safestring import mark_safe

from treemenu.models import Menu

register = template.Library()

@register.simple_tag()
def draw_menu(menu_name):
    menu_items = Menu.objects.filter(name=menu_name).select_related('parent')
    return mark_safe(display(menu_items))


def display(menu_items):
    html_for_menu = '<ul>'

    for item in menu_items:
        html_for_menu += '<li>'
        if item.named_url:
            html_for_menu += f'<a href="{item.named_url}">{item.name}</a>'
        elif item.slug:
            html_for_menu += f'<a href="{item.slug}">{item.name}</a>'
        else:
            html_for_menu += item.name

        if item.child.exists():
            html_for_menu += display(item.child.all())
        html_for_menu += '</li>'
    html_for_menu += '</ul>'
    
    return html_for_menu