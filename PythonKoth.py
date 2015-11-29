__author__ = 'Nephtiry'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os, stat
import time
import datetime
import json

class Pyjson:
    def json(data_file):
        with open(r"C:\Users\Nephtiry\PycharmProjects\PythonKoth\Pythondata.json") as data_file:
            global data
            data = json.load(data_file)
            global label
            label = data["TopLabel"]
            global pages
            pages = data["Pages"]
            global imgn
            imgn = data["Imgname"]

Pyjson.json('data_file')


class create:
    def createDir(self):
        global ts
        ts = time.time()
        os.mkdir('C:\\temp\KothosTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')))
        global folder
        folder=('C:\\temp\KothosTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')))
        os.mkdir(folder+'\Screenshots')
        global screenfolder
        screenfolder=(folder+'\Screenshots')

    def createLog(txt):
        global filename
        filename=open(folder+'\KothosAutoTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M'))+'.log', 'a')

create.createDir('self')
create.createLog('txt')



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.thecityofkothos.com/')

class gather(Pyjson):
    def pyjs(self):
        for item in label:
            filename.write(item + '\n')

    def pyjs2(self):
        filename.write('\nReached Homepage--PASSED')
        print('Reached Homepage. Testing links...')
        for item in pages:
            driver.find_element_by_link_text(item).click()
            for name in imgn:
                if driver.find_elements_by_css_selector(name):
                    filename.write('Reached ' + item + '--PASSED\n')
                    print('Reached ' + item + '-PASSED\n')
                    driver.get('http://www.thecityofkothos.com/')
                else:
                    filename.write("ERROR: " + item + "NOT FOUND--TEST FAILED")
                    print("ERROR: " + item + "NOT FOUND--TEST FAILED")


gather.pyjs('self')
gather.pyjs2('self')


#driver.save_screenshot(folder+'\Screenshots'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')