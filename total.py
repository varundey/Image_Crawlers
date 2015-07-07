from bs4 import BeautifulSoup
import requests
#file = open('total.txt','a')
for page in range(1,13272):
        print page
        website="https://archive.org/details/image?&sort=-downloads&page=%d"%page
        r=requests.get(website)
        soup=BeautifulSoup(r.content)
        channel=soup.findAll("div",{"class":"collection-title C C2"})
	for c in channel:
	        h= "https://archive.org"+c.find('a').get('href')
		q= BeautifulSoup(requests.get(h).content)
#                print q
		m=q.findAll("div",{"class":"tile-img"})
#		print m
		for x in m:
			print x.find('a').find('img').get('source')

	#print x
		#x="https://archive.org"+str(i)
		#print x
'''
		folder=BeautifulSoup(requests.get(x).content)
		img=soup.findAll("img",{"class":"item-img"})
		for z in img:
			p=z.get("source")
			print p
'''
	
'''
	for i in channel:
		i=requests.get(i)
		i=BeautifulSoup(i.content)
		img=soup.findAll("img",{"class":"item-img"})
		print img
	'''
