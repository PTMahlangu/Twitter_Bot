
from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class TwitterBot:
    def __init__(self,username,passward):
        self.username = username
        self.passward = passward
        # Instant of a bot, to open a page
        self.bot      = webdriver.Firefox() 

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        # wait for the page to load
        time.sleep(3)
        email = bot.find_element_by_class_name("email-input")
        password =bot.find_element_by__name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.passward)
        password.send_keys(keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hashtag):
        bot = self.bot

# test 
my = TwitterBot("mahlangupt@hotmail.com",'password')
my.login()
# https://www.youtube.com/watch?v=7ovFudqFB0Q