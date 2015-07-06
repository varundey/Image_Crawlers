from bs4 import BeautifulSoup
import requests
file = open('album_art.txt','a')
for no in range(5559):
	website="https://archive.org/details/coverartarchive?&sort=-downloads&page=%d"%no
	r=requests.get(website)
	soup=BeautifulSoup(r.content)
	img=soup.findAll("img",{"class":"item-img"})
	for i in img:
		x=i.get("source")
		x="https://archive.org/services/img/"+x[14:]
		file.write(x+'\n')
