from django.urls import path
from .views import powerPlaceView,blogView,packageView,bookingView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blogs/', blogView.as_view(), name='blog-list'),
    path('places/', powerPlaceView.as_view(), name='powerplaces-list'),
    path('package/', packageView.as_view(), name='package-list'),
    path('user/', bookingView, name='booking-send'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)