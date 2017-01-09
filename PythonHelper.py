
# run program with stdin stdout
python main.py < input.txt > output.txt

## Reader
#open for reading
file = open('input1.txt','rt')

#close
file.close()

#multiple lines 
lines = file.readlines()

#read line and split to list
prices = file.readline().split(' ')

#read line and convert to int
cash = int(file.readline())

# remove \n on string
str = line.rstrip('\n')

##List
#init empty
liste = []

#init with values
color = ['orange','jaune','vert', 'rose', 'bleu', 'violet']

#dequeue first value
liste.pop(0)

#dequeue last value
stack.pop()

#add value
xlist.append(int("5"))

#sort
datalist.sort()


##dico
#init empty
modedico = {}

#add val
if(val in modedico):
	modedico[val] = modedico[val] +1
else:
	modedico[val] = 1
	
#default dico
from collections import defaultdict 
wordDico= defaultdict(int)
for word in wordList:
	wordDico[word] += 1
	
#Dico to list
keys = wordDico.keys()

#Dico get value
dico.get(ext[1], "UNKNOWN")


##math
#modulo
color[a%6-1]

#max min
maxval = max(datalist)
minval = min(datalist)

#median
datalist.sort()
medianeval =(datalist[int(len(datalist)/2)-1]+datalist[int(len(datalist)/2)])/2

#length
len(datalist)


##loop
#foreach
for nb in lines:

#while
while cash>0:

#for
for a in range(len(instr)):
for i in range(9):
for val in modedico.keys():


##string
#cast to int
int(nb)

#remove last character
line = line[:-1]

#clean data
lines[i-1] = lines[i-1].replace("\n", "");
lines[i-1] = lines[i-1].replace(".","")
lines[i-1] = lines[i-1].lower()

#convert to bin
result = format(ord(charVal), 'b')

##Output
print("res: " + str(case))

##metod
def Cleanstr( instr ):
   outstr = instr.replace(">", "")
   return outstr
   
val = Cleanstr(word)



