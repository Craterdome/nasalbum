import json
import os

from django.core.files import File
from django.core.management.base import BaseCommand

from nasalbum.albums.models import Album, AlbumImage


class Command(BaseCommand):
    """
    Imports a directory of images and json metadata into the app
    Usage: python manage.py import_images --path=C:/Path/To/Images
    """

    help = "Import jpgs and their json metadata"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **options):
        # grab all the images from the directory
        path = options["path"]
        images = []
        for filename in os.listdir(path):
            if filename.endswith(".jpg"):
                images.append(filename)

        for image in images:
            # find image and matching json metadata
            image_path = os.path.join(path, image)
            json_path = os.path.join(path, image[:-3] + "json")
            with open(json_path) as json_file:
                json_text = json_file.read()
            metadata = json.loads(json_text)

            # create an album from the metadata if available
            album_name = metadata.get("album", "NASA")
            album, created = Album.objects.get_or_create(name=album_name)

            with open(image_path, "rb") as image_file:
                # if the album metadata are the same, don't duplicate
                album_image, created = AlbumImage.objects.get_or_create(
                    album=album, metadata=json_text
                )
                # save the image to our media root, then save the model to db
                album_image.image.save(os.path.basename(image), File(image_file))
                album_image.save()
                print(f"Imported '{image}' into '{album}' album")
