from rest_framework import serializers
from restaurants import models as restaurants_models

class TimingSerializers(serializers.ModelSerializer):
      class Meta:
        model = restaurants_models.Timings
        fields = "__all__"

class RestaurantsSerializers(serializers.ModelSerializer):
    class Meta:
        model = restaurants_models.Restaurants
        fields = "__all__"

