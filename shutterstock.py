import requests
from bs4 import BeautifulSoup as b
file=open("shutterstock.txt",'a')
url="http://www.shutterstock.com/cat.mhtml?autocomplete_id=&language=en&lang=en&search_source=&safesearch=1&version=llv1&searchterm=&media_type=images"
soup=b(requests.get(url).content)
soup=soup.find("div",{"class":"secondary_links clearfix"})
ul=soup.findAll("ul")
for per_ul in ul:
	li=per_ul.findAll('li')
	for per_li in li:
		category=per_li.find('a').text
		category_link="http://www.shutterstock.com"+per_li.find('a').get('href')
		print category
		file.write(str(category)+'\n')
		print category_link
		file.write(str(category_link)+'\n')
		page=1
		while True:
			print page
			category_page=category_link+"?page=%d&thumb_size=mosaic"%page
			category_page=b(requests.get(category_page).content)
			image=category_page.findAll("span",{"class":"gc_clip"})
			if (type(image) is list):
				break
			for per_image in image:
				link= per_image.find('img').get('src')
#				print link
				file.write(str(link)+'\n')
				desc= per_image.find('img').get('alt').encode('utf-8')
				file.write(str(desc)+'\n')
			page+=1
