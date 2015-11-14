__author__ = 'Nephtiry'
from selenium import webdriver
import os
import time
import datetime
import json
from pprint import pprint

class Pyjson:
    def json(data_file):
        with open(r"C:\Users\Nephtiry\PycharmProjects\PythonKoth\Pythondata.json") as data_file:
            global data
            data = json.load(data_file)
            global label
            label = data["TopLabel"]
            pprint(data)

Pyjson.json('data_file')

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
        global filename
        filename=open(folder+'\KothosAutoTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M'))+'.log', 'a')

create.createDir('self')
create.createLog('txt')

class gather(Pyjson):
    def pyjs(self):
        for item in label:
            filename.write(item + '\n')

gather.pyjs('self')

driver = webdriver.Chrome()
driver.get('http://www.thecityofkothos.com/')