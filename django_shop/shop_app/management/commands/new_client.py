from django.core.management.base import BaseCommand
from shop_app.models import Client
from faker import Faker


class Command(BaseCommand):
    help = "Create new client"

    def add_arguments(self, parser):
        faker = Faker('ru-ru')
        parser.add_argument('--name', default=faker.name(), type=str, help='Name of client')
        parser.add_argument('--email', default=faker.email(), type=str, help='Email')
        parser.add_argument('--phone', default=faker.phone_number(), type=str, help='Phone')
        parser.add_argument('--address', default=faker.address(), type=str, help='Phone')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')

        new_client = Client.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        self.stdout.write(f'Client {new_client.name} created')