import uuid

from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CASCADE
from django.db.models import CharField, DateField, UUIDField, EmailField, BooleanField, ForeignKey, TextField, DateTimeField
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
    body = TextField(max_length=1000, null=False)
    from_who = ForeignKey(User, on_delete=CASCADE)
    date_time_sent = DateTimeField(verbose_name='creation_time', default=now())
    is_changed = BooleanField(default=False)
    when_changed = DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
