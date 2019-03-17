from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from tkinter import *
import time
import os, sys
import json

#user name and password section starts here
def data_file(filePathAndName):
    return os.path.exists(filePathAndName)

if data_file('data.json'):
    pass

else:
    window = Tk()

    def create():
        data = {  
            'user': e1_val.get(),
            'pass': e2_val.get()
        }

        with open('data.json', 'w') as outfile:  
            json.dump(data, outfile)
        def quit1():
            window.destroy()
        quit1()
        
    l1 = Label(window, text="Username")
    l1.grid(padx=15,pady=10,ipady=3) 
    e1_val = StringVar()    

    e1 = Entry(window, width="50", textvariable= e1_val)
    e1.grid(row=0, column = 2)
    l3 = Label(window)
    l3.grid(row = 0, column = 3) 
    l3 = Label(window)
    l3.grid(row = 0, column = 4) 

    l2 = Label(window, text="Password")
    l2.grid(row = 1, column = 0) 
    e2_val = StringVar()


    e2 = Entry(window,  width="50", textvariable= e2_val)
    e2.grid(row=1, column = 2)

    b1 = Button(window, text = "Be BIBO!", command = create, width = '10', height='3')  
    b1.grid(row=3, column=2, rowspan=3)     
    l4 = Label(window)
    l4.grid(row = 5, column = 0) 
        
        
    window.mainloop()

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
#browser = webdriver.Chrome(options=options)
#variables to make life easier :)
timer = browser.implicitly_wait
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

def check():
    try:
        klas("ready_clickable").click()
        timer(30)
        bid("lessonstart").click()
        timer(30)
        print("greska")
        browser.quit()
    except NoSuchElementException:

    #NoSuchElementException
        #def chck():
        try:
            xpath("//span[@class='lbl_lesson_status label label-info lbl_lesson_open ready_clickable']").click()
            timer(60)
			#time.sleep(3)
            xpath("//table[@id='tbl-ready-status']//a[@class='color button btn-ready blue']").click()
            timer(30)
            print("greska2")
            browser.quit()
        except: #NoSuchElementException:#NoSuchElementException
            #print("smrt")
            browser.quit()
    except:
	    print("nope")
	    timer(60)
	    browser.quit()
    #return False
    else:
	    print("najn")
        #browser.quit()


def mia():
    try:
        check("ready_clickable")
    except NoSuchElementException:
        #browser.quit()
	    print('ola')
        #browser.quit()
		#NoSuchElementException

    #else:

    #return True
#this is the function according to the original code
def wrk():
    browser.get(url)
    timer(30)
    klas('css-cgadzw').click()
    timer(30)
    klas('css-cgadzw').send_keys(user)
    timer(30)
    bid('label-1').click()
    timer(30)
    bid('label-1').send_keys(pas)
    timer(30)
    xpath("//button[@type='submit']//div[contains(text(),'Sign In')]").click()
    timer(30)
    bid("schedule-today").click()
    timer(30)
    check()
    #mia()
wrk()
