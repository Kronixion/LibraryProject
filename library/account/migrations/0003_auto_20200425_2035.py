# Generated by Django 3.0.4 on 2020-04-25 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200425_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='order',
        ),
        migrations.RemoveField(
            model_name='account',
            name='shoppingCart',
        ),
    ]
