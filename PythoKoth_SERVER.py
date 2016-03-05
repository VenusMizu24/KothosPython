from re import A

__author__ = 'Nephtiry'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
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
            global form
            form = data["Contact"]
            global infm
            infm = data["Info"]

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
                driver.get('http://ramses/index.shtml')
            else:
                filename.write("ERROR: " + item + "NOT FOUND--TEST FAILED\n")
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print("ERROR: " + item + "NOT FOUND--TEST FAILED")

    def batt(self):
        driver.get('http://ramses/thePages/theChapterHeadings.shtml')
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
            driver.get('http://ramses/thePages/Creston.shtml')
            if driver.find_element_by_link_text(sub).click:
                filename.write("Found " + sub + " link--PASSED\n")
                print("Found " + sub + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED')

        driver.get('http://ramses/thePages/BowandArrow.shtml')
        if driver.find_element_by_link_text("Back to top").click:
            filename.write("Found Back to Top link in Bow and Arrow page--PASSED\n")
            print("Found Back To Top link in Bow and Arrow page--PASSED")
        else:
            filename.write('ERROR: CANNOT FIND Back to Top LINK-- TEST FAILED')
            print('ERROR: CANNOT FIND Back To Top LINK-- TEST FAILED')


        driver.get('http://ramses/thePages/PriceOfAVisit.shtml')
        if driver.find_element_by_link_text("Back to top").click:
            filename.write("Found Back to Top link in A Price of A Visit page--PASSED\n")
            print("Found Back To Top link in A Price of a Visit page--PASSED")
        else:
            filename.write('ERROR: CANNOT FIND Back to Top LINK-- TEST FAILED')
            print('ERROR: CANNOT FIND Back To Top LINK-- TEST FAILED')



    def crestg(self):
        for page in crestgall:
            driver.get('http://ramses/CrestonComic/ccPages/CrestonComic_Cover.shtml')
            driver.find_element_by_name(page).click()
            if driver.find_element_by_link_text(page).click:
                filename.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')

    def colorgall(self):
        for page in colorgal:
            driver.get('http://ramses/GallaryColor/Color_Pages/WizardandDrib.shtml')
            driver.find_element_by_name(page).click()
            if driver.find_element_by_name(page).click:
                filename.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')

    def BWgall(self):
        for each in BWgall:
            driver.get('http://ramses/GallaryBW/BW_Pages_v2/BW_Female_Male.shtml')
            driver.find_element_by_name(each).click()
            if driver.find_element_by_name(each).click:
                driver.implicitly_wait(10)
                filename.write("Found " + each + " link--PASSED\n")
                print("Found " + each + " link--PASSED")
            else:
                filename.write('ERROR: CANNOT FIND ' + each + '-- TEST FAILED')
                print('ERROR: CANNOT FIND ' + each + '-- TEST FAILED')

    def contact(self):
        driver.get("http://ramses/contactMe/Questionaire.shtml")
        field = driver.find_element_by_name("firstname")
        field.click()
        field.send_keys("John")
        if field.send_keys:
            filename.write("Verified FIRST NAME text entry")
            print ("Verified FIRST NAME text entry")
        else:
            filename.write('ERROR: FIRST NAME not entered!')
            print ("ERROR: FIRST NAME not entered!")
        field1 = driver.find_element_by_name("lastname")
        field1.click()
        field1.send_keys("Doe")
        if field1.send_keys:
            filename.write("Verified LAST NAME text entry")
            print ("Verified LAST NAME text entry")
        else:
            filename.write('ERROR: LAST NAME not entered!')
            print ("ERROR: LAST NAME not entered!")
        field2 = driver.find_element_by_name("email")
        field2.click()
        field2.send_keys("johndoe123@gmail.com")
        if field2.send_keys:
            filename.write("Verified EMAIL text entry")
            print ("Verified EMAIL text entry")
        else:
            filename.write('ERROR: EMAIL not entered!')
            print ("ERROR: EMAIL not entered!")
        field3 = driver.find_element_by_name("stAddress")
        field3.click()
        field3.send_keys("123 Nevada Ave.")
        if field3.send_keys:
            filename.write("Verified STREET ADDRESS text entry")
            print ("Verified STREET ADDRESS text entry")
        else:
            filename.write('ERROR: STREET ADDRESS not entered!')
            print ("ERROR: STREET ADDRESS not entered!")
        field4 = driver.find_element_by_name("city")
        field4.click()
        field4.send_keys("Las Vegas")
        if field4.send_keys:
            filename.write("Verified CITY text entry")
            print ("Verified CITY text entry")
        else:
            filename.write('ERROR: CITY not entered!')
            print ("ERROR: CITY not entered!")
        field5 = driver.find_element_by_name("zip")
        field5.click()
        field5.send_keys("91082")
        if field5.send_keys:
            filename.write("Verified ZIP CODE text entry")
            print ("Verified ZIP CODE text entry")
        else:
            filename.write('ERROR: ZIP CODE not entered!')
            print ("ERROR: ZIP CODE not entered!")
        field6 = driver.find_element_by_name("country")
        field6.click()
        field6.send_keys("United States")
        if field6.send_keys:
            filename.write("Verified COUNTRY text entry")
            print ("Verified COUNTRY text entry")
        else:
            filename.write('ERROR: COUNTRY not entered!')
            print ("ERROR: COUNTRY not entered!")
        field7 = driver.find_element_by_name("phone")
        field7.click()
        field7.send_keys("123-456-7890")
        if field7.send_keys:
            filename.write("Verified PHONE NUMBER text entry")
            print ("Verified PHONE NUMBER text entry")
        else:
            filename.write('ERROR: PHONE NUMBER not entered!')
            print ("ERROR: PHONE NUMBER not entered!")
        field8 = driver.find_element_by_name("comment")
        field8.click()
        field8.send_keys("testing")
        if field8.send_keys:
            filename.write("Verified COMMENT text entry")
            print ("Verified COMMENT text entry")
        else:
            filename.write('ERROR: COMMENT not entered!')
            print ("ERROR: COMMENT not entered!")
        state = driver.find_element_by_name("state")
        state.click()
        state.send_keys("n")
        state.send_keys(Keys.RETURN)
        if state.send_keys:
            filename.write("Verified STATE selected")
            print ("Verified STATE selected")
        else:
            filename.write('ERROR: STATE not selected!')
            print ("ERROR: STATE not selected!")


class Success(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        popup = QtGui.QVBoxLayout()

        self.setWindowTitle('Finished!')
        label = QLabel("Browser test done!\n\nThe log file and any error screenshots are in your temp folder.")
        popup.addWidget(label)
        self.setLayout(popup)

class Browsers():
    def gcvers(self):
        create.createDir('self')
        create.createLog('txt')
        global driver
        if GCButton.clicked:
            driver = webdriver.Chrome()
        driver.get('http://ramses/index.shtml')
        gather.pyjs('self')
        gather.pyjs2('self')
        gather.batt('self')
        gather.crest('self')
        gather.crestg('self')
        gather.contact('self')
        gather.colorgall('self')
        gather.BWgall('self')
        driver.quit()
        global popup
        popup = Success()
        popup.exec()

    def mfvers(self):
        create.createDir('self')
        create.createLog('txt')
        global driver
        if MFButton.clicked:
            driver = webdriver.Firefox()
        driver.get('http://ramses/index.shtml')
        gather.pyjs('self')
        gather.pyjs2('self')
        gather.batt('self')
        gather.crest('self')
        gather.crestg('self')
        gather.contact('self')
        gather.colorgall('self')
        gather.BWgall('self')
        driver.quit()
        global popup
        popup = Success()
        popup.exec()


    def ievers(self):
        create.createDir('self')
        create.createLog('txt')
        global driver
        if IEButton.clicked:
            driver = webdriver.Ie()
        driver.get('http://ramses/index.shtml')
        gather.pyjs('self')
        gather.pyjs2('self')
        gather.batt('self')
        gather.crest('self')
        gather.crestg('self')
        gather.contact('self')
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
        global GCButton
        GCButton = QPushButton("Google Chrome")
        global MFButton
        MFButton = QPushButton("Mozilla Firefox")
        global IEButton
        IEButton = QPushButton("Internet Explorer")
        #MEButton = QPushButton("Microsoft Edge")
        global closebutton
        closebutton = QPushButton("Exit")

        self.setWindowTitle('City of Kothos')
        layout.addWidget(label)
        layout.addWidget(GCButton)
        layout.addWidget(MFButton)
        layout.addWidget(IEButton)
        ##layout.addWidget(MEButton)
        layout.addWidget(closebutton)

        self.setLayout(layout)

        GCButton.clicked.connect(Browsers.gcvers)
        MFButton.clicked.connect(Browsers.mfvers)
        IEButton.clicked.connect(Browsers.ievers)
        closebutton.clicked.connect(self.close)

app = QApplication(sys.argv)
dialog = Browserbutton()
dialog.show()
app.exec()