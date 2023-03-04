from django.urls import path, include
from .views import *

urlpatterns = [
    path('', tests_index_view)
]