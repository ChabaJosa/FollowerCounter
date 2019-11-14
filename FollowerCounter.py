from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random
import re

class FollowerCounter:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome('./chromedriver') #No problem here
        self.browser.get(link)
        time.sleep(3)

        elements = self.browser.find_elements_by_class_name('g47SY')
        element_attribute_value = elements[1].get_attribute('title')
        print(element_attribute_value)

        time.sleep(3)
        self.browser.close()
 
if __name__ == '__main__':
    follower_counter = FollowerCounter('https://www.instagram.com/radiorochela/')