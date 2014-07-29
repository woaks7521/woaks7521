#-*- coding: utf-8 -*-
# JTBC 뉴스 속보 xml문서 파싱하기

import urllib
from xml.etree.ElementTree import parse

import webbrowser

xml = urllib.urlopen('http://rss.joins.com/joins_money_list.xml')	# 속보

tree = parse(xml)		# xml 파싱하여 나뭇가지 구조 얻기
root = tree.getroot()	# root태그 얻어오기

list_title=[]
list_link = []

i = 0
for parent in root.getiterator():	# root태그부터 시작하여 모든 태그를 반복
	for child in parent.findall("item"):
		list_title.append(child.findtext("title"))
		list_link.append(child.findtext("link"))
		i += 1
		print i,

		print child.findtext("title")


print
num = raw_input("보고싶은 뉴스번호를 입력하세요 : ")
num = int(num)

if num < 1 or num > 30:
	print "0부터 30까지 번호를 입력하세요"
elif num > 0 and num < 31:
	print list_title
	print list_link
	webbrowser.open(list_link)
