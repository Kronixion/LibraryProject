# Generated by Django 3.0.4 on 2020-04-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20200425_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(upload_to='books/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]