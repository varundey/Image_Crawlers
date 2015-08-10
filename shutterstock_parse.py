
import MySQLdb

db = MySQLdb.connect("localhost","root","root","TESTDB")
cursor = db.cursor()

import re
import requests
from bs4 import BeautifulSoup as b
url="http://www.shutterstock.com/cat.mhtml?autocomplete_id=&language=en&lang=en&search_source=&safesearch=1&version=llv1&searchterm=&media_type=images"
category=[]
soup=b(requests.get(url).content)
soup=soup.find('div',{"class":"secondary_links clearfix"}).findAll("ul")
for per_ul in soup:
	li=per_ul.findAll("li")
	for per_li in li:
		category.append(str(per_li.text))

file = open('shutterstock.txt', 'r')
i=0
x=file.readlines()
while(i<len(x)):
	if x[i].replace("\n","") in  category:
		y= str(x[i].replace("\n",""))
		print y
		sql = "INSERT INTO 'shutterstock' (`category`);"%(y)
		cursor.execute(sql)
		db.commit()
		i+=1
		
	elif re.search(r"http.*.html",x[i]):
		y= str(x[i].replace("\n",""))
		print y
		sql = "INSERT INTO 'shutterstock' (`cat_link`);"%(y)
		cursor.execute(sql)
		db.commit()
		i+=1
	elif re.search(r"http.*.jpg",x[i]):
		y= str(x[i].replace("\n",""))
		print y
		sql = "INSERT INTO 'shutterstock' (`title_link`);"%(y)
		cursor.execute(sql)
		db.commit()
		i+=1
	else:
		y= str(x[i].replace("\n",""))
		print y
		sql = "INSERT INTO 'shutterstock' (`title`);"%(y)
		cursor.execute(sql)
		db.commit()
		i+=1
