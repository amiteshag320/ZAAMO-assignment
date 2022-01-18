from django.contrib import admin
from restaurants import models as restaurants_models

class RestaurantsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in restaurants_models.Restaurants._meta.fields]

class TimingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in restaurants_models.Timings._meta.fields]
    

# Register your models here.
admin.site.register(restaurants_models.Restaurants,RestaurantsAdmin)
admin.site.register(restaurants_models.Timings,TimingsAdmin)
