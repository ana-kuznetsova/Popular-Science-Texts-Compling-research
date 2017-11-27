import re
import json
from lxml import html
from bs4 import BeautifulSoup
import sys
import os

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
		

class FileProcessor():
	def __init__(self, root_dir):
		self.root_dir = root_dir
		os.makedirs(root_dir, exist_ok=True)
		self.current_dir_number = 1
		self.current_file_number = 0
		
	def current_dir(self):
		dir = os.path.join(self.root_dir, str(self.current_dir_number))
		os.makedirs(dir, exist_ok=True)
		if(len(os.listdir(dir)) < 500):
			return dir
		self.current_dir_number += 1
		self.current_file_number = 0
		return self.current_dir()
	
	def current_file(self):
		self.current_file_number += 1
		return os.path.join(self.current_dir(), str(self.current_file_number))
	
	def send(self, title, body):
		path = self.current_file()
		f = open('{0}_{1}.txt'.format(path, title), 'w', encoding="utf-8")
		f.write(body)
		f.close()
		
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
	files = FileProcessor(root_dir='out3')
	for row in fp:
		if (len(row)<3): # не нужны первая и последняя
			continue
		if(row[-2] == ','):
			row = row[:-2]
		obj = json.loads(row)
		soup = BeautifulSoup(obj['content'], 'html.parser')
		for div in soup.find_all("div", {'class': True}):
			div.decompose()
		files.send(obj['id'], soup.get_text())
		for word in words(soup.get_text()):
			proc.send(word)
	print(proc.sorted())
        
        