from locators.locator import loc

class offers():
    def __init__(self,driver):
        self.driver=driver
        self.off = loc.off
        self.flg = loc.flg

    def offer(self):
        self.driver.find_element_by_xpath(self.off).click()
        self.driver.find_element_by_xpath(self.flg).click()
