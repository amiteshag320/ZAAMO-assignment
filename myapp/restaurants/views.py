from django.shortcuts import render
from restaurants import models as restaurants_models
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status, views, viewsets, mixins
from restaurants import serializers as restaurants_serializers
import requests
import datetime as dt
import json
# Create your views here.

list_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

@api_view(['POST'])
def creating_restaurants(request):
    res={}
    for i in range(100):
        res_satus = status.HTTP_200_OK
        response = requests.get("https://random-data-api.com/api/restaurant/random_restaurant")
        data = response.text
        res = json.loads(data)
        new_rest = restaurants_models.Restaurants()
        new_rest.rest_id = res['id']
        new_rest.name = res['name']
        new_rest.rest_type = res['type']
        new_rest.description = res['description']
        new_rest.reviews = res['review']
        new_rest.address = res['address']
        new_rest.save()
        time = res['hours']
        
        for day in time:
            new_time  = restaurants_models.Timings()
            new_time.restaurants = new_rest
            new_time.day = day
            new_time.open_time = dt.datetime.strptime(time[day]['opens_at'],'%H:%M %p').time()
            new_time.close_time = dt.datetime.strptime(time[day]['closes_at'],'%H:%M %p').time()
            new_time.save()
            new_rest.timings = new_time
            new_rest.save()  
    return JsonResponse(res,status = res_satus)

@api_view(['POST'])
def get_rest_information(request):
    res = {}
    res_status = status.HTTP_200_OK
    req_json = request.data
    rest_available = []
    time_format = dt.datetime.strptime(req_json['time'] ,'%H:%M %p').time()
    
    timing = restaurants_models.Timings.objects.filter(restaurants__rest_type = req_json['type'] , day = req_json['day'])
    for times in timing:
        if times.open_time <= time_format and  times.close_time >= time_format:
            rest_available.append(restaurants_serializers.RestaurantsSerializers(times.restaurants).data)
    
    if len(rest_available) > 0:
        res['data'] = rest_available
    else:
        res_status = status.HTTP_400_BAD_REQUEST
        res['error'] = "No restaurants available"
    return JsonResponse(res,status = res_status)

