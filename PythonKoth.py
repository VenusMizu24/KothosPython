__author__ = 'Nephtiry'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os, stat
import time
import datetime
import json
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.QtGui import *
import sys

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
            global cloop
            cloop = data["Creston"]
            global crestgall
            crestgall = data["CrestonGallary"]
            global colorgal
            colorgal = data ["ColorGall"]
            global BWgall
            BWgall = data["BWGall"]

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

    def crest(self):
        for sub in cloop:
            driver.get('http://www.thecityofkothos.com/thePages/Creston.shtml')
            if driver.find_element_by_link_text(sub).click:
                filename.write("Found " + sub + " link--PASSED\n")
                print("Found " + sub + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED')
        driver.get('http://www.thecityofkothos.com/thePages/BowandArrow.shtml')
        if driver.find_element_by_link_text("Back to top").click:
            filename.write("Found Back to Top link in Bow and Arrow page--PASSED\n")
            print("Found Back To Top link in Bow and Arrow page--PASSED")
        else:
            filename.write('ERROR: CANNOT FIND Back to Top LINK-- TEST FAILED')
            print('ERROR: CANNOT FIND Back To Top LINK-- TEST FAILED')

    def crestg(self):
        for page in crestgall:
            driver.get('http://www.thecityofkothos.com/CrestonComic/ccPages/CrestonComic_Cover.html')
            if driver.find_element_by_link_text(page).click:
                filename.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')

    def colorgall(self):
        for page in colorgal:
            driver.get('http://www.thecityofkothos.com/GallaryBW/BW_Pages_v2/BW_Female_Male.shtml')
            if driver.find_element_by_link_text(page).click:
                filename.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')


    def BWgall(self):
        for each in BWgall:
            driver.get('http://www.thecityofkothos.com/GallaryColor/Color_Pages/WizardandDrib.shtml')
            if driver.find_element_by_link_text(each).click:
                driver.implicitly_wait(10)
                filename.write("Found " + each + " link--PASSED\n")
                print("Found " + each + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + each + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + each + '-- TEST FAILED')


class Success(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        popup = QtGui.QVBoxLayout()

        self.setWindowTitle('Finished!')
        label = QLabel("Browser test done!\n\nThe log file and any error screenshots are in your temp folder.")
        popup.addWidget(label)
        self.setLayout(popup)

class Chrome():
    def gcvers(self):
        create.createDir('self')
        create.createLog('txt')
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        global driver
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://www.thecityofkothos.com/')
        gather.pyjs('self')
        gather.pyjs2('self')
        gather.batt('self')
        gather.crest('self')
        gather.crestg('self')
        gather.colorgall('self')
        gather.BWgall('self')
        driver.quit()
        global popup
        popup = Success()
        popup.exec()

class Browserbutton(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QtGui.QVBoxLayout()

        label = QLabel("Welcome to The City of Kothos testing module!\nWhich browser do you want to test?")
        GCbutton = QPushButton("Google Chrome")
        MFbutton = QPushButton("Mozilla Firefox")
        IEbutton = QPushButton("Internet Explorer")
        MEbutton = QPushButton("Microsoft Edge")
        closebutton = QPushButton("Exit")

        self.setWindowTitle('City of Kothos')
        layout.addWidget(label)
        layout.addWidget(GCbutton)
        layout.addWidget(MFbutton)
        layout.addWidget(IEbutton)
        layout.addWidget(MEbutton)
        layout.addWidget(closebutton)


        self.setLayout(layout)

        GCbutton.clicked.connect(Chrome.gcvers)
        closebutton.clicked.connect(self.close)

app = QApplication(sys.argv)
dialog = Browserbutton()
dialog.show()
app.exec()