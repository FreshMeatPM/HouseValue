#coding=utf-8
import urllib
from bs4 import BeautifulSoup
import time
import re
import codecs
import sys

def getData(s):
	soup = BeautifulSoup(s)
    	z = ""
    	m = soup.find("div",class_="list-wrap")
    	tmp = m.findAll('li')
    	for obj in tmp:
    		#try:
		title_obj = obj.find("div",class_="info-panel").find("h2").find("a").contents
		where = obj.find("div",class_="col-1").find("div",class_="where")
		xiaoqu_obj = where.find("a").find("span").contents
		zone_obj = where.find("span",class_="zone").find("span").contents
		meters_obj = where.find("span",class_="meters").contents
		region_obj = obj.find("span",class_="region").contents
		price_obj = obj.find("div",class_="price").find("span").contents
		up_date_obj = obj.find("div",class_="price-pre").contents
		title = title_obj[0]
		xiaoqu = str(xiaoqu_obj[0].rstrip())
		zone = str(zone_obj[0].rstrip())
		meters = str(meters_obj[0].rstrip())
		price = str(price_obj[0])
		up_date = str(up_date_obj[0])
		region = str(region_obj[0])
		house_info = title + ',' + xiaoqu +  ',' + zone + ',' + meters + ',' + price + ',' + region + ',' + up_date
		#print house_info
    		#except Exception, e:
            	#	print e
            	z += house_info + '\r\n'
    	return z

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

reload(sys)
sys.setdefaultencoding('utf8')
fh = codecs.open("HaidianYiJu.txt", "w", "utf-8")

for p in range(1,2):
	url = "http://bj.lianjia.com/zufang/haidian/pg"+str(p) +"l1/"
    	html = getHtml(url)
    	data = getData(html)
    	#print data
	fh.write(data)

fh.close()