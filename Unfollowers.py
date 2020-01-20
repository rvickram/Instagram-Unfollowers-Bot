# Instagram Unfollowers bot by Ryan Vickramasinghe

import selenium.webdriver as webdriver
import os.path as path

class UnfollowersBot:
    def __init__(self):
        print('\n\n---- Initializing Instagram Unfollowers Bot ----\n\n')
        if(path.exists('./chromedriver')):
            self.driver = webdriver.Chrome('./chromedriver')
            self.driver.get("https://instagram.com")
        else:
            print('No chrome driver detected in path!')

UnfollowersBot()