# Generated by Django 4.2.3 on 2023-08-10 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256, verbose_name='Product')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start selling from')),
                ('sales', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Sales')),
                ('is_active', models.BooleanField(verbose_name='Is active')),
                ('cart_id', models.ManyToManyField(db_table='cart', related_name='user_cart', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.productcategory')),
            ],
        ),
    ]
