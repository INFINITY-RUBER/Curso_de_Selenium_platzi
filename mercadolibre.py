import unittest
from selenium import webdriver
from time import sleep


class TestingMercadoLibre(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com/')
        driver.maximize_window()


    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(2)

        ubicacion = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/span')
        ubicacion.click()
        cooke = driver.find_element_by_xpath('//*[@id="cookieDisclaimerButton"]')
        cooke.click()


        location = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/dl[14]/dd[1]/a/span[1]')
        location.click()
        sleep(2)

        condicion = driver.find_element_by_partial_link_text('Nuevo')
        condicion.click()
        sleep(2)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        sleep(2)

        higher_price = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]/a/div/div')
        higher_price.click()
        sleep(2)

        articles = []
        prices = []
        N_articles = 11

        # /html/body/main/div/div/section/ol/li[1]/div/div/div[2]/div[1]/a/h2

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
            prices.append(article_price)

        print(articles, prices)


 


          

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()