from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key = True)
    orderid = models.CharField(max_length = 50, default='')
    orderdate = models.DateField(null = True)
    deliverydate = models.DateField(null = True)
    deliverytype = models.CharField(max_length = 50, default='')
    userid = models.CharField(max_length = 50, default='')
    username = models.CharField(max_length = 50, default='')
    segment = models.CharField(max_length = 50, default='')
    city = models.CharField(max_length = 50, default='')
    upcity = models.CharField(max_length = 50, default='')
    country = models.CharField(max_length = 50, default='')
    area = models.CharField(max_length = 50, default='')
    productid = models.CharField(max_length = 50, default='')
    category = models.CharField(max_length = 50, default='')
    categorydetail = models.CharField(max_length = 100,default='')
    productname = models.CharField(max_length = 100,default='')
    sales = models.FloatField(null = True, default='')
    quantity = models.IntegerField(null = False, default='')
    discountrate = models.FloatField(null = True, default='')
    revenue = models.FloatField(null = False, default='')