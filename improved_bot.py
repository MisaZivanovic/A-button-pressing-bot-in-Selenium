#This one has seen a lot of change.
#First change was to modify it so that it can be converted to exe
#Becuase people who are going to use this are not programers
#second change was adding that json data file
#json file serves as data for user and password
#if json file is not present the program will create it
#and will, in future, ready user and password from it.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import os, sys

def doesFileExists(filePathAndName):
    return os.path.exists(filePathAndName)
  
# Example
if doesFileExists('data.json'):
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

url=''

if getattr(sys, 'frozen', False):
	chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
	browser = webdriver.Chrome(chromedriver_path)
else:
	browser = webdriver.Chrome()


wid=browser.find_element_by_id
wclass=browser.find_element_by_class_name
time=browser.implicitly_wait

browser.get(url)
time(30)
wclass('css-cgadzw').click()
time(30)
wclass('css-cgadzw').send_keys(user)
time(30)
wid('label-1').click()
time(30)
wid('label-1').send_keys(pas)
time(30)
wclass('css-bxqq9l').click()
time(30)
wid("schedule-today").click()
time(30)
wclass("ready_clickable").click()
time(30)
wid("lessonstart").click()
time(30)
browser.quit()    

    

