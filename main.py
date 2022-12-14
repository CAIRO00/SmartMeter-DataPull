
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

url = "https://www.smartmetertexas.com"

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe", chrome_options=options)

s = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")





def meterPull():
    print('test')
    driver.get(url)
    time.sleep(5)
    driver.implicitly_wait(10)
    print('test')
    #---Login Page---#
    username = driver.find_element(by=By.ID, value = "userid")
    password = driver.find_element(by=By.ID, value = "password")
    login = driver.find_element(by=By.XPATH, value = '//*[@id="loginform"]/div[8]/button')
    print('test')
    username.send_keys('username')
    password.send_keys('password')
    login.click()
    print('test')
    #---Login Page---#
    time.sleep(5)
    #---Dashboard---#
    meterBttn = driver.find_element(by=By.XPATH, value='//*[@id="wrapper"]/div[2]/main/div/div[5]/div[1]/div/div[2]/div[2]/div/div[1]/button')
    meterBttn.click()
    time.sleep(70)
    
    meterUsage = driver.find_element(by=By.XPATH, value = '//*[@id="wrapper"]/div[2]/main/div/div[5]/div[1]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]')
    
    driver.close()
    return meterUsage.text


def timeCheck():
    time = ''
    hour = str(datetime.now().hour)
    if hour == 21:
        time = '9 pm: '
    elif hour == 7:
        time = '7 am: '
    else:
        time = hour + ' fm: '

    return time


def main():
    txt = open('data.txt', 'a')
    usge = meterPull()
    tme = timeCheck()
    txt.write(tme + usge + '\n')
    txt.close
    return

main()
