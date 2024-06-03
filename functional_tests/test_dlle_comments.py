from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from icecream import ic
import time

js_code = "arguments[0].scrollIntoView();"

class TestPortfolioComments(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()
    



    def test1_portfolio_is_displayed(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')

        title = self.browser.find_element(value='title')
        self.assertEqual(title.text, 'Get to know')
        self.browser.execute_script(js_code, title)
        time.sleep(0.1)
        
        picture = self.browser.find_element(value='myImage')
        self.assertAlmostEqual(picture.get_attribute("src"), 'http://127.0.0.1:8000/static/img/deleon_colored.png')
        self.browser.execute_script(js_code, picture)
        time.sleep(0.1)




    def test2_portfolio_section_titles_is_displayed(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')

        intro = self.browser.find_element('class name', 'blue')
        self.assertAlmostEqual(intro.find_element('tag name', 'h1').text, 'Introduction')
        self.browser.execute_script(js_code, intro)
        time.sleep(1)

        currently = self.browser.find_element('class name', 'black')
        self.assertAlmostEqual(currently.find_element('tag name', 'h1').text, 'Currently Doing')
        self.browser.execute_script(js_code, currently)
        time.sleep(1)
        
        passion = self.browser.find_element('class name', 'red')
        self.assertAlmostEqual(passion.find_element('tag name', 'h1').text, 'My Passion')
        self.browser.execute_script(js_code, passion)
        time.sleep(1)
        
        accomplishment = self.browser.find_element('class name', 'green')
        self.assertAlmostEqual(accomplishment.find_element('tag name', 'h1').text, 'My Biggest Accomplishment')
        self.browser.execute_script(js_code, accomplishment)
        time.sleep(1)
        
        lookingfor = self.browser.find_element('class name', 'blue2')
        self.assertAlmostEqual(lookingfor.find_element('tag name', 'h1').text, 'What I am looking for.')
        self.browser.execute_script(js_code, lookingfor)
        time.sleep(1)




    def test3_portfolio_comment_read(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')


        comment = self.browser.find_element('class name', 'comment-area')

        
        #1st Comment in the area
        aTitle = comment.find_element(value='commenth3-1')
        aParagraph = comment.find_element(value='commentp-1')
        ic(aTitle.text)
        ic(aParagraph.text)
        self.assertEqual(aTitle.text, 'Joe Biden - April 9, 2024, 9:40 a.m.')
        self.assertEqual(aParagraph.text, 'This is my first comment in this website!!')
        self.browser.execute_script(js_code, aTitle)
        time.sleep(1)

        #2nd Comment in the area
        bTitle = comment.find_element(value='commenth3-2')
        bParagraph = comment.find_element(value='commentp-2')
        ic(bTitle.text)
        ic(bParagraph.text)
        self.assertEqual(bTitle.text, 'Mark Josh - April 9, 2024, 9:40 a.m.')
        self.assertEqual(bParagraph.text, 'Woww Ganda ng design!!')
        self.browser.execute_script(js_code, bTitle)
        time.sleep(1)
        
        #3rd Comment in the area
        cTitle = comment.find_element(value='commenth3-4')
        cParagraph = comment.find_element(value='commentp-4')
        ic(cTitle.text)
        ic(cParagraph.text)
        self.assertEqual(cTitle.text, 'Anonymous - April 9, 2024, 9:54 a.m.')
        self.assertEqual(cParagraph.text, 'Nice curve m8!')
        self.browser.execute_script(js_code, cTitle)
        time.sleep(1)

        #4th Comment in the area
        dTitle = comment.find_element(value='commenth3-7')
        dParagraph = comment.find_element(value='commentp-7')
        ic(dTitle.text)
        ic(dParagraph.text)
        self.assertEqual(dTitle.text, 'Anonymous - April 10, 2024, 3:21 a.m.')
        self.assertEqual(dParagraph.text, 'Just strollin around the internet!')
        self.browser.execute_script(js_code, dTitle)
        time.sleep(1)

        #5th Comment in the area
        eTitle = comment.find_element(value='commenth3-16')
        eParagraph = comment.find_element(value='commentp-16')
        ic(eTitle.text)
        ic(eParagraph.text)
        self.assertEqual(eTitle.text, 'Donald Trump - April 10, 2024, 6:43 a.m.')
        self.assertEqual(eParagraph.text, 'I will build a wall here..')
        self.browser.execute_script(js_code, eTitle)
        time.sleep(1)




    def test4_portfolio_reply_read(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')

        comment = self.browser.find_element('class name', 'comment-area')

        #1st Reply in the area
        aTitle = comment.find_element(value='replyh3-1')
        aParagraph = comment.find_element(value='replyp-1')
        ic(aTitle.text)
        ic(aParagraph.text)
        self.assertEqual(aTitle.text, 'De Leon - April 10, 2024, 4:38 a.m.')
        self.assertEqual(aParagraph.text, 'Thank you mister president for visiting!')
        self.browser.execute_script(js_code, aTitle)
        time.sleep(1)
        
        #2nd Reply in the area
        bTitle = comment.find_element(value='replyh3-12')
        bParagraph = comment.find_element(value='replyp-12')
        ic(bTitle.text)
        ic(bParagraph.text)
        self.assertEqual(bTitle.text, 'De Leon - April 10, 2024, 6:44 a.m.')
        self.assertEqual(bParagraph.text, "Don't please!!")
        self.browser.execute_script(js_code, bTitle)
        time.sleep(1)




    def test5_portfolio_create_comment(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')

        commentarea = self.browser.find_element('class name', 'comment-area')
        comment = commentarea.find_element('id', 'comment_form')

        #Creating a comment
        cName = comment.find_element('id', 'id_name')
        cBody = comment.find_element('id', 'id_body')
        cSubmit = comment.find_element('id', 'id_csubmit')
        
        self.browser.execute_script(js_code, cName)
        cName.send_keys('Functional Testing')
        cBody.send_keys('This is an automated testing for comment pay no mind to this as this will be deleted soon')
        time.sleep(3)

        cSubmit.click()
        time.sleep(5)




    def test6_portfolio_create_reply(self):
        self.browser.get('http://127.0.0.1:8000/aboutme/')

        #Clicking Reply on Mark Josh
        commentarea = self.browser.find_element('class name', 'comment-area')
        btnReply = self.browser.find_element('xpath', "//button[@value='2']")
        self.browser.execute_script(js_code, commentarea)
        time.sleep(2)
        btnReply.click()
        time.sleep(2)


        wait = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(('id', 'reply_form')))
        time.sleep(2)
        #Checking if Cancel is working
        rCancel = self.browser.find_element('id', 'id_rcancel')
        self.browser.execute_script(js_code, rCancel)
        time.sleep(2)
        rCancel.click()
        time.sleep(2)

        wait = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(('class name', 'comment-area')))
        commentarea = self.browser.find_element('class name', 'comment-area')
        btnReply = self.browser.find_element('xpath', "//button[@value='2']")
        self.browser.execute_script(js_code, commentarea)
        time.sleep(2)
        btnReply.click()
        time.sleep(2)

        #Creating a Reply for Mark Josh
        wait = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(('id', 'reply_form')))
        time.sleep(2)
        rName = self.browser.find_element('id', 'id_name')
        rReply = self.browser.find_element('id', 'id_reply')
        rSubmit = self.browser.find_element('id', 'id_rsubmit')
        
        self.browser.execute_script(js_code, rName)
        rName.send_keys('Functional Testing')
        rReply.send_keys('This is an automated testing for comment pay no mind to this as this will be deleted soon')
        time.sleep(3)
        
        rSubmit.click()
        time.sleep(3)
        commentarea = self.browser.find_element('class name', 'comment-area')
        self.browser.execute_script(js_code, commentarea)
        time.sleep(4)


        