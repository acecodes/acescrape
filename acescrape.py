from bs4 import BeautifulSoup
import os
import unittest
import urllib.request
import re
from flask import Flask

url = 'http://www.reddit.com'
data = urllib.request.urlopen(url)
soup = BeautifulSoup(data)
body = soup.get_text()

app = Flask(__name__)

@app.route('/')
def title():
	return '<h1>AceScrape!</h1>'

