# Generated by Django 3.0.4 on 2020-04-29 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0007_remove_order_totalsum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='totalSum',
            field=models.IntegerField(default=0),
        ),
    ]
