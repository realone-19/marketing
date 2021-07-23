from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField(primary_key=True)


    def __str__(self):
        return self.user.username


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfileInfo.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.userprofileinfo.save()


class Customer(models.Model):
    full_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    home_address = models.CharField(max_length=50)
    office_address = models.CharField(max_length=50)
    phone_number = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=30)
    next_of_kin = models.CharField(max_length=30)
    relationship = models.CharField(max_length=20)
    estate = models.CharField(max_length=30)
    plots = models.IntegerField()
    amount = models.IntegerField()
    amount_paid = models.IntegerField()
    balance = models.IntegerField()
    registration_date = models.DateField()
    deadline_date = models.DateField(default=date.today)
    payment_complete = models.BooleanField(default=False)
    documentation = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


class Account_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount_paid = models.IntegerField()
    date = models.DateField()
    reciept_number = models.IntegerField()
    balance = models.IntegerField()


    def __str__(self):
        return str(self.customer.full_name)
