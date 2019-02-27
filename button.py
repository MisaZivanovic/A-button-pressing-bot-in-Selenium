from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#adresa sajta
#website url
url=''
user=''
passw=''
#drajver za hrom, moze se menjati
#chromedriver, you can use others, i like chrome
browser = webdriver.Chrome()#starts Chrome browser
browser.get(url)
#goes to the website
browser.find_element_by_class_name('css-cgadzw').click()
#clicks the input for user name, and the bottom one inputs username
browser.find_element_by_class_name('css-cgadzw').send_keys(user)
#clicks the password input and types it in
browser.find_element_by_id('label-1').click()
browser.find_element_by_id('label-1').send_keys(passw)
#clicks the sing in button
browser.find_element_by_class_name('css-bxqq9l').click()
browser.implicitly_wait(30)
#first page
browser.find_element_by_id("schedule-today").click()
browser.implicitly_wait(30)
#finds the aforementioned event and clicks on the page on which the event is
browser.find_element_by_class_name("ready_clickable").click()
browser.find_element_by_class_name("btn-ready").click()
browser.implicitly_wait(30)
#cliks the button
browser.find_element_by_id("lessonstart").click()
browser.implicitly_wait(30)
#closes the whole program, because it is not necessary for it to run anymore.
browser.quit()    
         

