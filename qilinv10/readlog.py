# -*- coding:utf-8*-
import os
import os.path
import time

time1 = time.time()


def MergeTxt(rootdir, outfile):
    k = open(rootdir + outfile, 'a+')
    for parent, dirnames, fileList in os.walk(rootdir):#返回三元数组
        for file in fileList:
            txtPath = os.path.join(parent, file)
            f = open(txtPath)
            line=f.read()
            print(line)
            k.write(line)
    k.close()
    print("finished")


if __name__ == '__main__':
    rootdir = "D:/info/"
    outfile = "result.txt"
    MergeTxt(rootdir, outfile)
    time2 = time.time()
    print(u'总共耗时：' + str(time2 - time1) + 's')
