file = open('input3.txt','rt')
dim = int(file.readline())

datalist = []
coef = dim/4
linenb = 0

# filter useful data
for i in range(dim):
	
	line = file.readline().split(' ')
	line = line[:-1]
	if linenb>coef-1 and linenb< dim-coef:
		for j in range(len(line)) :
			if j>coef-1 and j< dim-coef:
 				datalist.append(int(line[j]))
	
	linenb += 1
		
# min max
minval = min(datalist)
maxval = max(datalist)

#median
datalist.sort()
medianeval =(datalist[int(len(datalist)/2)-1]+datalist[int(len(datalist)/2)])/2

print("mediane: " + str(medianeval))

#mode
modedico = {}

for val in datalist:

	if(val in modedico):
		modedico[val] = modedico[val] +1
	else:
		modedico[val] = 1



		
maxmod = max(modedico.values())
maxlist = []


for val in modedico.keys():
	
	if(modedico[val] == maxmod):
		maxlist.append(val)
		
print(maxlist)

modval = min(maxlist)

print(str(minval) + " " + str(maxval) + " " + str(medianeval)+ " " + str(modval))		
	
        

