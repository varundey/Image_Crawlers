import requests
from bs4 import BeautifulSoup as b
url="http://www.bigstockphoto.com/"


#### getting inside website ####
soup=b(requests.get(url).content,"lxml")

###finding all category links
categories=soup.findAll("div",{"class":"row-fluid"})[4].findAll("a")

####picking one category at a time
for per_category in categories:
	 
	cat="http://www.bigstockphoto.com"+str(per_category.get('href'))
	
	category_name = per_category.text
	print category_name
	
	####just for the lulz
	cat = cat.split("category/")[0]+"?category="+cat.split("category/")[1][:-1]
	cat = cat.split("?")[0]+"?start=0&"+cat.split("?")[1]
	print cat								##category link
	
	####initialising page from 0
	page = 0

	#####iterating over page of category
	while True:
		
		#####going inside each page
		
		cat="http://www.bigstockphoto.com/search/?start=%d"%page + "&category=" + cat.split("=")[2]
		print cat								###############category page link  DO NOT INDEX   ##############
		
		page_soup = b(requests.get(cat).content,"lxml")

		####finding each image in page
		imgs = page_soup.findAll("div",{"class":"media"})
		if imgs:			
			#####iterating over each img
			for img in imgs:
#				try:
				img_soup =b(requests.get("http://www.bigstockphoto.com"+img.find('a').get('href')).content,"lxml")
				
				img_info = img_soup.findAll("div",{"class":"bsp-shadow"})[1]

				img_link =	img.find("div").find("img").get("src")	

				img_desc = img_soup.find('h1',{"class":"light"}).text
			
				height = img_info.get("style").split(":")[1].split(";")[0]
				
				width = img_soup.find("div",{"class":"left_wrapper"}).findAll('div')[1].get("style").split(":")[1].split(";")[0]
											
				print img_link
				
				print img_desc
				
				print height
				
				print width
				
#				except Exception as e:
#					print e
#					continue	
	
			page+=150
							
		else:
			break
