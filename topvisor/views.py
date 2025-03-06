from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from topvisor.models import *
from django.views import View
import json
from django.core import serializers

def index(request):
    return HttpResponse('huh')

class AllResultsData(View):
    def get(self, request):
        queryset = MonitoringGroupResult.objects.all()
        data=[]
        for result in queryset:
            data.append({})
        return HttpResponse(data, content_type='application/json')
