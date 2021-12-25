from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class VideoSharerTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/')
    #find the elements you need to submit form
    article = selenium.find_element_by_tag_name('article')
    assert article true
    button_array = selenium.find_element_by_class('nav-item nav-link')
    login = button_array[0]    
    login.send_keys(Keys.RETURN)
    #check result; page source looks at entire html document
    assert 'Join Today' in selenium.page_source