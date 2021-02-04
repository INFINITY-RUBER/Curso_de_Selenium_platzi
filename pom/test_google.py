import unittest
from selenium import webdriver
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod # para que corran en un sola intancia del navegador
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path = './chromedriver')
        


    def test_search(self):
        google = GooglePage(self.driver)#  por que estamos llamando al driver de esta clase
        google.open()
        google.search('platzi')

        self.assertEqual('platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)