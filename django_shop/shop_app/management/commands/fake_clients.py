from django.core.management.base import BaseCommand
from shop_app.models import Client, Goods, Order


class Command(BaseCommand):
    help = "Generate fake Clients, Goods and Orders."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name{i}', email=f'email{i}@mail.ru',
                            phone=i * 1_000_000, address=f'address{i}')
            goods = Goods(name=f'name{i}', description=f'description{i}', price=i * 1_000, amount=i)
            client.save()
            goods.save()
            for j in range(1, count + 1):
                order = Order(client_id=client, goods_id=goods, price=goods.total_price())
                order.save()