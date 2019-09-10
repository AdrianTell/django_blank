import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    username = models.EmailField(primary_key=True)
    has_tempPassword = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=150)


