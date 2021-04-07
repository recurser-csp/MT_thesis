import subprocess
import os
import random

f = open('../Data/ideal_seq.txt','r')

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

c = len(character[0])-2
for k in range(len(character)):

	c+=1
	if character[k][1] == -1:
		print("{0},{1},-1".format(sigma,c))
		continue


	mark = [0]*len(character[k])
	cycle_number = 1
	cycles = []
	def add_cycle(ch,m,pos):
		temp = 0
		cycles.append([])
		mark[pos] = 1
		cur = pos
		while ch[cur]!= pos:
			temp+=1
			# print(temp,len(character[k]),cur)
			cycles[-1].append(cur)
			mark[cur] = 1
			cur = ch[cur]
		cycles[-1].append(cur)
		mark[cur] = 1

	for i in range(1,len(mark)):
		if mark[i] == 0:
			add_cycle(character[k],mark,i)

	print("{0},{1},{2}".format(sigma,len(character[k])-1,len(cycles)))
