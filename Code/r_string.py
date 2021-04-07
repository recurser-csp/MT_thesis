import random
randomlist = []
sigma = 10
character = []
for i in range(50,2001):
	t = []
	t.append(i+1)
	for j in range(i):
		t.append(random.randint(1,sigma))
	t.append(0)
	character.append(t)

mtf = []
# print(chars)
c = len(character[0])-2
for k in range(len(character)):
	temp = 0
	chars = []
	for i in range(sigma+1):
		chars.append(i)
	for i in range(1,len(character[k])):
		for j in range(len(chars)):
			if chars[j] == character[k][i]:
				temp = temp+1+j
				break
		t_1 = chars.pop(j)
		chars.insert(0,t_1)
	print(temp,len(character[k])-1)
