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
# character = [[3,2,1,4,4,0]]
character = []

# file read code

f = open('../Data/10/150_single','r')
# character = []
c = []
for i in f:
	c.append(i)

for i in range(len(c)):
	c[i] = c[i].split(',')
	c[i].pop(-1)
	for j in range(len(c[i])):
		c[i][j] = int(c[i][j])
	sigma = c[i][0]
	c[i].pop(0)
	c[i].pop(0)
# print(c)
character=c.copy()
# file read code




bwt_list = []
# for i in f:
# 	character.append(i)
sigma = 10
for i in range(1950):
	next_char = sigma
	bwt_list.append(bwt(character[-1]))
	count = [0 for j in range(sigma+1)]
	for j in range(len(character[-1])):
		count[character[-1][j]]+=1
	for j in range(1,sigma):
		if count[j]<count[j+1]:
			next_char = j
			break
	pos = 2
	i_c = [ 1 for j in range(sigma+1)]
	for j in range(1,sigma+1):
		i_c[j] = pos
		pos+=count[j]
	i_c_copy = i_c.copy()
	bw = bwt_list[-1]
	for j in range(len(bw)):
		t = bw[j]
		bw[j] = i_c[bw[j]]
		i_c[t]+=1
	st = 0
	i_c = i_c_copy.copy()
	if(next_char<sigma):
		st = i_c[next_char+1]
	if(next_char == sigma):
		st = len(bw)+1
	for j in range(sigma+1):
		if(i_c[j]>=st):
			i_c[j]+=1
	bw.insert(0,0)
	next_bw = bw.copy()
	next_bw.append(0)
	for j in range(1,len(next_bw)):
		if(next_bw[j] >= st):
			next_bw[j]+=1
		if(j == next_bw[j]):
			t = next_bw[j]
			next_bw[j] = next_bw[j-1]
			next_bw[j-1] = t
	next_bw[-1] = st
	# Cycle Merging
	# print(next_bw)
	mark = [0 for j in range(len(next_bw))]
	cycle_pos = 1
	flag_1=0
	j=1
	reset = 0
	while j<len(next_bw):
		if reset == 1:
			# print(next_bw)
			j=1
			mark = [0 for m in range(len(next_bw))]
			cycle_pos=1
			reset=0
			flag_1=0
		if(next_bw[cycle_pos]==1 and j<len(next_bw)):
			# k = cycle_pos+1
			# while(k<len(mark)-1 and  mark[k]!=0 and k<=cycle_pos + sigma):
			# 	k+=1
			# if(k>cycle_pos+sigma):
			# 	k=cycle_pos-1
			# 	while(k>0 and mark[k]!=0 and k>= cycle_pos-sigma):
			# 		k-=1
			# 	if(k<cycle_pos-sigma or k == 0):
			for l in range(1,len(next_bw)):
				if(mark[l] == 0 and l!= cycle_pos):
					if(next_bw[l]!=l-1 and next_bw[l-1]!=l):
						temp3 = next_bw[l-1]
						next_bw[l-1] = next_bw[l]
						next_bw[l] = temp3
						reset=1
						break
					elif(next_bw[l]!=l+1 and next_bw[l+1]!=l):
						temp3 = next_bw[l+1]
						next_bw[l+1] = next_bw[l]
						next_bw[l] = temp3
						reset=1
						break
			# temp3= next_bw[cycle_pos]
			# next_bw[cycle_pos]=next_bw[k]
			# next_bw[k]=temp3
		mark[cycle_pos]=1
		cycle_pos=next_bw[cycle_pos]
		j+=1
	# print(next_bw)
	# inverse bwt (string)
	ibwt = [0 for j in range(len(next_bw))]
	ibwt[-1]=1
	j=1
	k = len(next_bw)-2
	while next_bw[j]!=1:
		ibwt[k] = next_bw[j]
		j = next_bw[j]
		k-=1
	# print(i_c_copy)
	# print(ibwt)
	f=0
	for j in range(1,len(next_bw)):
		f=0
		for k in range(sigma+1):
			if(ibwt[j]<i_c[k]):
				f=1
			if f==1:
				break
		ibwt[j] = k-1
		if f == 0:
			ibwt[j] = sigma
		
	# print(ibwt)
	ibwt.pop(0)
	# print(ibwt)
	character.append(ibwt)
	print(len(ibwt),cal_mtf(sigma,ibwt))
	
	# print(bw,next_bw)


# for i in range(len(character)-1940):
# 	character[i] = bwt(character[i])
# 	count = [0 for j in range(sigma+1)]
# 	print(character[i])
# 	for j in range(len(character[i])):
# 		count[character[i][j]]+=1
# 	print(count)

