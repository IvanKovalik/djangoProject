from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def tests_index_view(request):
    return HttpResponse('This is testing app')
