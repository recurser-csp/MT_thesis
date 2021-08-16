import matplotlib.pyplot as plt
cycle_count = 0
def cal_mtf(sigma,ch):
	temp = 0    # initial MTF value
	chars = []
	for m in range(sigma):
		chars.append(m)
	for k in range(len(ch)):
		for j in range(len(chars)):
			if chars[j] == ch[k]:
				temp = temp+1+j
				break
		t_1 = chars.pop(j)
		chars.insert(0,t_1)     #move_to_front
	return temp
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
def merge(next_bw,i_c):
	global cycle_count
	# print(next_bw)
	mark = [0 for j in range(len(next_bw))]
	cycle_pos = 0
	flag_1=0
	j=1
	reset = 0
	cycle_count = 0
	while j<len(next_bw):
		if reset == 1:
			j=1
			mark = [0 for m in range(len(next_bw))]
			cycle_pos=0
			reset=0
			flag_1=0
		if(next_bw[cycle_pos]==0 and j<len(next_bw)):
			for l in range(1,len(next_bw)):
				if(mark[l] == 0 and l!= cycle_pos):
					if(next_bw[l]!=l-1 and next_bw[l-1]!=l):
						temp3 = next_bw[l-1]
						next_bw[l-1] = next_bw[l]
						next_bw[l] = temp3
						reset=1
						cycle_count+=1
						break
					elif(next_bw[l]!=l+1 and next_bw[l+1]!=l):
						temp3 = next_bw[l+1]
						next_bw[l+1] = next_bw[l]
						next_bw[l] = temp3
						reset=1
						cycle_count+=1
						break
		mark[cycle_pos]=1
		cycle_pos=next_bw[cycle_pos]
		j+=1
	# print(next_bw)
# test
	check = next_bw.copy()
	f=0
	for j in range(len(check)):
		f=0
		for k in range(sigma):
			if(check[j]<i_c[k]):
				f=1
			if f==1:
				break
		check[j] = k-1
		if f == 0:
			check[j] = sigma-1
	# print(check)
# test
	ibwt = [0]
	x = next_bw[0]
	while x!=0:
		ibwt.insert(0,x)
		x = next_bw[x]
	# print(ibwt)
	f=0
	for j in range(len(ibwt)):
		f=0
		for k in range(sigma):
			if(ibwt[j]<i_c[k]):
				f=1
			if f==1:
				break
		ibwt[j] = k-1
		if f == 0:
			ibwt[j] = sigma-1
	x = bwt(ibwt)
	if x != check:
		print("GALAT!!!")
	return x

n = 50
k=1
failed = []
passed = []
num = 0
while k < 1000:
	k+=1
	num+=1
	flag = 1
	n+=1
	sigma = 12
	s = []
	t = sigma-1
	count = {0:1}
	for i in range(1,sigma):
		count[i] = 0
	for i in range(n-1):
		s.append(t)
		count[t]+=1
		t-=1
		if t==0:
			t = sigma-1
	# print(s)s
	count_copy=[0]
	for i in range(1,sigma):
		count_copy.append(count_copy[-1]+count[i-1])
	# print(count_copy)
	# if (len(s)-1)%(sigma-1) == 0:
	# 	s[-1],s[-2] = s[-2],s[-1]
	mx_length = 0
	mx_length_string = []

	for i in range(len(s)):
		temp = s.copy()
		temp.insert(i+1,0)
		# print(temp)
		bwt_string = temp.copy()
		c = count_copy.copy()
		for j in range(len(temp)):
			x = temp[j]
			bwt_string[j] = c[x]
			c[x]+=1
		x = bwt_string[0]
		cycle_length = 1
		while x!=0:
			x = bwt_string[x]
			cycle_length+=1
		if cycle_length>mx_length:
			# print("yes", cycle_length,bwt_string)
			mx_length = cycle_length
			mx_length_string = bwt_string.copy()
		if cycle_length == n:
			flag = 0
			# print(temp)
			# print(len(bwt_string),cal_mtf(sigma,temp),0)
			# passed.append(len(bwt_string)-1)
			break
	if flag == 1:
		# print(mx_length_string)
		mx_length_string = merge(mx_length_string,count_copy)
		# print(mx_length_string)
		# print(temp)
		# print(len(mx_length_string),cal_mtf(sigma,mx_length_string),cycle_count)



	