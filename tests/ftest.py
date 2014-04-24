# Functional testing
from selenium import webdriver
import unittest
import time

server = 'http://localhost:5000/'
live_server = 'http://acescrape.herokuapp.com'

class FuncTest(unittest.TestCase):
	
	def test_server_up(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		self.browser.get(server)
		time.sleep(5) # Use for degugging connection problems
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()
