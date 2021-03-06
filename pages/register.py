import selenium
from locators.locator import loc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class reg():

    def __init__(self,driver):
        self.driver=driver
        self.re = loc.register
        self.fname = loc.fname
        self.lname = loc.lname
        self.email = loc.email
        self.drp = loc.drop
        self.no = loc.no
        self.com = loc.com
        self.add = loc.add
        self.add1 = loc.add1
        self.city = loc.city
        self.state = loc.state
        self.coun = loc.country
        self.mob = loc.mob
        self.genpw = loc.genpw
        self.gencl = loc.gencl
        self.cap = loc.cap
        self.sub = loc.sub

    def register(self,fname,lname,email,number,com,address,address1,city,mob,pwd1):

        self.driver.find_element_by_id(self.fname).send_keys(fname)
        self.driver.find_element_by_id(self.lname).send_keys(lname)
        self.driver.find_element_by_id(self.email).send_keys(email)
        self.driver.find_element_by_class_name(self.drp).click()
        self.driver.find_element_by_xpath("//span[contains(text(),'India (भारत)')]").click()
        self.driver.find_element_by_id(self.no).send_keys(number)
        self.driver.find_element_by_id(self.com).send_keys(com)
        self.driver.find_element_by_id(self.add).send_keys(address)
        self.driver.find_element_by_id(self.add1).send_keys(address1)
        self.driver.find_element_by_id(self.city).send_keys(city)
        c=Select(self.driver.find_element_by_id(self.coun))
        c.select_by_visible_text("India")
        self.driver.find_element_by_id(self.mob).send_keys(mob)
        self.driver.find_element_by_id(self.genpw).send_keys(pwd1)
        self.driver.find_element_by_id(self.gencl).send_keys(pwd1)
        self.driver.implicitly_wait(8)
        self.driver.find_element_by_xpath(self.sub).click()
        self.driver.close()


