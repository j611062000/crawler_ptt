from bs4 import BeautifulSoup
import requests



for i in range(1300,1355):
	result=requests.get("https://www.ptt.cc/bbs/Soft_Job/index"+str(i)+".html")
	soup=BeautifulSoup(result.content,"lxml")
	soup_title = soup.find_all(class_="title")
	soup_author=soup.find_all(class_="author")
	
	data={}
	for j in range(len(soup_title)):
		data[j]=[soup_author[j].get_text(),soup_title[j].get_text().rstrip()[1:]]

	for elemet in data:
		print("Author: {:^15} Title: {}".format(data[elemet][0],data[elemet][1]))