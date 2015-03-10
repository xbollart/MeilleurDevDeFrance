file = open('input3.txt','rt')
instr = file.readline()
file.close()

outstr = ""
prev = ""
nb = 0

for a in range(len(instr)):
	
	if(prev == ""):
		prev = instr[a]
		nb += 1
		
	elif(prev == instr[a]):
		nb += 1
		
	elif(prev != instr[a]):
	
		if(nb<=2):
			outstr =  outstr + nb*prev

		else:
			outstr = outstr + str(nb) + prev
			
		prev = instr[a]
		nb = 1


if(nb>0):
	if(nb<=2):
		outstr =  outstr + nb*prev
	else:
		outstr = outstr + str(nb) + prev
		
		
print ("final res: "+ outstr)