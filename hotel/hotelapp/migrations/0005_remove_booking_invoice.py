# Generated by Django 2.2.6 on 2019-10-18 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0004_auto_20191018_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Invoice',
        ),
    ]