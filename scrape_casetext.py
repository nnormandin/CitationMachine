import os
import time
import docx
import re
import copy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import wait modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_load(browser, timeout=20, xp="//input[@id='q']"):
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.element_to_be_clickable((By.xpath, xp)))


def search_case(w, text):
    searchbar = w.find_element_by_xpath("//input[@id='q']")
    searchbar.send_keys(text)
    searchbar.send_keys(Keys.ENTER)
    wait_load(w)


def title_to_case(title):
    out = []
    for i in title.split():
        if i == "V":
            out.append('v.')
        else:
            out.append(i.title())
    return(' '.join(out))


def parse_case(w, caseid, page):

    # search for case
    search_case(w, caseid)
    wait_load(w)

    # find title and parse
    xpt = "//h1[@class='title-and-tools-shell']/span"
    title = w.find_element_by_xpath(xpt).text
    title = title_to_case(title)

    # find header data
    xph = "//ct-document-header[@class='ng-isolate-scope']"
    header = w.find_element_by_xpath(xph)

    court = header.find_element_by_xpath("//li[0]").text


    dategroup = header.find_element_by_xpath("//li[2]").text
    year = yr.search(dategroup).group(0)[1:-1]

    print("located {}: {}".format(caseid, title))

    return(Citation(title, caseid, page, year))


# start firefox and go to casetext
w = webdriver.Firefox()
w.get('https://casetext.com/')
wait_load(w)