# Functional testing

from bs4 import BeautifulSoup
import unittest
import urllib.request
import re

url = 'http://www.reddit.com'
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data)
body = soup.get_text()

class FuncTest(unittest.TestCase):
	
	def test_title(self):
		assert 'reddit' in soup.title.string
		print(soup.title.string)

	def test_subreddits(self):
		assert 

if __name__ == '__main__':
	print('\n')
	unittest.main()
