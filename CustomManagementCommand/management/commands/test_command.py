
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This is a test command !!"

    def handle(self, *args, **kwargs):
        self.stdout.write('Test command successful !!') 