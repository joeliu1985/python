#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Version = 3.5.2
import psutil

disk_used = {}

def get_disk_info():
    for id in psutil.disk_partitions():
        if 'cdrom' in id.opts or id.fstype == '':
            continue
        disk_name = id.device.split(':')
        s = disk_name[0]
        disk_info = psutil.disk_usage(id.device)
        # disk_used[s+'盘使用率：'] = '{}'.format(disk_info.percent)
        disk_used[s+'剩余空间：'] = '{}'.format(disk_info.free//1024//1024//1024)
    return disk_used

if __name__ == '__main__':
    ret = get_disk_info()
    for k, v in ret.items():

            print(v)
