# -*- coding: utf-8 -*-
# _author_ = 'plech'

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Windows', 'os_version': '10', 'browser': 'ie', 'browser_version': '11.0' }


class shoplo_rekrutacja(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote(command_executor='http://shoplo1:pEo6qu696jksLpJxBQny@hub.browserstack.com:80/wd/hub', desired_capabilities=desired_cap)

        cls.driver.implicitly_wait(15)
        cls.driver.set_page_load_timeout(50)
        cls.driver.maximize_window()
        cls.nazwa_sklepu = 'pawellechSKLEP01'

    def setUp(self):
        pass

    def test_dodaj_sklep_towar(self):
        przegladarka = self.driver
        adres = 'https://www.shoplo.com'
        przegladarka.get(adres)
        przegladarka.find_element_by_css_selector('.btn-with-icon').click()
        time.sleep(3)
        przegladarka.find_element_by_xpath('//*[@id="mm-0"]/header/div/div[2]/nav/'
                                           'ul/li[6]/ul/li/div/div/div/ul/li[1]/a/span[2]/span').click()
       # zamiast usypiania time.sleep()
       # menu_rozwijane = przegladarka.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/nav/ul/'
       #                                                     'li[6]/ul/li/div/div/div/ul/li[1]/a/span[2]/span')
       # if menu_rozwijane.is_visible():
       #    menu_rozwijane.click()

        przegladarka.find_element_by_partial_link_text('by się zarejestrować').click()
        przegladarka.find_element_by_id('storeName').send_keys(self.nazwa_sklepu)
        przegladarka.find_element_by_id('storeEmail').send_keys('pawel.lech@outlook.com')
        przegladarka.find_element_by_name('password').send_keys('lech.123')
        przegladarka.find_element_by_xpath('//*[@id="registerShop"]/button').click()
        przegladarka.find_element_by_name('name').send_keys('Pawel')
        przegladarka.find_element_by_name('phone').send_keys('123456789')
        przegladarka.find_element_by_css_selector('body > section.main-container.no-sidebar > '
                                                  'section > section > section > section > section >'
                                                  ' form > section:nth-child(4) > section >'
                                                  ' div > button '
                                                  '> span.filter-option.pull-left').click()

        przegladarka.find_element_by_css_selector('body > section.main-container.no-sidebar > section > section >'
                                                  ' section > section > section > form > section:nth-child(4) >'
                                                  ' section > div > div > ul > li:nth-child(6) > a > span.text').click()
        # -------------------------------------------------------------------------------------------------------------
        # można to załatwić również standardowym sposobem na listboxy czyli:
        # select = Select(przegladarka.find_element_by_css_selector('body > section.main-container.no-sidebar > '
                                                                 # 'section > section > section > section > section >'
                                                                 #' form > section:nth-child(4) > section >'
                                                                 # ' div > button '
                                                                 #'> span.filter-option.pull-left'))
        # select.select_by_visible_text('Nie')
        # --------------------------------------------------------------------------------------------------------------

        przegladarka.find_element_by_css_selector('body > section.main-container.no-sidebar > section >'
                                                  ' section > section > section > '
                                                  'section > form > section:nth-child(5) > '
                                                  'section > div > button >'
                                                  ' span.filter-option.pull-left').click()
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/section'
                                           '/section/section/form/section[4]/section/div/div'
                                           '/ul/li[4]/a/span[1]').click()

        przegladarka.find_element_by_css_selector('body > section.main-container.no-sidebar > '
                                                  'section > section > section > section > section >'
                                                  ' form > section:nth-child(6) > section > div >'
                                                  ' button > span.filter-option.pull-left').click()
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/'
                                           'section/section/section/form/section[5]/section/'
                                           'div/div/ul/li[2]/a/span[1]').click()

        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/'
                                           'section/section/section/form/section[6]/section/button').click()
        przegladarka.find_element_by_xpath('//*[@id="productListSidebar"]/span').click()
        przegladarka.find_element_by_css_selector('body > section.main-container.notifications-visible > section >'
                                                  ' section > article > section:nth-child(1) > '
                                                  'a.btn.btn-small.btn-dark').click()
        przegladarka.find_element_by_id('name').send_keys('Produkt testowy')
        przegladarka.find_element_by_id('price').send_keys('150')
        przegladarka.find_element_by_id('sku').send_keys('0987654321')
        przegladarka.find_element_by_id('redactor-uuid-0').send_keys('Jakiś opis produktu')
        przegladarka.find_element_by_id('short_description').send_keys('Jakiś opis..')

        # ------------------------------Scrollowanie-----------------------------------
        # Scrolluje ponieważ Selenium klika w elementy które są widoczne.

        scroll = ActionChains(przegladarka)
        scroll.move_to_element(przegladarka.find_element_by_css_selector('body > '
                                                                         'section.main-container.notifications-visible'
                                                                         ' > '
                                                                         'section > section > article > section > '
                                                                         'section > '
                                                                         ' form > section.buttons-bar.static > '
                                                                         'section > button'))
        scroll.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(4)
        # -----------------------------------------------------------------------------

        przegladarka.find_element_by_css_selector('body > '
                                                  'section.main-container.notifications-visible > '
                                                  'section > section > article > section > '
                                                  'section > form > table > tbody > tr:nth-child(2) '
                                                  '> td:nth-child(2) >'
                                                  ' section:nth-child(2) > section.clearfix > '
                                                  'section.control-group.pull-left.sibling > '
                                                  'div > button > span.filter-option.pull-left').click()
        przegladarka.find_element_by_css_selector('body > section.main-container.notifications-visible > section >'
                                                  ' section > article > section > section > form > '
                                                  'table > tbody > tr:nth-child(2) > td:nth-child(2) > '
                                                  'section:nth-child(2) > section.clearfix > '
                                                  'section.control-group.pull-left.sibling > div >'
                                                  ' div > ul > li:nth-child(2) > a').click()
        przegladarka.find_element_by_css_selector('body > '
                                                  'section.main-container.notifications-visible > '
                                                  'section > section > article > section > '
                                                  'section > form > table > tbody > tr:nth-child(2) '
                                                  '> td:nth-child(2) >'
                                                  ' section:nth-child(2) > section.clearfix > '
                                                  'section.control-group.pull-left.sibling > '
                                                  'div > button > span.filter-option.pull-left').click()
        przegladarka.find_element_by_css_selector('body > section.main-container.notifications-visible > section >'
                                                  ' section > article > section > section > form > table > tbody > '
                                                  'tr:nth-child(2) > td:nth-child(2) > section:nth-child(2) > '
                                                  'section.clearfix > section.control-group.pull-left.sibling > div > '
                                                  'div > ul > li:nth-child(1) > a > span.text').click()
        przegladarka.find_element_by_id('tax').send_keys('23')
        przegladarka.find_element_by_xpath('/html/body/section[2]/section/section/article'
                                           '/section/section/form/table/tbody/tr[2]/td[2]/'
                                           'section[2]/section[2]/div/button/span[1]').click()
        przegladarka.find_element_by_css_selector('body > section.main-container.notifications-visible >'
                                                  ' section > section > article > section > section >'
                                                  ' form > table > tbody > tr:nth-child(2) >'
                                                  ' td:nth-child(2) > section:nth-child(2) >'
                                                  ' section.control-group > div >'
                                                  ' button > span.filter-option.pull-left').click()
        przegladarka.find_element_by_id('weight').send_keys('100')
        przegladarka.find_element_by_id('width').send_keys('100')
        przegladarka.find_element_by_id('height').send_keys('100')
        przegladarka.find_element_by_id('depth').send_keys('100')
        przegladarka.find_element_by_id('diameter').send_keys('100')
        przegladarka.find_element_by_id('quantity').send_keys('10')
        przegladarka.find_element_by_xpath('//*[@id="addToStockView"]/section[2]/section[2]/div/label').click()
        przegladarka.find_element_by_xpath('/html/body/section[2]/section/section/article/section/'
                                           'section/form/table/tbody/tr[2]/td[2]/section[4]/div/label').click()

        scroll.move_to_element(przegladarka.find_element_by_css_selector('body > '
                                                                         'section.main-container.notifications-visible'
                                                                         ' > '
                                                                         'section > section > article > section > '
                                                                         'section > '
                                                                         ' form > section.buttons-bar.static > '
                                                                         'section > button')).click()
        scroll.perform()
        time.sleep(5)


        # ---------------------------Logowanie -----------------------------------------

    def test_logowanie(self):
        przegladarka = self.driver
        adres = 'https://' + self.nazwa_sklepu + '.shoplo.com/admin'
        przegladarka.get(adres)
        przegladarka.find_element_by_name('email').send_keys('AbCd')
        przegladarka.find_element_by_name('password').send_keys('AbCd')
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/form/button').click()
        assert "Niepoprawny adres email" in przegladarka.find_element_by_css_selector('body > '
                                                                                      'section.overlay-container.'
                                                                                      'login-overlay >'
                                                                                      ' section > section > form >'
                                                                                      ' fieldset.icon-envelope.error >'
                                                                                      ' div > div.tooltip-inner').text

        przegladarka.find_element_by_name('email').clear()
        przegladarka.find_element_by_name('password').clear()
        przegladarka.find_element_by_name('email').send_keys('pawel.lech@outlook.com')
        przegladarka.find_element_by_name('password').send_keys('AbCd')
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/form/button').click()
        time.sleep(3)# bez time.sleep(3) element jest niewidoczny przed kliknięciem, dostajemy bład
        assert "Niepoprawny adres e-mail lub hasło" in przegladarka.find_element_by_css_selector('body > '
                                                                                                'section.'
                                                                                                'overlay-container.'
                                                                                                'login-overlay >'
                                                                                                ' section > section > '
                                                                                                'form > p').text

        przegladarka.find_element_by_name('email').clear()
        przegladarka.find_element_by_name('password').clear()
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/form/button').click()
        assert "Niepoprawny adres email" in przegladarka.find_element_by_css_selector('body > '
                                                                                      'section.overlay-container.'
                                                                                      'login-overlay >'
                                                                                      ' section > section > form >'
                                                                                      ' fieldset.icon-envelope.error >'
                                                                                      ' div > div.tooltip-inner').text
        time.sleep(3)
        assert "Niepoprawny adres e-mail lub hasło" in przegladarka.find_element_by_css_selector('body > '
                                                                                                 'section.overlay-'
                                                                                                 'container.login-'
                                                                                                 'overlay >'
                                                                                                 ' section > '
                                                                                                 'section > form >'
                                                                                                 ' p').text
        assert "Niepoprawne hasło" in przegladarka.find_element_by_css_selector('body > section.overlay-container.'
                                                                                'login-overlay > section > section >'
                                                                                ' form > fieldset.icon-lock.error >'
                                                                                ' div > div.tooltip-inner').text

        przegladarka.find_element_by_name('email').send_keys('pawel.lech@outlook.com')
        przegladarka.find_element_by_name('password').send_keys('lech.123')
        przegladarka.find_element_by_xpath('/html/body/section[1]/section/section/form/button').click()
        assert "witaj w Shoplo" in przegladarka.find_element_by_xpath('/html/body/section[2]/section/'
                                                                      'section/div/div/div/div/h1').text

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


