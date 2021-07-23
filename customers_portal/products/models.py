from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    category = models.CharField(max_length=30)
    locaton = models.CharField(max_length=255)
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    likes = models.IntegerField()


    def like(self):
        self.likes = self.likes + 1


class Prospect(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    estate_of_interest = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    office_address = models.CharField(max_length=200)
    home_address = models.CharField(max_length=200)
    # date = models.DateField(default=date.today)
