# -*- coding:utf-8*-
import os
import os.path
import time

from qilinv10.info import Info

time1 = time.time()


def MergeTxt(rootdir, outfile):
    k = open(rootdir + outfile, 'a+')
    filegroup = []
    for parent, dirnames, fileList in os.walk(rootdir):  # 返回三元数组
        for file in fileList:
            txtPath = os.path.join(parent, file)
            f = open(txtPath)
            oneline = f.read()
            if len(oneline.split("\t")) > 5:
                emp1 = Info(oneline, oneline.split("\t")[5])
                filegroup.append(emp1)
            k.write(oneline)
    k.close()
    k = open("D:/info/sortinfo.txt" , 'a+')
    for i in sorted(filegroup, key=lambda u: u.ip):
        k.write(i.str)

    print("finished")


if __name__ == '__main__':
    rootdir = "D:/info/"
    outfile = "result.txt"
    MergeTxt(rootdir, outfile)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')
