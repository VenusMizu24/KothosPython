from re import A

__author__ = 'Nephtiry'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, stat
import time
import datetime
import json
import time
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.QtGui import *
import sys

class Pyjson:
    def json(data_file):
        with open(r"C:\Users\Neph\Desktop\KothosPython-master\Pythondata.json") as data_file:
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
        os.mkdir(folder+'\\Screenshots\\')
        global screenfolder
        screenfolder=(folder+'\\Screenshots\\')

    def createLog(txt):
        global filename
        filename=folder+'\KothosAutoTest_'+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M'))+'.log'
        
class gather(Pyjson):

    def pyjs(createLog):
        f=open(filename, 'a')
        for each in label:
            f.write(each + '\n')
        f.close()

    def homelin(self):
        f=open(filename, 'a')
        f.write('\nReached Homepage--PASSED\n')
        print('Reached Homepage. Testing links...')
        f.close()
        for i in pages:
            driver.find_element_by_link_text(i).click()
            if driver.find_elements_by_tag_name('img'):
                f=open(filename, 'a')
                time.sleep(1)
                f.write('Reached ' + i + '--PASSED\n')
                print('Reached ' + i + '-PASSED')
                driver.get('http://thecityofkothos.com/')
                time.sleep(1)
                f.close()
            else:
                f = open(filename, 'a')
                f.write("ERROR: " + i + "NOT FOUND--TEST FAILED\n")
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print("ERROR: " + i + "NOT FOUND--TEST FAILED")
                f.close()
                

    def batt(self):
        driver.get('http://thecityofkothos.com/thePages/theChapterHeadings.shtml')
        if driver.find_element_by_link_text('Back to Top').click:
            f=open(filename, 'a')
            time.sleep(4)
            f.write("Found 'Back To Top' link in Chapter Headings --PASSED\n")
            print("Found 'Back To Top' link in Chapter Headings --PASSED")
            f.close()
        else:
            f = open(filename, 'a')
            f.write("ERROR: CANNOT FIND 'Back to Top' link in Chapter Headings-- TEST FAILED\n")
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print("ERROR: CANNOT FIND 'Back to Top' link in Chapter Headings-- TEST FAILED\n")
            f.close()

        for nav in btt:
            if driver.find_element_by_link_text("Back to Top").click:
                f=open(filename, 'a')
                time.sleep(1)
                f.write("Found 'Back To Top' link in " + nav + "--PASSED\n")
                print("Found 'Back To Top' link in " + nav + "--PASSED")
                time.sleep(1)
                for each in btt2:
                    driver.find_element_by_link_text(each).click()
                    time.sleep(1)
                f.close()

            else:
                f = open(filename, 'a')
                f.write("ERROR: CANNOT FIND 'Back to Top' LINK IN " + nav + "-- TEST FAILED\n")
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print("ERROR: CANNOT FIND 'Back to Top' LINK IN " + nav + "-- TEST FAILED")
                f.close()
                

    def crest(self):
        for sub in cloop:
            driver.get('http://thecityofkothos.com/thePages/Creston.shtml')
            if driver.find_element_by_link_text(sub).click:
                f=open(filename, 'a')
                time.sleep(1)
                f.write("Found " + sub + " link--PASSED\n")
                print("Found " + sub + " link--PASSED")
                time.sleep(1)
                f.close()
            else:
                f = open(filename, 'a')
                f.write('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED\n')
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print('ERROR: CANNOT FIND ' + sub + '-- TEST FAILED')
                f.close()
                

        driver.get('http://thecityofkothos.com/thePages/BowandArrow.shtml')
        if driver.find_element_by_link_text("Back to top").click:
            f=open(filename, 'a')
            time.sleep(1)
            f.write("Found Back to Top link in Bow and Arrow page--PASSED\n")
            print("Found Back To Top link in Bow and Arrow page--PASSED")
            time.sleep(1)
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: CANNOT FIND Back to Top LINK-- TEST FAILED\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print('ERROR: CANNOT FIND Back To Top LINK-- TEST FAILED')
            f.close()
            


        driver.get('http://thecityofkothos.com/thePages/PriceOfAVisit.shtml')
        if driver.find_element_by_link_text("Back to top").click:
            f=open(filename, 'a')
            time.sleep(1)
            f.write("Found Back to Top link in A Price of A Visit page--PASSED\n")
            print("Found Back To Top link in A Price of a Visit page--PASSED")
            time.sleep(1)
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: CANNOT FIND Back to Top LINK-- TEST FAILED\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print('ERROR: CANNOT FIND Back To Top LINK-- TEST FAILED')
            f.close()
            



    def crestg(self):
        for page in crestgall:
            driver.get('http://thecityofkothos.com/CrestonComic/ccPages/CrestonComic_Cover.shtml')
            driver.find_element_by_name(page).click()
            if driver.find_element_by_link_text(page).click:
                f=open(filename, 'a')
                time.sleep(1)
                f.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
                time.sleep(1)
                f.close()
            else:
                f = open(filename, 'a')
                f.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED\n')
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                f.close()
                

    def colorgall(self):
        for page in colorgal:
            driver.get('http://thecityofkothos.com/GallaryColor/Color_Pages/WizardandDrib.shtml')
            driver.find_element_by_name(page).click()
            if driver.find_element_by_name(page).click:
                f=open(filename, 'a')
                time.sleep(1)
                f.write("Found " + page + " link--PASSED\n")
                print("Found " + page + " link--PASSED")
                time.sleep(1)
                f.close()
            else:
                f = open(filename, 'a')
                f.write('ERROR: CANNOT FIND ' + page + '-- TEST FAILED\n')
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print('ERROR: CANNOT FIND ' + page + '-- TEST FAILED')
                f.close()
                

    def BWgall(self):
        for each in BWgall:
            driver.get('http://thecityofkothos.com/GallaryBW/BW_Pages_v2/BW_Female_Male.shtml')
            driver.find_element_by_name(each).click()
            if driver.find_element_by_name(each).click:
                f=open(filename, 'a')
                time.sleep(1)
                f.write("Found " + each + " link--PASSED\n")
                print("Found " + each + " link--PASSED")
                time.sleep(1)
                f.close()
            else:
                f = open(filename, 'a')
                f.write('ERROR: CANNOT FIND ' + each + '-- TEST FAILED\n')
                time.sleep(2)
                driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
                print('ERROR: CANNOT FIND ' + each + '-- TEST FAILED')
                f.close()
                

    def contact(self):
        driver.get("http://thecityofkothos.com/contactMe/Questionaire.shtml")
        field = driver.find_element_by_name("firstna")
        field.click()
        field.send_keys("John")
        if field.send_keys:
            f=open(filename, 'a')
            f.write("Verified FIRST NAME text entry\n")
            print ("Verified FIRST NAME text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: FIRST NAME not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: FIRST NAME not entered!")
            f.close()
            
        field1 = driver.find_element_by_name("lastna")
        field1.click()
        field1.send_keys("Doe")
        if field1.send_keys:
            f=open(filename, 'a')
            f.write("Verified LAST NAME text entry\n")
            print ("Verified LAST NAME text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: LAST NAME not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: LAST NAME not entered!")
            f.close()
            
        field2 = driver.find_element_by_name("email2")
        field2.click()
        field2.send_keys("johndoe123@gmail.com")
        if field2.send_keys:
            f=open(filename, 'a')
            f.write("Verified EMAIL text entry\n")
            print ("Verified EMAIL text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: EMAIL not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: EMAIL not entered!")
            f.close()
            
        field3 = driver.find_element_by_name("stAddress")
        field3.click()
        field3.send_keys("123 Nevada Ave.")
        if field3.send_keys:
            f=open(filename, 'a')
            f.write("Verified STREET ADDRESS text entry\n")
            print ("Verified STREET ADDRESS text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: STREET ADDRESS not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: STREET ADDRESS not entered!")
            f.close()
            
        field4 = driver.find_element_by_name("city")
        field4.click()
        field4.send_keys("Las Vegas")
        if field4.send_keys:
            f=open(filename, 'a')
            f.write("Verified CITY text entry\n")
            print ("Verified CITY text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: CITY not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: CITY not entered!")
            f.close()
            
        field5 = driver.find_element_by_name("zip")
        field5.click()
        field5.send_keys("91082")
        if field5.send_keys:
            f=open(filename, 'a')
            f.write("Verified ZIP CODE text entry\n")
            print ("Verified ZIP CODE text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: ZIP CODE not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: ZIP CODE not entered!")
            f.close()
            
        field6 = driver.find_element_by_name("country")
        field6.click()
        field6.send_keys("United States")
        if field6.send_keys:
            f=open(filename, 'a')
            f.write("Verified COUNTRY text entry\n")
            print ("Verified COUNTRY text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: COUNTRY not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: COUNTRY not entered!")
            f.close()
            
        field7 = driver.find_element_by_name("phone")
        field7.click()
        field7.send_keys("123-456-7890")
        if field7.send_keys:
            f=open(filename, 'a')
            f.write("Verified PHONE NUMBER text entry\n")
            print ("Verified PHONE NUMBER text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: PHONE NUMBER not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: PHONE NUMBER not entered!")
            f.close()
            
        field8 = driver.find_element_by_name("msg")
        field8.click()
        field8.send_keys("testing")
        if field8.send_keys:
            f=open(filename, 'a')
            f.write("Verified COMMENT text entry\n")
            print ("Verified COMMENT text entry")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: COMMENT not entered!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: COMMENT not entered!")
            f.close()
            
        state = driver.find_element_by_name("state")
        state.click()
        state.send_keys("n")
        state.send_keys(Keys.RETURN)
        if state.send_keys:
            f=open(filename, 'a')
            f.write("Verified STATE selected\n")
            print ("Verified STATE selected")
            f.close()
        else:
            f = open(filename, 'a')
            f.write('ERROR: STATE not selected!\n')
            time.sleep(2)
            driver.save_screenshot(screenfolder+(datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S'))+'.png')
            print ("ERROR: STATE not selected!")
            f.close()


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
        if GCButton.clicked:
            global driver
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get('http://thecityofkothos.com/index.shtml')
            gather.pyjs('self')
            time.sleep(1)
            gather.homelin('self')
            time.sleep(1)
            gather.batt('self')
            time.sleep(1)
            gather.crest('self')
            time.sleep(1)
            gather.crestg('self')
            time.sleep(1)
            gather.contact('self')
            time.sleep(1)
            gather.colorgall('self')
            time.sleep(1)
            gather.BWgall('self')
            time.sleep(1)
            driver.quit()
            global popup
            popup = Success()
            popup.exec()

    def mfvers(self):
        create.createDir('self')
        create.createLog('txt')
        if MFButton.clicked:
            global driver
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get('https://thecityofkothos.com/')
            gather.pyjs('self')
            time.sleep(1)
            gather.homelin('self')
            time.sleep(1)
            gather.batt('self')
            time.sleep(1)
            gather.crest('self')
            time.sleep(1)
            gather.crestg('self')
            time.sleep(1)
            gather.contact('self')
            time.sleep(1)
            gather.colorgall('self')
            time.sleep(1)
            gather.BWgall('self')
            time.sleep(1)
            driver.quit()
            global popup
            popup = Success()
            popup.exec()


    def ievers(self):
        create.createDir('self')
        create.createLog('txt')
        if IEButton.clicked:
            global driver
            driver = webdriver.Ie()
            driver.maximize_window()
            driver.get('http://thecityofkothos.com/index.shtml')
            gather.pyjs('self')
            time.sleep(1)
            gather.homelin('self')
            time.sleep(1)
            gather.batt('self')
            time.sleep(1)
            gather.crest('self')
            time.sleep(1)
            gather.crestg('self')
            time.sleep(1)
            gather.contact('self')
            time.sleep(1)
            gather.colorgall('self')
            time.sleep(1)
            gather.BWgall('self')
            time.sleep(1)
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