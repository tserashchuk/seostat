from rest_framework import  serializers, viewsets, status
from rest_framework.routers import DefaultRouter
from topvisor.models import *



class MonitoringGroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = MonitoringGroup
            fields = ('name_vertical', 'name_Group', 'domain','searchengine')




class MonitoringGroupResultSerializer(serializers.ModelSerializer):
    group = MonitoringGroupSerializer()

    class Meta:
        model = MonitoringGroupResult
        fields = ("avg", "median", "visibility", "top1_3", "top1_10",  "top11_30",  "top31_50",  "top51_100",  "top101_1000",  "date_from_topvisor_from",  "date_from_topvisor_to",  "date_sended_to_topvisor",  "group")
        extra_kwargs = {'group': {'required': False}}



class MonitoringGroupResultViewSet(viewsets.ModelViewSet):
    queryset = MonitoringGroupResult.objects.all()
    serializer_class = MonitoringGroupResultSerializer

router = DefaultRouter()
router.register(r'results', MonitoringGroupResultViewSet, basename='user')