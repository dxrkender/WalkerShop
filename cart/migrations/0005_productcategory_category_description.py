# Generated by Django 4.2.3 on 2023-11-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_audiencecategory_productsubcategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_description',
            field=models.TextField(default='Category of products', max_length=255),
        ),
    ]