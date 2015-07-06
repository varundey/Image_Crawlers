from bs4 import BeautifulSoup
import requests
import threading
def fetch(no):
	website="https://archive.org/details/coverartarchive?&sort=-downloads&page=%d"%no
	r=requests.get(website)
	soup=BeautifulSoup(r.content)
	img=soup.findAll("img",{"class":"item-img"})
	for i in img:
		x=i.get("source")
		x="https://archive.org/services/img/"+x[14:]
		file.write(x+'\n')
'''
for no in range(5559):
	if threading.activeCount()<20:
		threading.Thread(target=fetch,args=(no,)).start()
	else:
		while True:
			if threading.activeCount()<20:
				threading.Thread(target=fetch,args=(no,)).start()
				break
				
				'''
file = open('album_art_thread1.txt','a')			
T=threading.Thread	
for no in range(5565):
	while threading.activeCount()>20:
		continue
	t=T(target=fetch, args=(no,))
	t.start()
