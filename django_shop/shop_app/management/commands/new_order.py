# from _decimal import ROUND_DOWN
from django.core.management.base import BaseCommand
from shop_app.models import Client, Goods, Order
# from faker import Faker
from decimal import Decimal


class Command(BaseCommand):
    help = "Create new order"

    def add_arguments(self, parser):
        # faker = Faker(locale='ru-ru')
        parser.add_argument('--client_id', default=1, type=int, help='Client ID')
        parser.add_argument('--goods_id', default=1, type=int, help='Goods ID')
        parser.add_argument('--amount', default=3, type=int, help='Count of goods in order')

    def handle(self, *args, **kwargs):
        client_pk = kwargs.get('client_id')
        good_pk = kwargs.get('goods_id')
        amount = Decimal(kwargs.get('amount'))
        client = Client.objects.filter(pk=client_pk).first()
        goods = Goods.objects.filter(pk=good_pk).first()
        # total_price = self.__total_price(goods=goods, amount=amount)
        total_price = self.__total_price(goods, amount)

        new_order = Order.objects.create(
            client=client,
            goods=goods,
            price=total_price,
        )
        self.stdout.write(f'Order {new_order.pk} created,  Total price {total_price}')

    @staticmethod
    def __total_price(goods, amount):
        total = goods.price * amount
        return total