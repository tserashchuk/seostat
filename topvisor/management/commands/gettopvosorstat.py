from django.core.management.base import BaseCommand
from topvisor.models import  *
import requests
from datetime import date, datetime, timedelta

class Command(BaseCommand):
    help = "collect stats"  
    headers = {
        'User-Id': '12685',
        'Authorization': 'f0b60f119642340f556b4ff05cd357ec'
        }
    
    # определяем логику команд

    def handle(self, *args, **options):
        
        groups = MonitoringGroup.objects.all()
        today7 = datetime.today() - timedelta(days=7)
        for group in groups:
            data = {
                "project_id": group.project_id,
                "region_index": group.region_index,

                "dates": [
                    today7.strftime("%Y-%m-%d"),
                    date.today().strftime("%Y-%m-%d"),
                ],
              
                'show_tops':1,
                'show_avg':1,
                'show_median':1,
                "show_visibility":1,
                }   
            print('1')
            if not group.filterbygroup:
                data['filters'] = [{"name": 'group_id',"operator":'EQUALS',"values":[group.group_id]},]
            response = requests.post('https://api.topvisor.com/v2/json/get/positions_2/summary?project_id=8314284', json=data, headers=self.headers)
            print('2',response)
            if response.status_code == 200:
                res_payload_dict = response.json()
                new_record = MonitoringGroupResult(
                    avg=res_payload_dict['result']['avgs'][-1], 
                    median =res_payload_dict['result']['medians'][-1], 
                    visibility = res_payload_dict['result']['visibilities'][-1], 
                    top1_3 =  res_payload_dict['result']['tops'][-1]['1_3'],
                    top1_10 =  res_payload_dict['result']['tops'][-1]['1_10'],
                    top11_30 =  res_payload_dict['result']['tops'][-1]['11_30'],
                    top31_50 =  res_payload_dict['result']['tops'][-1]['31_50'],
                    top51_100 =  res_payload_dict['result']['tops'][-1]['51_100'],
                    top101_1000 =  res_payload_dict['result']['tops'][-1]['101_10000'],
                    date_from_topvisor_from = res_payload_dict['result']['dates'][0],
                    date_from_topvisor_to = res_payload_dict['result']['dates'][1],
                    date_sended_to_topvisor =  date.today().strftime("%Y-%m-%d"),
                    group=group
                    )
                new_record.save()
            print('3')    
        # собираем html
