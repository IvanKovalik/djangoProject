import uuid
from random import randint

from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, UUIDField, EmailField, BooleanField
from django.utils.timezone import now


class User(AbstractUser):
    username = CharField(
        max_length=50,
        unique=True,
        null=False,
        help_text='This is your username',
    )
    password = CharField(
        max_length=50,
        null=False,
    )
    email = EmailField(
        max_length=50,
        null=False,
        unique=True,
    )
    date_joined = DateField(
        default=now(),
    )
    user_id = UUIDField(default=uuid.uuid4())
    is_staff = BooleanField(default=False)

    def __str__(self):
        return self.username
