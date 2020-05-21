import json
import os

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase, Client

from nasalbum.albums.models import AlbumImage


class AlbumImageTestCase(TestCase):
    def _import_images(self):
        """Import the images for testing"""
        image_path = os.path.join(settings.PROJECT_ROOT, "images")
        opts = {"path": image_path}
        call_command("import_images", *[], **opts)

    def test_import_images(self):
        """Import the images and verify database information"""
        self._import_images()
        self.assertEqual(AlbumImage.objects.count(), 4)

        album_image = AlbumImage.objects.all()[0]
        self.assertEqual(album_image.album.name, "Test")
        self.assertEqual(album_image.metadata_json["creator"], "NASA Goddard")

    def test_api(self):
        """Import the images and verify the api is working"""
        self._import_images()
        c = Client()
        response = c.get("/api/images/")
        images = json.loads(response.content)
        self.assertEqual(len(images), 4)

        image = images[0]
        self.assertEqual(image["nasaId"], "GSFC_20171208_Archive_e001465")
