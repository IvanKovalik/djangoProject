from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def messenger_index_view(request):
    return HttpResponse('This is messenger')


def func(request, pid):
    return HttpResponse(f'This is page with id {pid}')
