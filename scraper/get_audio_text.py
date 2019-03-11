from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup
import time
import numpy as np

url = 'https://etc.usf.edu/lit2go/books/'

html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
audio_book_link_list = soup.find('section',attrs={'id':'results'}).find_all('figure')
final_book_links = []

for a in audio_book_link_list:
	link = a.find('figcaption',attrs={'class':'title'}).find('a')['href']
	chapter_link = []
	html = urlopen(link)
	soup = BeautifulSoup(html,'html.parser')
	chapters = soup.find('dl').find_all('dt')
	for ch in chapters:
		chapter_link.append(ch.find('a')['href'])
	final_book_links.append({'Book_link':link, 'Chapter_links':chapter_link})
	ff = open('book_chapter_links.txt','w')
	ff.write(str(final_book_links))
	ff.close()
	print(link)