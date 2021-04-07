import subprocess
import os
import random
# cmd = 'touch ./Data/data.txt'
# os.system(cmd)
for sigma in range(7,8):
	for length in range(10,12):
		print(length)
		cmd = 'rm ../Data/data.txt'
		os.system(cmd)
		# f = open('./Data/data.txt','w').close()
		cmd = './a.out '+str(sigma)+' '+str(length)+' >>../Data/data.txt'
		os.system(cmd)
		f = open('../Data/data.txt','r')

		character = []
		for i in f:
			character = i

		character = character.split(',')
		character.pop(-1)
		for i in range(len(character)):
			character[i] = int(character[i])
		character.insert(0,-1)
		mark = [0]*len(character)

		cycle_number = 1
		cycles = []
		def add_cycle(ch,m,pos):
			cycles.append([])
			mark[pos] = 1
			cur = pos
			while ch[cur]!= pos:
				cycles[-1].append(cur)
				mark[cur] = 1
				cur = ch[cur]
			cycles[-1].append(cur)
			mark[cur] = 1
		# if len(character)>2:
		for i in range(1,len(mark)):
			if mark[i] == 0:
				add_cycle(character,mark,i)
		# print(character)
		# if len(character)>2:
		print("{0},{1},{2}".format(sigma,length,len(cycles)))
		# else:
			# print("{0},{1},0".format(sigma,length))
		# print(cycles)
