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

## Reddit ##
Reddit = site_to_be_scraped('http://www.reddit.com')

# Front page subreddits
subreddits_original = Reddit.soup.find_all("a", class_="subreddit hover may-blank")
# Placed into a set to avoid duplicates (since sets do not allow multiple occurances of elements)
subreddits = set(subreddits_original)

# Front page images
images = Reddit.soup.find_all("a", class_="thumbnail")

## TechCrunch ##
TechCrunch = site_to_be_scraped('http://www.techcrunch.com')

# Number of times VCs are mentioned on TC's front page
vc_word_search = TechCrunch.regex(r'VC[s]?')
VCs = len(vc_word_search)

app = Flask(__name__)


@app.route('/')
def front_page(name='AceScrape'):
	return render_template('index.html', subreddits=subreddits, name=name, images=images, VCs=VCs)

if __name__ == '__main__':
	app.run(debug=True)


