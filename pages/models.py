from django.db import models

class Pages(models.Model):
    description = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)


