import unittest
from pyunitreport import HTMLTestRunner # nos ayuda o Orquestar los reportes
from selenium import webdriver

class HelloWord(unittest.TestCase):
    
    @classmethod # para que no se cierre las ventanas y abra solo una ventana
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(3)
    
    def test_hello_word(self):# siempre debe iniciar con "test_xxxx"
        driver = self.driver
        driver.get('http://www.platzi.com')

    def test_visit_wiki(self):
        self.driver.get('http://www.wikipedia.org')
        driver.implicitly_wait(3)

        

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-word-report'))

