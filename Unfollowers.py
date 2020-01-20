import selenium as webdriver

class UnfollowersBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")

UnfollowersBot()