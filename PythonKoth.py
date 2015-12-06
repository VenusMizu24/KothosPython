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
            global btt
            btt = data["BTT"]
            global btt2
            btt2 = data["BTT2"]

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

class gather(Pyjson):
    def pyjs(self):
        for item in label:
            filename.write(item + '\n')

    def pyjs2(self):
        filename.write('\nReached Homepage--PASSED\n')
        print('Reached Homepage. Testing links...')
        for item in pages:
            driver.find_element_by_link_text(item).click()
            if driver.find_elements_by_tag_name('img'):
                filename.write('Reached ' + item + '--PASSED\n')
                print('Reached ' + item + '-PASSED')
                driver.get('http://www.thecityofkothos.com/')
            else:
                filename.write("ERROR: " + item + "NOT FOUND--TEST FAILED\n")
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print("ERROR: " + item + "NOT FOUND--TEST FAILED")

    def batt(self):
        driver.get('http://www.thecityofkothos.com/thePages/theChapterHeadings.shtml')
        driver.find_element_by_link_text('Back to Top').click()
        filename.write("Found 'Back To Top' link in Chapter Headings --PASSED\n")
        print("Found 'Back To Top' link in Chapter Headings --PASSED")

        for nav in btt:
            if driver.find_element_by_link_text("Back to Top").click:
                filename.write("Found 'Back To Top' link in " + nav + "--PASSED\n")
                print("Found 'Back To Top' link in " + nav + "--PASSED")
                for each in btt2:
                    driver.find_element_by_link_text(each).click()
            else:
                filename.write("ERROR: CANNOT FIND 'Back to Top' LINK IN " + nav + "-- TEST FAILED")
                print("ERROR: CANNOT FIND 'Back to Top' LINK IN " + nav + "-- TEST FAILED")

create.createDir('self')
create.createLog('txt')
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.thecityofkothos.com/')
gather.pyjs('self')
gather.pyjs2('self')
gather.batt('self')


