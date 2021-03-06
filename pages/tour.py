from locators.locator import loc

class tour():

    def __init__(self,driver):
        self.driver = driver
        self.trs = loc.trs
        self.trp = loc.trp
        self.bk = loc.bk
        self.fnn = loc.fnn
        self.lnn = loc.lnn
        self.em = loc.em
        self.ph = loc.ph
        self.add = loc.add3
        self.tf = loc.fn
        self.tl = loc.ln
        self.tf1 = loc.fn1
        self.tl1 = loc.ln1
        self.py = loc.pay
        self.agr = loc.agr
        self.cfn = loc.cfn

    def tours(self,fnn,lnn,em,ph,add,tf,tl,tf1,tl1):
        self.driver.find_element_by_xpath(self.trs).click()
        button=self.driver.find_element_by_xpath(self.trp)
        self.driver.execute_script("arguments[0].click();", button)
        button1=self.driver.find_element_by_xpath(self.bk)
        self.driver.execute_script("arguments[0].click();", button1)
        self.driver.find_element_by_xpath(self.fnn).send_keys(fnn)
        self.driver.find_element_by_xpath(self.lnn).send_keys(lnn)
        self.driver.find_element_by_xpath(self.em).send_keys(em)
        self.driver.find_element_by_xpath(self.ph).send_keys(ph)
        self.driver.find_element_by_xpath(self.add).send_keys(add)
        self.driver.find_element_by_xpath(self.tf).send_keys(tf)
        self.driver.find_element_by_xpath(self.tl).send_keys(tl)
        self.driver.find_element_by_xpath(self.tf1).send_keys(tf1)
        self.driver.find_element_by_xpath(self.tl1).send_keys(tl1)
        button3 = self.driver.find_element_by_xpath(self.agr)
        self.driver.execute_script("arguments[0].click();", button3)
        button2 = self.driver.find_element_by_xpath(self.py)
        self.driver.execute_script("arguments[0].click();", button2)
        button4 = self.driver.find_element_by_xpath(self.cfn)
        self.driver.execute_script("arguments[0].click();", button4)
        self.driver.implicitly_wait(10)
