# Generated by Django 4.2 on 2023-04-22 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='amera-asdaksdsad', unique=True),
            preserve_default=False,
        ),
    ]
