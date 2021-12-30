#!/bin/env python
# -*- coding: UTF-8 -*-
import requests
import sys
try:
    qheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)", "Connection": "close"}
    html = requests.get("http://www.netseah.com/" ,headers=qheaders)
    code = html.status_code
    print(code)

except:
    print(1)
    sys.exit(0)
