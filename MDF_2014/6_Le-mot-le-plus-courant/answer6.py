from collections import defaultdict 

file = open('input1.txt','rt')
lines = file.readlines()
file.close()

#clean input data
for i in range(len(lines)):
	lines[i-1] = lines[i-1].replace("\n", "");
	lines[i-1] = lines[i-1].replace(".","")
	lines[i-1] = lines[i-1].replace(",","")
	lines[i-1] = lines[i-1].lower()
	lines[i-1] = lines[i-1].replace("l'","")

#load dico	
wordDico= defaultdict(int)
for line in lines:
	wordList = line.split(' ')
	for word in wordList:
		if(word != ''):
			wordDico[word] += 1 


# remove unvalid word	
keys = wordDico.keys()

print(keys)
for key in keys:
	counter = 0
	for line in lines:
		wordList = line.split(' ')
		for word in wordList:
			if word == key:
				counter += 1
				break
	if counter == len(lines):
		wordDico[key] = -1
		

#format output
maxval = max(wordDico.values())
outnb=0

while maxval > 0:
	outlist = []
	for key in wordDico.keys():
		if wordDico[key] == maxval:
			outlist.append(key)
	outlist.sort()
	for val in outlist:
		if outnb >=3:
			break
		print(str(maxval) + " " + val)
		outnb += 1
	
	maxval -= 1
		
		

