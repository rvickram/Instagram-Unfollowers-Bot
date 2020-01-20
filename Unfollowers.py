import selenium as webdriver

class UnfollowersBot:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://instagram.com")

UnfollowersBot()