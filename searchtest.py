import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        
    def test_search_field(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button(self):
        button = self.driver.find_element_by_class_name("button search-button")

    def test_count_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_element_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//body/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/p[1]/img[1]')

    def test_shopping_cart(self):
        shopping_cart = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)