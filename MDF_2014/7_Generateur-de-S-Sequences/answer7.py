def Cleanstr( instr ):
   outstr = instr.replace(">", "")
   outstr = outstr.replace("<", "")
   outstr = outstr.replace("/", "")
   return outstr

file = open('input1.txt','rt')
line = file.readline()
file.close()

wordlist = []
stack = []
cursor = 0
outstr = ""
position = 2


# split data 
for i in range(len(line)):
	if(line[i] == '<'):
		cursor = i
	elif(line[i] == '>'):
		wordlist.append(line[cursor:i+1])

#convert to new format	
for word in wordlist:
	if word.find('</') == -1:
		stack.append(word)
		val = Cleanstr(word)
		outstr += "(" + val
	else:
		word = word.replace("/", "")
		if(word == stack[-1]):
			stack.pop()
			outstr += ")"
		else:
			#error in str
			errorWord = Cleanstr(word)
			expectedWord = Cleanstr(stack.pop())
			outstr = "E" + " " + str(position) + " " + errorWord + " " + expectedWord 
			break
			
	position += len(word)
		
print(outstr)


