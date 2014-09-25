
from django.shortcuts import render


def intro(request, template='intro.html'):
    response = render(request, template)
    response['X-Frame-Options'] = 'SAMEORIGIN'

    return response
