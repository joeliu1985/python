import requests
import sys

url="https://api.bilibili.com/x/click-interface/web/heartbeat"
#Form data 格式
postData = {
    'aid': 35122164,
    'cid': 107464593,
    'bvid': 'BV1eb411P7tV',
    'mid': 17636028,
    'csrf':'b1382725b33244d5a1774390e1a14841',
    'played_time':1815,
    'real_played_time':1815,
    'start_ts':1608880593,
    'type':3,
    'dt':2,
    'play_type':0
}

response = requests.post(url,data=postData)
print(response.json())

assert response.json()['message']=='0'

assert ('win' in sys.platform)

