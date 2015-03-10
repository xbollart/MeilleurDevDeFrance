file = open('input3.txt','rt')
cash = int(file.readline())
prices = file.readline().split(' ')
de = file.readline().split(' ')
file.close()

case = 1


while cash>0:
	print("case: "+ str(case) + " cash: "+ str(cash) )
	
	deVal = int(de.pop(0)) + int(de.pop(0))
	tmpCase = (case +deVal)%40
	
	if tmpCase == 20:
		tmpCase = 10
	
	price = prices[tmpCase-1]
	cash -= int(price)
	case = tmpCase

print("res: " + str(case))
	
		