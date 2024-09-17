from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
# your_app/views.py
from django.http import JsonResponse
from meters.api import get_api_data
from django.shortcuts import render
def electronic_meter_data_view(request):
    value = get_api_data()
    context = {'value': value}
    return render(request, 'meters/123.html', context)
# Create your views here.

