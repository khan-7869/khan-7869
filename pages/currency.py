from locators.locator import loc

class curr():

    def __init__(self,driver):
        self.driver=driver
        self.cr = loc.cr
        self.inr = loc.inr

    def currency(self):
        self.driver.find_element_by_xpath(self.cr).click()
        self.driver.find_element_by_xpath(self.inr).click()