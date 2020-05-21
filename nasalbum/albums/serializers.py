from rest_framework import serializers

from nasalbum.albums.models import AlbumImage


class AlbumImageSerializer(serializers.Serializer):
    def to_representation(self, instance):
        request = self.context.get("request")
        metadata = instance.metadata_json
        metadata["id"] = instance.id
        metadata["url"] = request.build_absolute_uri(instance.image.url)
        metadata["album"] = instance.album.name
        return metadata

    class Meta:
        model = AlbumImage
