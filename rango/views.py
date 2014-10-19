from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    """
    Main page of Rango application
    """
    context_dict = {'boldmessage': "I am bold font from the context"}

    return render(request, 'index.html', context_dict)

