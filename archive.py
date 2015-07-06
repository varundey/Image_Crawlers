from bs4 import BeautifulSoup
import requests
import threading
#file = open('archive1.txt','a')
for page in range(1,13272):
    li=[]
    website="https://archive.org/details/image?&sort=-downloads&page=%d"%page
    r=requests.get(website)
    soup=BeautifulSoup(r.content)
    img=soup.findAll("div",{"class":"collection-title C C2"})
    for i in img:
        x= i.find('a').find('div').text
     	print x
        with open("dal.txt", "a") as f:
    	    f.write(x)    	    
    	f.close()
