def bwt(s):
	A = []
	st = []
	for i in range(len(s)):
		t = s[len(s)-i:]+s[:len(s)-i]
		A.append(t)
	A_ = sorted(A)
	# print(A_)
	for i in range(len(A_)):
		st.append(A_[i][-1])
	t = 0
	for i in range(len(A_[-1])):
		if A_[-1][i] == 0:
			t = i
			break
	return [st,t]

f = open('../Data/10/2k_single','r')
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
	character[i].pop(0)
# character = [[1,2,3,4,5,6,7,8,9,0]]
for i in range(1950):
	t = character[-1].copy()
	t.pop(len(t)-bwt(t)[1]-2)
	character.append(t)
# print(character)

for i in range(len(character)):
	character[i] = bwt(character[i])[0]
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
	print(temp,len(character[i])-1)
