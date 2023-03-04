from django.urls import path, include
from .views import *

urlpatterns = [
    path('', messenger_index_view),
    path('<int:pid>', func),
]
