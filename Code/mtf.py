import subprocess
import os
import random

f = open('../Data/4_ideal_2k','r')

character = []
for i in f:
	character.append(i)

for i in range(len(character)):
	character[i] = character[i].split(',')
	character[i].pop(-1)
	for j in range(len(character[i])):
		character[i][j] = int(character[i][j])
	sigma = character[i][0]
	character[i].pop(0)
# print(character)
# print(sigma)
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



	# print(character[k])
	# print("{0},{1},{2}".format(sigma,len(character[k])-1,len(cycl