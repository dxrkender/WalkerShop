# Generated by Django 4.2.3 on 2023-11-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_clientaudiencecategory_alter_product_product_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientaudiencecategory',
            options={'verbose_name': 'Audience category', 'verbose_name_plural': 'Audience categories'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product category', 'verbose_name_plural': 'Product categories'},
        ),
        migrations.AlterField(
            model_name='clientaudiencecategory',
            name='audience_description',
            field=models.TextField(max_length=255),
        ),
    ]
