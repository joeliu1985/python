#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import json
import urllib
import requests

def hostname(IP):
    url = 'https://ip.taobao.com/outGetIpInfo'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'ipAddress': IP}
    headers = {'User-Agent': user_agent}
    accessKey='alibaba-inc'
    req = requests.get(url+'?ip='+IP+'&accessKey='+accessKey, params =values, headers=headers)
    if(req.status_code==200):
        return req.json().get('data').get('city')



if __name__ == "__main__":
    b = hostname('204.9.36.126')
    print(b)