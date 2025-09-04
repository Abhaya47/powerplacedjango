from django.shortcuts import render
from rest_framework import generics
from .models import Blog, powerPlaces,Package,User, Booking
from .serializers import blogSerializer, powerPlacesSerializer,packageSerializer,userSerializer,bookingSerializer
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from datetime import datetime, timedelta

from django.views.decorators.csrf import csrf_exempt

class blogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer

class powerPlaceView(generics.ListAPIView):
    queryset = powerPlaces.objects.all()
    serializer_class = powerPlacesSerializer

class packageView(generics.ListAPIView):
    queryset= Package.objects.all()
    serializer_class = packageSerializer

@csrf_exempt
@api_view(('POST',))
@renderer_classes([JSONRenderer])
def bookingView(request):
    [...]
    data = request.data
    try:
        user= User.objects.get(email=data['email'])
        # serializer = userSerializer(user, data=userData, partial=True)
        # if !serializer.is_valid():
        #     return Response(serializer.errors, status=400)
        # serializer.save()                 
    except User.DoesNotExist:
        serializer = userSerializer(data=userData)
        if not (serializer.is_valid()):
            return Response({"message" : "User info not clear"}, status=400)    
        serializer.save()
    
    bookingData={
        "title":data["packageTitle"],
        "startDate":data["startDate"]
    }
    try:
        Bookingadd(data['email'],bookingData)
        return Response({"message" : "Booked"})
    except:
        return Response({"message" : "Some problem in booking data. check date and package"}, status=400)

def Bookingadd(userData,bookingData):
    user= User.objects.get(email=userData)
    package= Package.objects.get(packageTitle=bookingData["title"])
    endDate = datetime.strptime(bookingData["startDate"], "%Y-%m-%d").date()+timedelta(days=int(package.duration-1)) 
    try:
        availability = Booking.objects.get(
            startDate__gte=bookingData["startDate"], 
            endDate__lte=endDate
        )
        raise ValidationError("Date is not available")

    except Booking.DoesNotExist:
        serializer = bookingSerializer(data={
            "userID": user.userID,    
            "packageID": package.packageID, 
            "startDate":bookingData["startDate"],
            "endDate":endDate})
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        raise ValidationError(serializer.errors)
    
