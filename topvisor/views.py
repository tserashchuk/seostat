from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from topvisor.models import *
from django.views import View
import json
import requests


def index(request):
    return HttpResponse('huh')

