# Generated by Django 2.2.6 on 2019-10-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0006_auto_20191019_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_book',
            field=models.DateField(auto_now=True),
        ),
    ]