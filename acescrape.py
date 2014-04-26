from bs4 import BeautifulSoup
import os
import urllib.request
import re
from flask import Flask
from flask import render_template
from jinja2 import Template

class site_to_be_scraped:
	def __init__(self, url):
		self.url = url
		self.data = urllib.request.urlopen(url)
		self.soup = BeautifulSoup(self.data)
		self.body = self.soup.get_text()

	def regex(self, string):
		return re.findall(string, self.body)

Reddit = site_to_be_scraped('http://www.reddit.com')
subreddits = Reddit.regex(r'/r/[a-z]+[^1234567890][^comments][^share]')

app = Flask(__name__)


@app.route('/')
def front_page(name='AceScrape'):
	return render_template('index.html', subreddits=subreddits, name=name)

if __name__ == '__main__':
	app.run(debug=True)


