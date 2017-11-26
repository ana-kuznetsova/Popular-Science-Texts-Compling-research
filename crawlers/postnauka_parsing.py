import re
import json
from lxml import html
from bs4 import BeautifulSoup
import sys

class TextProcessor():
	def __init__(self):
		self.ws = {}
	def send(self, word):
		if(not (word in self.ws)):
			self.ws[word] = 0
		self.ws[word] += 1
	def words(self):
		return self.ws
	def sorted(self):
		return sorted(list(self.ws.items()), key=lambda w: -w[1])[:3]
		

def words(str):
	clean_line = re.sub('[\W\d_-]+', ' ', str.lower().strip())
	line_words = re.split(' +', clean_line)
	return [w for w in line_words if w]
	
# with open("C:\\Users\\Ksenia\\Documents\\SciPop\\postnaukanew.json", encoding="utf-8") as fp:
if (len(sys.argv) == 1):
	print("Usage: {0} path-to-file".format(sys.argv[0]))
	exit()
with open(sys.argv[1], encoding="utf-8") as fp:
	proc = TextProcessor()
	for row in fp:
		if (len(row)<3): # не нужны первая и последняя
			continue
		if(row[-2] == ','):
			row = row[:-2]
		obj = json.loads(row)
		soup = BeautifulSoup(obj['content'], 'html.parser')
		for word in words(soup.get_text()):
			proc.send(word)
	print(proc.sorted())
        
        