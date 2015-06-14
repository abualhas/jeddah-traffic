from selenium import webdriver
import time
n = 500
   

browser = webdriver.Chrome("C:\\Python34\\selenium\\chrome\\chromedriver.exe", port=9515)
browser.get('http://alrawdatravel.byethost7.com/')
browser.maximize_window()
file = open('photo_time.txt','a')
i=1
while i <= n :
    browser.refresh()
    time.sleep(3)
    time_photo = str(int(time.strftime("%H"))+1)
    browser.save_screenshot(str(i)+'.png') 
    file.write(time_photo + '\n')
    if i == n:
        break
    time.sleep(597)
    i+=1
    
browser.quit()
file.close()
