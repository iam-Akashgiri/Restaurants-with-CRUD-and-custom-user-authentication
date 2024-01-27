from django.db import models
import datetime

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    picture = models.ImageField()
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_foods_by_id(cart_food_id):
        return Food.objects.filter(id__in=cart_food_id)
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    
class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.today)

class BgImage(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self):
        return self.name
    