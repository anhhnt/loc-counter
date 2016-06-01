import re

def process(line):
	if 'Sent:' in line:
		print(line)
	elif 'Subject:' in line:
		matchObj = re.search(r'secutix2\-[a-z]*: svn commit \(([a-z]{3})\)', line, re.I)
		if matchObj:
			print(matchObj.group(1))
		else:
			print("No match!!" + line)
with open('./reviewed.txt') as f:
	for line in f:
		process(line)