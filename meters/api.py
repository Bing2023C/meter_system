import requests
import json

url = 'http://39.99.163.66:8900/api/data/ReadMeterDatalist?token=23e31bf0-0a63-455a-af05-52d1f5d1a6bc'
data = {
    'MeterAddrList': '',
    'ReadType': '1',
    'BeginDate': '2024-02-05',
    'EndDate': '2024-02-05',
    'PageSize': '100',
    'PageIndex': '1',
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Set the 'Content-Type' header to 'application/json'
headers = {
    'Content-Type': 'application/json; charset=utf-8',
}
def get_api_data():
    response = requests.post(url, data=json_data, headers=headers)
    if response.status_code == 200:
        return response.json()  # 将API返回的JSON数据转换为Python字典或列表
    else:
        return None

