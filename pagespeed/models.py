from django.db import models
import datetime

from django.urls import reverse
from django.db import models

class Link(models.Model):
    tgt_url = models.CharField('Ссылка для проверки', max_length=500)
    