from celery import shared_task
from topvisor.models import  *
import requests
from datetime import date, datetime, timedelta
import json
import logging

logger = logging.getLogger(__name__)

@shared_task
def add():
    headers = {
        'User-Id': '12685',
        'Authorization': 'f0b60f119642340f556b4ff05cd357ec'
        }
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
        response = requests.post('https://api.topvisor.com/v2/json/get/positions_2/summary?project_id=8314284', json=data, headers=headers)
        print('2',response)
        print(data)
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
            print('saved')
        print('3')

@shared_task
def create_issue_bankiros(summary,description,component,assignee):
    logger.info(summary,description,component,assignee)
    print(summary,description,component,assignee)
    try:
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer perm:0JrQuNGA0LjQu9C7X9Ci0LXRgNC10YnRg9C6.NTYtMjM=.e7p34zrnxkA3l3LBWKTXwuu0zEUxCl',
            'Content-Type': 'application/json'
            }
        data = {  
            "project":{
                "id":"0-6",
                },
            "summary":summary,
            "description":description,
            "customFields":[
                { "name":"Компонент","$type":"MultiOwnedIssueCustomField","value":json.loads(component)},
                { "name": "Assignee","$type": "SingleUserIssueCustomField","value":json.loads(assignee)}
                ]
        }
        print(data)
        response = requests.post('https://youtrack.myfin.group/api/issues', data=json.dumps(data), headers=headers)
        print(response.content)
        if response.status_code == 200:
            res_payload_dict = response.json()
            print(res_payload_dict)
    except Exception as e:
        logger.info(e)
        return(summary,description,component,assignee)
    return 'str(response.content) + str(data)'

# data = {  
#     "project":{
#         "id":"0-6",
#         },
#     "summary":"REST API lets you create issues!",
#     "description":"Let REST API.",
#     "customFields":[
#         { "name":"Компонент","$type":"MultiOwnedIssueCustomField","value":[{"name":"SEO","$type":"OwnedBundleElement"}]},
#         { "name": "Assignee","$type": "SingleUserIssueCustomField","value": {'name': 'Кирилл Терещук', 'id': '1-305', '$type': 'User'}}
#         ]
# }


# {"summary":"test","description":"test","component":[{"name":"SEO","$type":"OwnedBundleElement"}],"assignee":{'name': 'Кирилл Терещук', 'id': '1-305', '$type': 'User'}}
