from bs4 import BeautifulSoup
import requests
file = open('total.txt','a')
main_page=1
while True:
	file.write(str(main_page)+'\n')
	website="https://archive.org/details/image?&sort=-downloads&page=%d"%main_page
	website=BeautifulSoup(requests.get(website).content)
	channeldiv=website.findAll("div",{"class":"collection-title C C2"})
	if type(channeldiv) is list:
		break
	else:
		for per_div in channeldiv:
			channel_page=1
			channel_name=per_div.find('a').get('href')
			channel_name="https://archive.org"+channel_name
			print per_div.find('a').find('div').string
			print channel_name
			file.write(str(per_div.find('a').find('div').string)+'\n')
			while True:
				file.write(str(channel_page)+'\n')
				channel_link= "https://archive.org"+per_div.find('a').get('href')+"?&sort=-downloads&page=%d"%channel_page
				channel_content= BeautifulSoup(requests.get(channel_link).content)
				channel_img=channel_content.findAll("div",{"class":"item-ia"})
				if type(channel_img) is list:
					break
				else:
					channel_img = channel_img[1:]
					for img in channel_img:
						link= "https://archive.org/services/img/"+str(img.findAll('div')[4].find('a').find('img').get('source'))[14:]
						print link
						desc= img.find_all('div')[6].find('a').text
						desc=desc.encode('utf-8')
						print desc
						file.write(str(link)+'\n')
						file.write(desc+'\n')
				channel_page+=1				
	main_page+=1
