
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self,username,passward):
        self.username = username
        self.passward = passward
        self.bot = webdriver.Firefox() 

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        # wait for the page to load
        time.sleep(1)
        email = bot.find_element_by_name('session[username_or_email]')
        password =bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.passward)
        password.send_keys(Keys.RETURN)
        time.sleep(1)

    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        time.sleep(1)
        for i in range(1,5):
            bot.execute_script('window.scrollTo(0.body.scrollHeight)')
            time.sleep(1)


mybot = TwitterBot("username",'password')
mybot.login()
mybot.like_tweet("amakhosi")

