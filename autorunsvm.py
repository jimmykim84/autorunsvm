#!/usr/bin/env python
# -*- coding: utf-8 -*-

' Cross platform automatic batch execution LibSVM under Python '

__author__ = 'Jimmykim'

import glob, os, time, sys  

#os.chdir('/Users/jimmykim/Documents/libsvm-3.21/tools/test/')

import subprocess
import platform

sysstr = platform.system()

if(sysstr=="Windows"):
    # Windows
    filesRead = r"C:\libsvm\tools\test\*.txt" # your libsvm data path
    subsetpath = r"C:\libsvm\tools\test\subset.py"
    easypath = r"C:\libsvm\tools\test\easy.py"
else:
    # Mac
    filesRead = r"/Users/jimmykim/Documents/libsvm-3.21/tools/test/*.txt"
    subsetpath = r"/Users/jimmykim/Documents/libsvm-3.21/tools/test/subset.py"
    easypath = r"/Users/jimmykim/Documents/libsvm-3.21/tools/test/easy.py"
    
m = 11 # 10 times validations
ts = 600 # train sample num
  
if __name__ == '__main__':  
    list = glob.glob(filesRead)

    start = time.time()
    # print list
    for name in list:
        txtFileName = name[0:-4]
        showname =os.path.basename(txtFileName)
        for j in range(1,m,1):
            trainName = '%s_train_%d_.txt'%(txtFileName,j)
            testName = '%s_test_%d_.txt'%(txtFileName,j)
            resultName = '%s_result_%d_.txt'%(txtFileName,j)
            subprocess.call("python %s %s %d %s %s"%(subsetpath,name,ts,trainName,testName),shell=True)
        for j in range(1,m,1):
            print '第 %2d 次对 %s 数据进行分类'%(j,showname)
            trainName = '%s_train_%d_.txt'%(txtFileName,j)
            testName = '%s_test_%d_.txt'%(txtFileName,j)
            resultName = '%s_result_%d_.txt'%(txtFileName,j)   # output 
            #print "python %s %s %s >> %s"%(easypath,trainName,testName,resultName)
            subprocess.call("python %s %s %s >> %s"%(easypath,trainName,testName,resultName),shell=True)
    end = time.time()
    print "spend time: %f s" % (end - start)


