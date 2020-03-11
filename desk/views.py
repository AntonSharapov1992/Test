from django.shortcuts import render
from django.http import HttpResponse


def desk_index(request):
    print()
    print(request)
    print()
    for d in dir(request):
        print(d)
    print()

    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")
