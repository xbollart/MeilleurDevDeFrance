file = open('input1.txt','rt')
lines = file.readlines()
file.close()

a= 0

for nb in lines:
	a += int(nb)

color = ['orange','jaune','vert', 'rose', 'bleu', 'violet']
	
print(color[a%6-1])

