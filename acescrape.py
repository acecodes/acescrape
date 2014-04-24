from bs4 import BeautifulSoup
import os
import urllib.request
import re
from flask import Flask
from flask import render_template

# Scraping parameters
class site_to_be_scraped:
	def __init__(self, url):
		self.url = url
		data = urllib.request.urlopen(url)
		soup = BeautifulSoup(data)
		body = soup.get_text()

Reddit = site_to_be_scraped('http://www.reddit.com')


app = Flask(__name__)

@app.route('/')
def front_page(name='AceScrape'):
	return render_template('index.html', name=name)



if __name__ == '__main__':
	app.run(debug=True)


