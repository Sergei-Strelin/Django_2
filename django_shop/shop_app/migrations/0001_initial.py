from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=254)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.IntegerField(default=0)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('date_edit_create_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.client')),
                ('goods', models.ManyToManyField(related_name='goods', to='shop_app.goods')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.goods')),
            ],
        ),
    ]