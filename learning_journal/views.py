"""Stores views for __init__.py"""


import os
from pyramid.response import Response

HERE = os.path.dirname(__file__)

def home(request):
    imported_text = open(os.path.join(HERE, 'data/home.html')).read()
    return Response(imported_text)

def detail(request):
    imported_text = open(os.path.join(HERE, 'data/detail.html')).read()
    return Response(imported_text)

def create(request):
    imported_text = open(os.path.join(HERE, 'data/create.html')).read()
    return Response(imported_text)

def update(request):
    imported_text = open(os.path.join(HERE, 'data/update.html')).read()
    return Response(imported_text)

def includeme(config):
    config.add_view(home, route_name='home')
    config.add_view(detail, route_name='detail')
    config.add_view(create, route_name='create')
    config.add_view(update, route_name='update')
