from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=20)


class Agent(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    photo=models.FileField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=50)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.FileField()
    age=models.IntegerField()
    phoneno = models.BigIntegerField()
    email = models.CharField(max_length=15)

class Complaint(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)

class Picup_Request(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    request=models.CharField(max_length=100)
    date = models.DateField()
    status=models.CharField(max_length=50)
    latitude=models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

class Work_assign(models.Model):
    AGENT = models.ForeignKey(Agent, on_delete=models.CASCADE)
    REQUEST= models.ForeignKey(Picup_Request, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)
    wtype=models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField()
    quantity = models.IntegerField()
    price=models.FloatField()
    description=models.CharField(max_length=500)


class Order(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50)
    amount = models.FloatField()

class Orderdetails(models.Model):
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    PRODUCT = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.IntegerField()
    quantity = models.IntegerField()

class Payment(models.Model):
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.FloatField()


class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    feedback = models.CharField(max_length=100)

class Waste(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image=models.FileField()
    # latitude = models.CharField(max_length=50)
    # longitude = models.CharField(max_length=50)


