import unittest
from selenium import webdriver


class LanguageOptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver        
        driver.get('http://demo-store.seleniumacademy.com/')


    def test_select_language(self):
        pass

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()