from django.urls import path
from .views import electronic_meter_data_view

urlpatterns = [
    path('', electronic_meter_data_view),
    ]
