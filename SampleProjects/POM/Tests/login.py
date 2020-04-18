from selenium import webdriver
import time
import unittest
import sys
import os
from SampleProjects.POMDemo.Pages.loginPage import LoginPage
from SampleProjects.POMDemo.Pages.homePage import HomePage
from HTMLTestRunner import HTMLTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\edu\python\selenium\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    def test_02_login_invalid_username(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin1")
        login.enter_password("admin123")
        login.click_login()
        # message = driver.find_element_by_xpath("").text
        message = login.check_invalid_username_message()
        self.assertEqual(message, "Invalid Credentials123")

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output='D:\edu\python\selenium\SampleProjects\POMDemo\Tests'))




