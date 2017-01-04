"""Stores views for __init__.py"""


import os
from pyramid.response import Response

HERE = os.path.dirname(__file__)

def home_page(request):
    imported_text = open(os.path.join(HERE, 'sample.html')).read()
    return Response(imported_text)

def includeme(config):
    config.add_view(home_page, route_name='home')
