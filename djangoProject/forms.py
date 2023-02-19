from django.contrib.auth.forms import UserCreationForm
from djangoProject.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
