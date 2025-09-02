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
    userData={
        "name":data['name'],
        "email":data['email'],
        "phone":data['phone']
    }
    bookingData={
        "title":data["packageTitle"],
        "startDate":data["startDate"]
    }
    try:
        user= User.objects.get(email=userData["email"])
        serializer = userSerializer(user, data=userData, partial=True)
        if serializer.is_valid():
            serializer.save()
            Bookingadd(userData,bookingData)
            return Response({"message": "User updated", "data": serializer.data})
        return Response(serializer.errors, status=400)    

    except User.DoesNotExist:
        serializer = userSerializer(data=userData)
        if serializer.is_valid():
            serializer.save()
            Bookingadd(userData,bookingData)
            return Response({"message": "User Created and booked", "data": serializer.data})
        return Response(serializer.errors, status=400)    

def Bookingadd(userData,bookingData):
    user= User.objects.get(email=userData["email"])
    package= Package.objects.get(packageTitle=bookingData["title"])
    tmp=int(package.duration-1)
    startDate = datetime.strptime(bookingData["startDate"], "%Y-%m-%d").date()    
    endDate=startDate + timedelta(days=tmp)
    tempData={
        "userID": user.userID,    
        "packageID": package.packageID, 
        "startDate":bookingData["startDate"],
        "endDate":endDate
    }

    serializer = bookingSerializer(data=tempData)
    if serializer.is_valid():
        serializer.save()
        return 
    print(serializer.errors)
    return     