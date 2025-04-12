import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    isActive = models.BooleanField()

    def __str__(self):
        return self.name
