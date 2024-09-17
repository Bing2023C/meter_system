import requests
import json
import sqlite3

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
response = requests.get(api_url)

# 解析响应数据为JSON（这里假设API返回的是一个字典列表）
data = response.json()

# 连接到SQLite数据库
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 确保在插入数据之前数据库表已经存在
# 以下SQL命令仅作示例，根据你的实际表结构可能需要调整
cursor.execute('''CREATE TABLE IF NOT EXISTS data_table (
                meter_address TEXT,
                meter_number TEXT,
                read_date TEXT,
                valve_status TEXT,
                voltage REAL,
                csq INTEGER,
                imei TEXT,
                battery_voltage REAL,
                attack_state TEXT)''')

# 遍历数据，将每项插入数据库
for item in data:
    cursor.execute('''INSERT INTO data_table (meter_address, 
                   meter_number, read_date, valve_status, voltage, 
                   csq, imei, battery_voltage, attack_state)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (item['meteraddr'], item['meternumber'], item['readdate'], item['valvestatus'], item['voltage'], item['csq'], item['imei'], item['batteryvoltage'], item['attackstate']))

# 提交事务
conn.commit()

# 关闭连接
cursor.close()
conn.close()
