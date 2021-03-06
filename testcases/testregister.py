import unittest

from selenium import webdriver
from pages.register import reg
from pages.login import price
from pages.hotels import hotel
from pages.currency import curr
from pages.offers import offers
from pages.tour import tour


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\HCL TSS\Downloads\chromedriver_win32 (3)\chromedriver.exe")

    def test_aregister(self):
        driver=self.driver
        driver.get("https://www.phptravels.net/login")
        driver.maximize_window()
        p=price(driver)
        p.price1("user@phptravels.com","demouser")
        act=driver.title
        exp="Dashboard - PHPTRAVELS"
        self.assertEqual(exp,act)

    def test_blogin(self):
        driver = self.driver
        driver.get("https://phptravels.org/register.php")
        driver.maximize_window()
        r=reg(driver)
        r.register("khan","ibr","khan@gmail.com","7869","Hcl","cisf","rdm","karimnager",1234,"@123k")
        act=driver.find_element_by_xpath("//div[@class='alert-body']").text
        exp="The following errors occurred:"
        self.assertTrue(act.__contains__(exp))

    def test_chotel(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/hotels")
        driver.maximize_window()
        h=hotel(driver)
        h.search("danish","khan","khan@gmail.com",7869,"cisf","ibrahim","khan","rushi","patil","akash","dhakar","harsh","vardhan")
        act=driver.find_element_by_xpath("//h3[@class='title pb-1']").text
        exp="Thanks danish khan"
        self.assertEqual(exp,act)

    def test_dcurrency(self):
        driver=self.driver
        driver.get("https://www.phptravels.net/")
        driver.maximize_window()
        z=curr(driver)
        z.currency()
        act=driver.find_element_by_xpath("//span[normalize-space()='INR 56152']").text
        exp="INR 56152"
        self.assertEqual(exp,act)

    def test_eoffers(self):
        driver=self.driver
        driver.get("https://www.phptravels.net/")
        driver.maximize_window()
        o=offers(driver)
        o.offer()
        act = driver.current_url
        exp="https://www.phptravels.net/offers/cheap-flights-tickets/4"
        self.assertEqual(exp,act)

    def test_ftour(self):
        driver = self.driver
        driver.get("https://www.phptravels.net/")
        driver.maximize_window()
        t=tour(driver)
        t.tours("danish","khan","khan78@gmail.com","7896","cisf","ibr","khan","danish","khan")
        act=driver.current_url
        exp="https://www.phptravels.net/tours/book"
        self.assertEqual(exp,act)

if __name__ == '__main__':
    unittest.main()
