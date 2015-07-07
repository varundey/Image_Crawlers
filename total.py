from bs4 import BeautifulSoup
import requests
#file = open('total.txt','a')
for main_page in range(1,13284):
	print main_page
	website="https://archive.org/details/image?&sort=-downloads&page=%d"%main_page
	soup=BeautifulSoup(requests.get(website).content)
	channeldiv=soup.findAll("div",{"class":"collection-title C C2"})
	for div in channeldiv:
		for channel_page in range(1,10):
			channel= "https://archive.org"+div.find('a').get('href')+"?&sort=-downloads&page=%d"%channel_page
			print channel
			channel_link= BeautifulSoup(requests.get(channel).content)
			channel_link=channel_link.findAll("img",{"class":"item-img"})
			for img in channel_link:
				img= img.get('source')
				print "https://archive.org/services/img/"+img[14:]
