from rest_framework import viewsets

from nasalbum.albums.models import AlbumImage
from nasalbum.albums.serializers import AlbumImageSerializer


class AlbumImageViewSet(viewsets.ModelViewSet):
    """
    Returns the album information, metadata, and url for images
    """

    queryset = AlbumImage.objects.all()
    serializer_class = AlbumImageSerializer
