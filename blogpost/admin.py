from django.contrib import admin

# Register your models here.

from .models import powerPlaces, Blog, User, Package, Booking



admin.site.register(powerPlaces)
admin.site.register(Blog)
admin.site.register(Package)
admin.site.register(User)
admin.site.register(Booking)

