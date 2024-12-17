import json
import requests
import os
from datetime import datetime


data_source_names = [
    "elasticsearch-breakdown",
    "elasticsearch-seat-assignments",
    "elasticsearch-seat-info-settings",
    "elasticsearch-total",
]

grafana_folder = 'grafana'
template_path = f'{grafana_folder}/dashboard-template.json'
model_output_path = f'{grafana_folder}/dashboard-model-{datetime.today().strftime("%Y-%m-%d")}.json'
mapping_output_path = f'{grafana_folder}/dashboard-model-data_sources_name_uid_mapping-{datetime.today().strftime("%Y-%m-%d")}.json'

grafana_url = os.getenv('GRAFANA_URL', 'http://localhost:3000/')
grafana_token = os.getenv('GRAFANA_TOKEN')

headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {grafana_token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
response = requests.get(grafana_url.rstrip('/')+'/api/datasources', headers=headers)

# sample data_resources
# data_resources = [
#       {
#     "id": 1,
#     "uid": "ee73owudpbim8f",
#     "orgId": 1,
#     "name": "elastcsearch-breakdown",
#     "type": "elasticsearch",
#     "typeName": "Elasticsearch",
#     "typeLogoUrl": "public/app/plugins/datasource/elasticsearch/img/elasticsearch.svg",
#     "access": "proxy",
#     "url": "http://localhost:9200",
#     "user": "",
#     "database": "",
#     "basicAuth": false,
#     "isDefault": true,
#     "jsonData": {
#       "includeFrozen": false,
#       "index": "copilot_usage_breakdown",
#       "logLevelField": "",
#       "logMessageField": "",
#       "maxConcurrentShardRequests": 5,
#       "timeField": "day",
#       "timeInterval": "1d"
#     },
#     "readOnly": false
#   },
# ]
data_resources = response.json()

data_sources_name_uid_mapping = {}
for data_resource in data_resources:
    name = data_resource['name']
    uid = data_resource['uid']
    data_sources_name_uid_mapping[name] = uid

# 保存映射关系的json文件，空格缩进为4
with open(mapping_output_path, 'w') as f:
    json.dump(data_sources_name_uid_mapping, f, indent=4)

with open(template_path, 'r') as template_file:
    template_content = template_file.read()

for data_source_name in data_source_names:
    uid = data_sources_name_uid_mapping.get(data_source_name)
    if not uid:
        print(f"Data source {data_source_name} not found, you must create it first")
        break
    uid_placeholder = f"{data_source_name}-uid"
    template_content = template_content.replace(uid_placeholder, uid)

with open(model_output_path, 'w') as output_file:
    output_file.write(template_content)