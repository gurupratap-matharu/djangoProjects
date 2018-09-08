from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def papa(request):
    return HttpResponse("Papa i Miss You!")


def mama(request):
    return HttpResponse("Mama I love you!")
