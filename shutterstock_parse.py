import MySQLdb
db = MySQLdb.connect("localhost","root","root","TESTDB")
cursor = db.cursor()
import re
import requests
from bs4 import BeautifulSoup as b
url="http://www.shutterstock.com/cat.mhtml?autocomplete_id=&language=en&lang=en&search_source=&safesearch=1&version=llv1&searchterm=&media_type=images"
page_categories=[]
soup=b(requests.get(url).content)
soup=soup.find('div',{"class":"secondary_links clearfix"}).findAll("ul")
for per_ul in soup:
	li=per_ul.findAll("li")
	for per_li in li:
		page_categories.append(str(per_li.text))

file = open('shutterstock.txt', 'r')
i=0


x=file.readlines()
while(i<len(x)):
										#category
	if x[i].replace("\n","") in  page_categories:
		a= str(x[i].replace("\n","").replace("\"",""))
		i+=1
								#category link
	elif re.search(r"http.*.html",x[i]):
		b= str(x[i].replace("\n","").replace("\"",""))
		i+=1
							#link
	elif re.search(r"http.*.jpg",x[i]):
		d= str(x[i].replace("\n","").replace("\"",""))
		i+=1
							#title
	else:
		title= str(x[i].replace("\n","").replace("\"",""))
		c=title
		sql = '''INSERT INTO shutterstock(category,cat_link,title,title_link) VALUES ("%s","%s","%s","%s")''' %(a,b,c,d)
		cursor.execute(sql)
		db.commit()
		i+=1
	



