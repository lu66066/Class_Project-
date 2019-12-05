import csv
from django.core.management.base import BaseCommand
from adopt.models import Pet

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader=csv.DictReader(fp)
            data=list(reader)

        for item in data:
            p=Pet(
            species=item['species'],
            birth_date=item['birthdate'],
            sex=item['sex'],
            )
            p.save()
