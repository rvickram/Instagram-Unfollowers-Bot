# Instagram Unfollowers bot by Ryan Vickramasinghe

from selenium import webdriver
from os import path
from getpass import getpass
from time import sleep

class UnfollowersBot:
    def __init__(self, username, password):
        print('\nAttempting to login...')

        # check for chromedriver
        if(path.exists('./chromedriver')):
            self.driver = webdriver.Chrome('./chromedriver')
            self.driver.get("https://instagram.com")
            sleep(2)

            # attempt to login using username, password
            self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
                .click()
            sleep(2)
            self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
                .send_keys(username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(password)
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            # TODO: Check for two-factor authentication
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
            sleep(2)
            print('Successfully logged in.')
        else:
            print('ERROR: No chrome driver detected in path!')

print('\n\n---- Welcome to Instagram Unfollowers Bot ----\n\n')
# get login details from console (user must enter)
username = input('Username: ')
password = getpass('Password: ')

# initialize the bot (login)
bot = UnfollowersBot(username, password)