from django.db import models
import datetime

from django.urls import reverse
from django.db import models


class MonitoringGroup(models.Model):
    name_vertical = models.CharField('Название вертикали', max_length=200)
    name_Group = models.CharField('Название группы', max_length=200)
    name_product = models.CharField('Название Продукта', max_length=200, blank=True)
    domain = models.CharField('Домен для мониторинга', max_length=200)
    project_id = models.CharField('ID проекта в топвизор', max_length=200)
    searchengine = models.CharField('Поисковая система', max_length=200)
    region_index = models.CharField('Индекс региона', max_length=200)
    group_id = models.CharField('ID группы ключей', max_length=200)
    filterbygroup = models.BooleanField('Мониторинг без группы', default=False)
   
    def __str__(self):
        return self.domain +'|'+ self.name_vertical +'|'+ self.name_Group +'|'+ self.searchengine
    
class MonitoringGroupResult(models.Model):
    avg = models.CharField('Средняя позиция', max_length=200, blank=True)
    median = models.CharField('Медиана', max_length=200, blank=True)
    visibility = models.CharField('Видимость', max_length=200, blank=True)
    top1_3 = models.CharField('В ТОП3', max_length=200, blank=True)
    top1_10 = models.CharField('В ТОП10', max_length=200, blank=True)
    top11_30 = models.CharField('В ТОП11-30', max_length=200, blank=True)
    top31_50 = models.CharField('В ТОП30-50', max_length=200, blank=True)
    top51_100 = models.CharField('В ТОП50-100', max_length=200, blank=True)
    top101_1000 = models.CharField('В ТОП101-10000', max_length=200, blank=True)
    date_from_topvisor_from = models.CharField('Даты прилетевшие с топвизора c', max_length=200, blank=True)
    date_from_topvisor_to = models.CharField('Даты прилетевшие с топвизора по', max_length=200, blank=True)  
    date_sended_to_topvisor = models.CharField('Дата отправленная и от нее -7 дней', max_length=200, blank=True)
    group = models.ForeignKey(MonitoringGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date_sended_to_topvisor