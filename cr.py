import re
import time
from dateutil.parser import parse

def readValue(file, pattern):
	while True:
		line = file.readline()
		matchedText = re.search(pattern, line)
		if matchedText != None:
			print(matchedText.group(0))
			return matchedText.group(0)

def countLoc(file):
	loc = 0
	while True:
		line = file.readline()
		if re.match(r'^\+[^\+]{2}.*$', line, re.MULTILINE):
			loc += 1
		elif 'ELCA Subversion service' in line:
			break
	return loc

with open('./reviewed.txt') as f:
	while True:
		line = f.readline()
		if line == '':
			break
		if re.search(r'^Revision$', line) != None:
			revision = readValue(f, r'(\d*)')
		elif re.search(r'^Author$', line) != None:
			author = readValue(f, r'([a-z]{3})')
		elif re.search(r'^Date$', line) != None:
			date = readValue(f, r'^(.*)$')
			b = parse(date[:20])
			#print(str(b.day) + '/' + str(b.month) + '/' + str(b.year))
			realDate = time.strptime(str(b.day) + '/' + str(b.month) + '/' + str(b.year), "%d/%m/%Y")
		elif re.search(r'^Diff$', line) != None:
			loc = countLoc(f)
			print(loc)
