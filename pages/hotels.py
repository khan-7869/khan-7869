from locators.locator import loc
from selenium.webdriver.support.select import Select

class hotel():
    def __init__(self,driver):
        self.driver=driver
        self.clk = loc.clk1
        self.bk = loc.book
        self.fn = loc.fn
        self.ln = loc.ln
        self.fn1 = loc.fn1
        self.ln1 = loc.ln1
        self.cn = loc.cn
        self.cln = loc.cln
        self.cn1 = loc.cn1
        self.cln1 = loc.cln1
        self.pay = loc.pay
        self.agr = loc.agr
        self.cfn = loc.cfn
        self.fnn = loc.fnn
        self.lnn = loc.lnn
        self.em = loc.em
        self.add3 = loc.add3
        self.ph = loc.ph



    def search(self,fnn,lnn,em,ph,add3,fn,ln,fn1,ln1,cn,cln,cn1,cln1):
        button = self.driver.find_element_by_xpath(self.clk)
        self.driver.execute_script("arguments[0].click();", button)
        button1 = self.driver.find_element_by_xpath(self.bk)
        self.driver.execute_script("arguments[0].click();", button1)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath(self.fnn).send_keys(fnn)
        self.driver.find_element_by_xpath(self.lnn).send_keys(lnn)
        self.driver.find_element_by_xpath(self.em).send_keys(em)
        self.driver.find_element_by_xpath(self.ph).send_keys(ph)
        self.driver.find_element_by_xpath(self.add3).send_keys(add3)
        self.driver.find_element_by_xpath(self.fn).send_keys(fn)
        self.driver.find_element_by_xpath(self.ln).send_keys(ln)
        self.driver.find_element_by_xpath(self.fn1).send_keys(fn1)
        self.driver.find_element_by_xpath(self.ln1).send_keys(ln1)
        self.driver.find_element_by_xpath(self.cn).send_keys(cn)
        self.driver.find_element_by_xpath(self.cln).send_keys(cln)
        self.driver.find_element_by_xpath(self.cn1).send_keys(cn1)
        self.driver.find_element_by_xpath(self.cln1).send_keys(cln1)
        button3 = self.driver.find_element_by_xpath(self.agr)
        self.driver.execute_script("arguments[0].click();", button3)
        button2 = self.driver.find_element_by_xpath(self.pay)
        self.driver.execute_script("arguments[0].click();", button2)
        button4 = self.driver.find_element_by_xpath(self.cfn)
        self.driver.execute_script("arguments[0].click();", button4)





