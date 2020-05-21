import json

from django.conf import settings
from django.db import models

from nasalbum.core.models import BaseModel


class Album(BaseModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class AlbumImage(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="albums")
    metadata = models.TextField()

    @property
    def metadata_json(self):
        """
        In a fuller version the metadata would be added
        to individual fields on the AlbumImage model.
        This would allow the metadata to be more searchable.
        """
        try:
            return json.loads(self.metadata)
        except ValueError:
            return {}

    def __str__(self):
        meta = self.metadata_json
        if "nasaId" in meta:
            return f"{self.album.name} - {meta['nasaId']}"
        return self.album.name
