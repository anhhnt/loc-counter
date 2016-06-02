import re
import time
from dateutil.parser import parse

def readValue(file, pattern):
	while True:
		line = file.readline()
		matchedText = re.search(pattern, line)
		if matchedText != None:
			#print(matchedText.group(0))
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

revisions = range(2)
revisions[0] = []
revisions[1] = []

authors = range(2)
authors[0] = []
authors[1] = []

dates = range(2)
dates[0] = []
dates[1] = []

locs = range(2)
locs[0] = []
locs[1] = []



def readFile(fileName, keyForData):
	with open(fileName) as f:
		while True:
			line = f.readline()
			if line == '':
				break
			matchObj = re.match(r'^Subject\:\s*secutix2\-([a-z]{2})', line)
			if matchObj:
				module = matchObj.group(1)
				print(module)
			elif re.search(r'^Revision$', line) != None:
				revision = readValue(f, r'(\d*)')
				revisions[keyForData].append(revision)
			elif re.search(r'^Author$', line) != None:
				author = readValue(f, r'([a-z]{3})')
				authors[keyForData].append(author)
			elif re.search(r'^Date$', line) != None:
				date = readValue(f, r'^(.*)$')
				b = parse(date[:20])
				#print(str(b.day) + '/' + str(b.month) + '/' + str(b.year))
				realDate = time.strptime(str(b.day) + '/' + str(b.month) + '/' + str(b.year), "%d/%m/%Y")
				dates[keyForData].append(realDate)
			elif re.search(r'^Diff$', line) != None:
				loc = countLoc(f)
				locs[keyForData].append(loc)
				#print(loc)

readFile('./non-reviewed.txt', 0)
print('Found ' + str(len(revisions[0])) + ' unreviewed commmits (includeing reviewed)')
readFile('./reviewed.txt', 1)
print('Found ' + str(len(revisions[1])) + ' reviewed commmits')

# Remove commit in non-reviewed list if it is in reviewed list
toRemoveIndexes = []
for rev in revisions[0]:
	if rev in revisions[1]:
		idx = revisions[0].index(rev)
		toRemoveIndexes.append(idx)

toRemoveIndexes=toRemoveIndexes[::-1]
for idx in toRemoveIndexes:
	print('Delete commit at index: ' + str(idx) + ' because it was already reviewed')
	del revisions[0][idx]
	del authors[0][idx]
	del dates[0][idx]
	del locs[0][idx]

# Counting things to print out
totalNonReviewed = 0
totalReviewed = 0
for loc in locs[0]:
	totalNonReviewed += loc
print('Total non reviewed loc : ' + str(totalNonReviewed))

for loc in locs[1]:
	totalReviewed += loc
print('Total reviewed loc : ' + str(totalReviewed))
