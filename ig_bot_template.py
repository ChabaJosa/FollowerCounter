from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import config

ig_password = config.PASSWORD

class InstaBot:
    def __init__(self,username,password):

        '''
        Initializes an instance of the InstaBot class.

        Call the login method to authenticate a user with IG.

        Args:
            username: str: The IG username for user.
            password: str: The IG passowrd for user.
        '''

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com/'
        self.browser = webdriver.Chrome('./chromedriver')
        self.login()

        
        
    def login(self):
        self.browser.get('{}accounts/login/'.format(self.base_url))
        time.sleep(3)
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.browser.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()

    def nav_user(self,user):
        self.browser.get('{}{}'.format(self.base_url, user))

    #def follow_user(self,user):
        #self.nav_user(user)


if __name__ == '__main__':
    ig_bot = InstaBot('TestingVainas1969',ig_password)
    time.sleep(5)
    ig_bot.nav_user('rctv')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

class FollowerCounter:
    def __init__(self,link):
        self.link = link
        self.browser = webdriver.Chrome('./chromedriver') #No problem here
        self.browser.get(link)
        time.sleep(3)
        self.browser.find_elements_by_link_text(" followers")
        def time1():
            #time.sleep(150)
            time.sleep(int(random.randrange(150,800,1)))
        def time2():
            #time.sleep(600)
            time.sleep(int(random.randrange(150,800,1)))
        def time3():
            #time.sleep(800)
            time.sleep(int(random.randrange(30,800,1)))
        Times = [time1,time2,time3]
        random.choice(Times)()
        self.browser.close()
        
for i in range (0,25):
    if __name__ == '__main__':
        YT_Bot = YTBot('https://www.instagram.com/radiorochela/')