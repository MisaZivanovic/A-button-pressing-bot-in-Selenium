#This one has seen a lot of change.
#First change was to modify it so that it can be converted to exe
#Because people who are going to use this are not programers
#second change was adding that json data file.
#json file serves as data for user and password
#if json file is not present the program will create it
#and will, in future, ready user and password from it.
#If json is present, it will just continue on to the rest of the code.
#comand in prompt for converting it to exe ( note that chromedriver.exe is located
#on C:\, change if needed, also the name of my script is ready.py )
#pyinstaller -F --add-binary "C:\chromedriver.exe";"." ready.py


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import os, sys

def where_json(file_name):
    return os.path.exists(file_name)
  

if where_json('data.json'):
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

    

