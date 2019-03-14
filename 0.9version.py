from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.chrome.options import Options
import time
import os, sys
import json

#user name and password section starts here
def data_file(filePathAndName):
    return os.path.exists(filePathAndName)
  
if data_file('data.json'):
    pass
    
else:
    data = {  
        'user': input('User input: '),
        'pass': input('Pass input: ')
    }

    with open('data.json', 'w') as outfile:  
        json.dump(data, outfile)

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

user = list(data.values())[0]  
pas = list(data.values())[1]
#user name/pass input ends here
#headless settings
options = Options()
options.headless = True

#code for propper exe
#pyinstaller -F --add-binary "path:\to\your\webdriver.exe";"." ready.py
#settings in the file, necessary for this to work as an exe
#if you need it as an exe
#if you don't, ignore this part up to URL
if getattr(sys, 'frozen', False):
	chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe",)
	browser = webdriver.Chrome(chromedriver_path, options=options)
else:
	browser = webdriver.Chrome(options=options)
#website address
#adresa sajta
url='https://tutor.engoo.com/schedules/day/3382/2019/02/17'

#variables to make life easier :)
time = browser.implicitly_wait
klas = browser.find_element_by_class_name
bid = browser.find_element_by_id
xpath = browser.find_element_by_xpath

#function that fixes the issue the program had
# at one point there were 3 options, to find the button and click it
#to find additional button ( like, steady, or something like htat )
#find nothing
#and this function regulates that issue
#first, it searches for button, presses it, and quits, 
#if not, searches for the other one, presses it and quits
#if neither are there, it justs quits browser

def check(x):
    try:
        klas(x).click()
        time(30)
        bid("lessonstart").click()
        time(30)
        browser.quit()
    except NoSuchElementException:#NoSuchElementException
        def chck():
            try:
                xpath("//span[@class='lbl_lesson_status label label-info lbl_lesson_open ready_clickable']").click()
                time(60)
                xpath("//a[@class='color button btn-ready blue']").click()
                time(30)
                browser.quit()
            except NoSuchElementException:#NoSuchElementException
                return False
        #return False
    else:
        browser.quit()
    #return True
#this is the function according to the original code
def wrk():
    browser.get(url)
    time(30)
    klas('css-cgadzw').click()
    time(30)
    klas('css-cgadzw').send_keys(user)
    time(30)
    bid('label-1').click()
    time(30)
    bid('label-1').send_keys(pas)
    time(30)
    xpath("//button[@type='submit']//div[contains(text(),'Sign In')]").click()
    time(30)
    bid("schedule-today").click()
    time(30)
    check("ready_clickable")
    
wrk()
