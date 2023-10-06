import django
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=254, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}, {self.phone}, {self.address}'


class Goods(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField(default=0)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    def total_price(self):
        return self.price * self.amount

    @property
    def all_fields(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "amount": self.amount,
            "date": self.create_at,
            "image": self.image,
        }

    def __str__(self):
        return f'{self.name} {self.description} {self.price} {self.amount} {self.create_at}'


class Order(models.Model):
    # client_id = models.ForeignKey(
    #     to=Client, on_delete=models.CASCADE, related_name="orders"
    # )
    client = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.Client')
    goods = models.ManyToManyField(to=Goods, related_name="goods")
    price = models.DecimalField(max_digits=15, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    date_edit_create_at = models.DateTimeField(auto_now=True)

    goods_id = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.Goods')

    def __str__(self):
        return f'{self.client_id}, {self.goods}, {self.price}, {self.goods_id}'