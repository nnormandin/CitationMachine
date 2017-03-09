import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import wait modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_load(browser, timeout=20, xp="//textarea[@id='searchInputId']"):
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.element_to_be_clickable((By.xpath, xp)))



# pull the email and password from text files
un = open('.email.txt').read().strip()
pw = open('.pw.txt').read().strip()

# start firefox and go to westlaw
w = webdriver.Firefox()
w.get('https://1.next.westlaw.com/')

# enter credentials
w.find_element_by_name('Username').send_keys(un)
w.find_element_by_name('Password').send_keys(pw)

# press enter
time.sleep(0.2)
w.find_element_by_name('Password').send_keys(Keys.ENTER)

# wait for load,
time.sleep(3)
w.find_element_by_class_name('co_primaryBtn').click()

try:
    w.find_element_by_xpath("//input[@value='Close']").click()
    time.sleep(1)
except:
    print('finding searchbar')

wait_load(w)
searchbar = w.find_element_by_xpath("//textarea[@id='searchInputId']")


searchbar.send_keys('79 S.Ct. 1171')
searchbar.send_keys(Keys.ENTER)

wait_load(w)

header = w.find_element_by_xpath("//h2[@id='co_docHeaderTitleLine']")
casename = header.get_attribute("title")

court = w.find_element_by_xpath("//span[@id='courtline']").text
filedate = w.find_element_by_xpath("//span[@id='filedate']").text

citations = []

citations.append(w.find_element_by_xpath("//span[@id='cite0']").text)

try:
    citations.append(w.find_element_by_xpath("//span[@id='cite2']").text)
    print('three citations found')
except:
    try:
        citations.append(w.find_element_by_xpath("//span[@id='cite1']").text)
        print('two citations found')
    except:
        print('one citation found')

