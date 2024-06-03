from selenium import webdriver
from django.test import LiveServerTestCase
from icecream import ic
import time


class TestPortfolioComments(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()

    def test_handler400(self):
        self.browser.get('http://127.0.0.1:8000/handler400/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '400 Error Page')
        self.assertEqual(header.text, 'Bad Request')
        time.sleep(5)
        btn.click()
        time.sleep(2)



    def test_handler401(self):
        self.browser.get('http://127.0.0.1:8000/handler401/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '401 Error Page')
        self.assertEqual(header.text, 'Unauthorized Access')
        time.sleep(5)
        btn.click()
        time.sleep(2)
        


    def test_handler402(self):
        self.browser.get('http://127.0.0.1:8000/handler402/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '402 Error Page')
        self.assertEqual(header.text, 'Payment Required')
        time.sleep(5)
        btn.click()
        time.sleep(2)
        


    def test_handler403(self):
        self.browser.get('http://127.0.0.1:8000/handler403/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '403 Error Page')
        self.assertEqual(header.text, 'Forbidden Error')
        time.sleep(5)
        btn.click()
        time.sleep(2)



    def test_handler404_multiple(self):
        #1st Test
        self.browser.get('http://127.0.0.1:8000/dwkaofas/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '404 Error Page')
        self.assertEqual(header.text, 'Page Not Found')
        time.sleep(5)
        btn.click()
        time.sleep(2)

        #2nd Test
        self.browser.get('http://127.0.0.1:8000/Kahitanongurls/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        self.assertEqual(title, '404 Error Page')
        self.assertEqual(header.text, 'Page Not Found')
        time.sleep(3)
        btn.click()
        time.sleep(2)

        #3rd Test
        self.browser.get('http://127.0.0.1:8000/OPkspoakdpaoskd/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        self.assertEqual(title, '404 Error Page')
        self.assertEqual(header.text, 'Page Not Found')
        time.sleep(3)
        btn.click()
        time.sleep(2)



    def test_handler408(self):
        self.browser.get('http://127.0.0.1:8000/handler408/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '408 Error Page')
        self.assertEqual(header.text, 'Request Timeout')
        time.sleep(5)
        btn.click()
        time.sleep(2)



    def test_handler500(self):
        self.browser.get('http://127.0.0.1:8000/check500/')
        
        title = self.browser.title
        div = self.browser.find_element('class name', 'errorbg')
        header = div.find_element('tag name', 'h3')
        btn = self.browser.find_element('class name', 'btn')
        ic(title)
        ic(header.text)
        self.assertEqual(title, '500 Error Page')
        self.assertEqual(header.text, 'Server Error')
        time.sleep(5)
        btn.click()
        time.sleep(2)

