 
from rest_framework import serializers
from myapp.models import Listing


class Listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
