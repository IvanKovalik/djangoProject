import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CASCADE
from django.db.models import CharField, DateField, UUIDField, EmailField, BooleanField, ForeignKey, TextField
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


class Message(Model):
    to_who = ForeignKey(User, CASCADE)
    date_created = DateField(
        default=now()
    )
    date_updated = DateField(
        auto_now=True
    )
    body = TextField(
        max_length=1000,
        null=False,
        help_text='This is your message',
    )

    def __str__(self):
        return self.body[:50]
