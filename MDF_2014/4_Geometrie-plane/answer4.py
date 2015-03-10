file = open('input3.txt','rt')
nbrec = int(file.readline())

xlist = []
ylist = []

for i in range(nbrec):

	points = file.readline().split(' ')
	
	xlist.append(int(points[0]))
	xlist.append(int(points[2]))
	
	ylist.append(int(points[1]))
	ylist.append(int(points[3]))
	
minx = min(xlist)
maxx = max(xlist)
miny = min(ylist)
maxy = max(ylist)

print(str(minx) +" " + str(miny)+" " + str(minx)+" " + str(maxy)+" "  + str(maxx) +" " + str(miny)+" "  + str(maxx)+" "  + str(maxy))