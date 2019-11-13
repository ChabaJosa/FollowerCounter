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

        # elements = self.browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
        elements = self.browser.find_elements_by_class_name('g47SY')
        element_attribute_value = elements[1].get_attribute('title')
        #Add it somewhere, maybe a variable 
        print(element_attribute_value)

        time.sleep(5)
        self.browser.close()

    #def cleanUp (self, pattern):
        #Regex for followers
        #re.comppile 

    #def print (self):
        #print(cssClass)
 
if __name__ == '__main__':
    follower_counter = FollowerCounter('https://www.instagram.com/radiorochela/')