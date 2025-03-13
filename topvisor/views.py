from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from topvisor.models import *
from django.views import View
import json
import requests


def index(request):
    url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://beleuroprivod.by/&strategy=mobile&locale=ru&key=AIzaSyA8d1Veeg04Uj_LPIgyu3oqf89z-CIVmBM"
    
    response = requests.get(url)
    return_text = response.text
    data = json.loads(return_text)
    li = data['lighthouseResult']
    return HttpResponse(data['lighthouseResult'], content_type='application/json')

class AllResultsData(View):
    def get(self, request):
        queryset = MonitoringGroupResult.objects.all()
        data=[]
        for result in queryset:
            data.append({})
        return HttpResponse(data, content_type='application/json')
