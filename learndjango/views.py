from django.http import HttpResponse
from django.shortcuts import redirect


def index(req):
    return redirect('/emp')
