# Generated by Django 3.0.4 on 2020-04-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200425_1603'),
        ('purchases', '0002_remove_order_orderstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='books',
        ),
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(to='book.Book'),
        ),
    ]
