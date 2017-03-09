import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import wait modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_load(browser, timeout=20, xp="//input[@id='q']"):
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.element_to_be_clickable((By.xpath, xp)))

def search(w, text):
    searchbar = w.find_element_by_xpath("//input[@id='q']")
    searchbar.send_keys(text)
    searchbar.send_keys(Keys.ENTER)
    wait_load(w)

def parse_case(w):
    title = 


# start firefox and go to casetext
w = webdriver.Firefox()
w.get('https://casetext.com/')
wait_load(w)

searchbar = w.find_element_by_xpath("//input[@id='q']")


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

