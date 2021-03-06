# Generated by Django 2.2.6 on 2019-10-19 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
                ('bed', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guests', models.IntegerField(default=1)),
                ('date_of_book', models.DateField()),
                ('is_cancel', models.BooleanField(default=False)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('checked_out', models.BooleanField(default=False)),
                ('guest_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Guest')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.Room')),
            ],
        ),
    ]
