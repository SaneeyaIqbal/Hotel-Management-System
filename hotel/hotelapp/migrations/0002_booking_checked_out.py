# Generated by Django 2.2.6 on 2019-10-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checked_out',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]