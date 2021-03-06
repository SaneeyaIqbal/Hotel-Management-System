from django.db import models
from datetime import date, timedelta, datetime
from django.db.models import signals
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

#Create your models here.


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    def get_title(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField(null=True,blank = True)

    def __str__(self):
        return str(self.name)

    def get_name(self):
        return str(self.name)


class Room(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=20)
    bed = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    availability = models.BooleanField(default=True)

    def room_price(self):
        if self.type == 'A':
            return 1000
        elif self.type == 'B':
            return 2000
        elif self.type == 'C':
            return 3000

    def __str__(self):
        return str(self.number)

    def get_room_number(self):
        return self.number

    def get_bed(self):
        return self.bed

    def checked_out(self):
        if self.number > 0:
            return True
        else:
            return False

    checked_out.boolean = True
    checked_out.short_description = 'checked_out'


class Guest(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return str(self.name)


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    guest_name = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_of_stay_days = models.IntegerField(default=1)
    guests = models.IntegerField(default=1)
    date_of_book = models.DateField(auto_now=True)
    is_cancel = models.BooleanField(default=False)
    check_in = models.DateField()
    check_out = models.DateField()
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return str(self.guest_name)

    def check_out_date(self):
        return self.check_in + timedelta(days=self.check_in + self.check_out)

    def room_number_detail(self):
        return self.room.room_number

    def room_type(self):
        return self.room.type

    def room_price_per_night(self):
        return self.room.price()

    def guest_name_detail(self):
        return self.guest.name

    def contact_number(self):
        return self.guest.number

    def cost(self):
        return self.number_of_stay_days * self.room.price()

    def bill(self):
        day = 0
        invoice = self.room_number.price
        if (self.check_out - self.check_in).days == 0:
            day = 1
        else:
            day = (self.check_out - self.check_in).days

        return day * invoice


@receiver(signals.post_save,sender=Booking)
def update(sender,instance,created,**kwargs):
    if not instance.check_out:
        if created:
            avail = instance.check_in.availability
            if avail > 0:
                avail -= 1
                room = instance.check_in
                room.availability = avail
                if avail <= 0:
                    room.availability = False
                room.save()

        else:
            avail = instance.check_in.availability
            room = instance.check_in
            room.availability = avail + 1
            room.save()


