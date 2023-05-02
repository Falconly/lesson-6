from django import template

register = template.Library()


@register.simple_tag()
def get_menu():
    menu = [{'title': 'Список сотрудников', 'url_name': 'list_workers'},
            {'title': 'Сотрудник месяца', 'url_name': 'employee_month'},
            {'title': 'Добавить сотрудника', 'url_name': 'add_worker'}]
    return menu
