from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def auth_app_index_view(request):
    return HttpResponse('This is auth app')

