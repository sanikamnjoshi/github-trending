# generate time stamp 'ts'
import datetime
ts = datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")

# libs required for core scraping logic
import requests
from bs4 import BeautifulSoup

# lib required for writing data to file in specific location
from os import path

def scrape(lang):
	url_string = "https://github.com/trending?&since=weekly" + "&l=" + lang
	page = requests.get(url_string)
	
	soup = BeautifulSoup(page.content, 'html.parser')
	
	file_path_string = lang + "/" + lang + ts + ".txt"
	file_path = path.relpath(file_path_string)
	file = open(file_path , "w+")
	
	for item in soup.select("h3 a"):
		temp_item = BeautifulSoup(item.get_text().replace('\n',' ') , 'html.parser')
		temp_str = temp_item.get_text().replace(' ','')
		repo_link = "https://github.com/"+temp_str+".git"
		file.write(repo_link + "\n")
		
	file.close()

# for java
scrape("java")
print("Text file of Java trending repos created.")

# for c
scrape("c")
print("Text file of C trending repos created.")

# for cpp
scrape("cpp")
print("Text file of CPP trending repos created.")

# for csharp
scrape("csharp")
print("Text file of C# trending repos created.")
