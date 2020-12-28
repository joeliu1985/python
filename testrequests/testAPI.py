import requests
import sys
import json
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

response = requests.post(url,data=postData,headers={'Content-Type':'application/x-www-form-urlencoded'})
print(response.json())

assert response.json()['message']=='0'

assert ('win' in sys.platform)

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
httpurl = "http://jinbao.pinduoduo.com/network/api/common/goodsList"
pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}

r=requests.post(url=httpurl,json=json.dumps(pyload),headers=headers).text

print(r)
print(json.loads(r))


