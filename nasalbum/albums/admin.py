from django.contrib import admin

from reversion.admin import VersionAdmin

from nasalbum.albums.models import Album, AlbumImage


@admin.register(AlbumImage)
class AlbumImageAdmin(VersionAdmin):
    list_filter = ("album",)


@admin.register(Album)
class AlbumAdmin(VersionAdmin):
    list_display = (
        "name",
        "owner",
    )
