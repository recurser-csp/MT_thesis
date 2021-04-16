def bwt(s):
	A = []
	st = []
	for i in range(len(s)):
		# t = s[:]
		t = s[len(s)-i:]+s[:len(s)-i]
		# print(i,t)
		A.append(t)
	A_ = sorted(A)
	# st = ''
	for i in range(len(A_)):
		# print(A_[i])
		st.append(A_[i][-1])
	return st

f = open('../Data/10/dataset_5.txt','r')
character = []
for i in f:
	character.append(i)

for i in range(len(character)):
	character[i] = character[i].split(',')
	character[i].pop(-1)
	for j in range(len(character[i])):
		character[i][j] = int(character[i][j])
	# sigma = character[i][0] 
	# character[i].pop(0)
	# character[i].pop(0)
sigma = 4
mx_mtf =0
for i in range(len(character)):
	character[i] = bwt(character[i])
	# print(character[i])
	temp = 0
	chars = []
	for m in range(sigma+1):
		chars.append(m)
	for k in range(len(character[i])):
		for j in range(len(chars)):
			if chars[j] == character[i][k]:
				temp = temp+1+j
				break
		t_1 = chars.pop(j)
		chars.insert(0,t_1)
	# print(character[i])
	mx_mtf = max(mx_mtf,temp)
	print(temp,len(character[i])-1)
print(mx_mtf)