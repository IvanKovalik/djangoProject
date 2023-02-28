from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import Form
from djangoProject.models import User, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class MessageForm(Form):
    class Meta:
        model = Message
        fields = ['body']
