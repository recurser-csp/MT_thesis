def bwt(s):
	A = []
	st = []
	for i in range(len(s)):
		# t = s[:]
		t = s[len(s)-i:]+s[:len(s)-i]
		# print(i,t)
		A.append(t)
	A_ = sorted(A)
	for i in range(len(A_)):
		st.append(A_[i][-1])
	return st
def cal_mtf(sigma,ch):
	# for i in range(len(character)):
	ch = bwt(ch)
	# print(character[i])
	temp = 0    # initial MTF value
	chars = []
	for m in range(sigma+1):
		chars.append(m)
	for k in range(len(ch)):
		for j in range(len(chars)):
			if chars[j] == ch[k]:
				temp = temp+1+j
				break
		t_1 = chars.pop(j)
		chars.insert(0,t_1)     #move_to_front
	# print(character[i])
	return temp

# f = open('../Data/10/2k_single','r')
f = open('../Data/10/150_single','r')
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
# print(sigma)

# character = [[1,2,3,4,5,6,7,8,9,0]]

for i in range(700):
	t = character[-1].copy()
	max_mtf = 0
	max_mtf_str = t
	for k in range(1,sigma+1):
		x = t.copy()
		x.insert(0,k)
		# print(x)
		cur_mtf = cal_mtf(sigma,x)
		if cur_mtf>=max_mtf:
			max_mtf_str = x
			max_mtf = cur_mtf

	character.append(max_mtf_str)
	# print(character)
	print(max_mtf,len(max_mtf_str))

