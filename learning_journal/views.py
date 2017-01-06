"""Stores views for __init__.py"""


import os
from pyramid.view import view_config


HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "LJ - Day 10", "date": "Aug 19, 2016", "id": 10, "body": "Sample body text."},
    {"title": "LJ - Day 11", "date": "Aug 22, 2016", "id": 11, "body": "Sample body text."},
    {"title": "LJ - Day 12", "date": "Aug 23, 2016", "id": 12, "body": "Sample body text."},
]


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    # imported_text = open(os.path.join(HERE, 'data/home.html')).read()
    # return imported_text
    return {"entries": ENTRIES}


@view_config(route_name='detail', renderer='templates/detail.jinja2')
def detail(request):
    # imported_text = open(os.path.join(HERE, 'data/detail.html')).read()
    # return imported_text
    return {"entry": ENTRIES[0]}


@view_config(route_name='create', renderer='templates/create.jinja2')
def create(request):
    # imported_text = open(os.path.join(HERE, 'data/create.html')).read()
    # return imported_text
    return {}


@view_config(route_name='update', renderer='templates/update.jinja2')
def update(request):
    # imported_text = open(os.path.join(HERE, 'data/update.html')).read()
    # return imported_text
    return {"entry": ENTRIES[0]}


# def includeme(config):
#     config.add_view(home, route_name='home')
#     config.add_view(detail, route_name='detail')
#     config.add_view(create, route_name='create')
#     config.add_view(update, route_name='update')
