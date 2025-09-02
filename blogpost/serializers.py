from rest_framework import serializers
from .models import Blog,powerPlaces,Package,User,Booking

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'title',
            'description',
            'pubDate'
        )

class powerPlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = powerPlaces
        fields = (
            'title',
            'description'
        )

class packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = (
            'packageTitle',
            'description',
            'duration'
        )

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'phone'
        )

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'bookingID',
            'userID',
            'packageID',
            'startDate',
            'endDate'
        )
