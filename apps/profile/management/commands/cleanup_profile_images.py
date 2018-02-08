from os import path
from django.core.management.base import BaseCommand, CommandError
from django.core.files.storage import default_storage
from django.conf import settings
from apps.profile.models import ProfileImage

class Command(BaseCommand):
    help = 'Deletes not used profile images.'
    base_dir = 'profile'

    def handle(self, *args, **options):
        self.check_directory(path.join(settings.MEDIA_ROOT, self.base_dir))
        pass

    def check_directory(self, directory):
        listdir = default_storage.listdir(directory)
        for directory in listdir[0]:
            self.check_directory(path.join(directory, directory)) 
        for filename in listdir[1]:
            self.check_file(path.join(directory, filename)) 

    def check_file(self, file):
        path = file.replace(settings.MEDIA_ROOT + '/', '')
        try:
            ProfileImage.objects.get(path=path)
        except ProfileImage.DoesNotExist:
            self.stdout.write('Delte %s' %file)
            default_storage.delete(file)
