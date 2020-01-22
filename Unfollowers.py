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
                .send_keys(self.username)
            self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
                .send_keys(self.password)
            self.driver.find_element_by_xpath('//button[@type="submit"]')\
                .click()
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
                .click()
            sleep(2)
            print('Successfully logged in.')
        else:
            print('ERROR: No chrome driver detected in path!')

    def get_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()

        # get following list
        print('Fetching users you follow.')
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._get_names()
        print('Found ' + str(len(following)) + ' users you follow.')
        
        # get followers list
        print('Fetching users who follow you.')
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._get_names()
        print('Found ' + str(len(followers)) + ' users following you.')

        # find users not following you back
        print('Calculating results...')
        sleep(2)
        not_following_back = [user for user in following if user not in followers]
        print('\nThe following users are not following you back:\n')
        print(not_following_back)
        print('\n')

    def _get_names(self):
        sleep(2)
        sugs = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div[2]/button")\
            .click()
        return names

print('\n\n---- Welcome to Instagram Unfollowers Bot ----\n\n')
# get login details from console (user must enter)
username = input('Username: ')
password = getpass('Password: ')

# initialize the bot (login)
bot = UnfollowersBot(username, password)
bot.get_unfollowers()