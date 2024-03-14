from django.core.management.base import BaseCommand
from catalog.models import Country
from django_seed import Seed


class Command(BaseCommand):
    help = 'Generate 5 random Countries'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Country, 5)

        seeder.execute()