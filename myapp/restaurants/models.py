from django.db import models


# Create your models here.
class Restaurants(models.Model):

    rest_id = models.IntegerField(null=False,blank = False)
    name = models.CharField(max_length = 500,null = False,blank = False)
    rest_type = models.CharField(max_length=100,null =True , blank =True)
    description = models.CharField(max_length=1000,null =True , blank =True)
    reviews = models.CharField(max_length=1000,null =True , blank =True)
    address = models.CharField(max_length=1000,null =True , blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Timings(models.Model):

    DAYS_OPTIONS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ]
    restaurants = models.ForeignKey(Restaurants,blank = True,null = True,on_delete=models.CASCADE)
    day = models.CharField(choices=DAYS_OPTIONS, max_length=10)
    open_time = models.TimeField(null = False,blank = False)
    close_time = models.TimeField(null = False,blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
