from django.urls import path, include
from .views import auth_app_index_view

urlpatterns = [
    path('', auth_app_index_view)
]
