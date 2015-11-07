__author__ = 'Nephtiry'
from selenium import webdriver
import os
import time
import datetime
import json

class create:
    def createDir(self):
        global ts
        ts = time.time()
        os.mkdir('C:\\temp\KothosTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')))
        global folder
        folder=('C:\\temp\KothosTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')))
        os.mkdir(folder+'\Screenshots')
        screenfolder=(folder+'\Screenshots')

    def createLog(txt):
        filename=open(folder+'\KothosAutoTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M'))+'.log', 'w+')

create.createDir('self')
create.createLog('txt')





driver = webdriver.Chrome()
driver.get('http://www.thecityofkothos.com/')