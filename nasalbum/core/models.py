from django.db import models


class BaseModel(models.Model):
    """An abstract model all models should extend to get timestamps"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
