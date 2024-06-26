import uuid
from django.db import models

class LicenseModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    key = models.UUIDField(default=uuid.uuid4, unique=True)
    is_Activated = models.BooleanField(default=False)
    def __str__(self):
        return self.name
