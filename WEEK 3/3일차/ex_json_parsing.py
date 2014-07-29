#-*- coding: utf-8 -*-
# json 파싱하기

import urllib
import json

htmltext = urllib.urlopen("http://codingsroom.com/likelion/json_example2.php")

data = json.load(htmltext)

print "MEM_NUM      Age                Job                  MEM_CODE          etc"
for element in data['data']:
	print '%5s %10s %20s %25s' % (element["MEM_NUM"], element["age"], element["job"], element["MEM_CODE"])
	if element['age'] > 50:
		print '%77s' % 'Old'
	else:
		print

hello = "Hello World!"
wow = "wow"

print "%s %s" % (hello, wow)