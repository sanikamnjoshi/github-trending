import requests
from bs4 import BeautifulSoup, SoupStrainer

page = requests.get("https://github.com/trending")
response = requests.request('GET',"https://github.com/trending")

pageSoup = BeautifulSoup(page.content, 'html.parser')

for item in pageSoup.select("h3 a"):
	tempItem = BeautifulSoup(item.get_text().replace('\n',' ') , 'html.parser')
	tempStr = tempItem.get_text().replace(' ','')
	repoLink = "https://github.com/"+tempStr+".git"
	print(repoLink)
	
