import matplotlib.pyplot as plt
cycle_count = 0
def loop_check(arr,previous_arr,location):
	# previous_arr = temp_arr.copy()
	temp_arr = previous_arr.copy()
	t = temp_arr[-1]
	while t!=location and len(temp_arr)<=len(arr):
		if t<location:
			temp_arr.append(arr[t])
			t = arr[t]
			continue
		else:
			temp_arr.append(arr[t-1])
			t = arr[t-1]
	# print(temp_arr)
	if len(temp_arr) == len(arr)+1:
		return 1
	else:
		return 0

def bar(l,h,arr,previous_arr):
	left = 0
	right = 0
	prev_arr = previous_arr.copy()
	t = prev_arr[-1]
	# print(l,h,prev_arr)
	if l == h:
		return(loop_check(arr,prev_arr,l))
	while t<l or t>h:
		# print(t)
		if t<l:
			prev_arr.append(arr[t])
			t = prev_arr[-1]
			continue
		if t>h:
			prev_arr.append(arr[t-1])
			t = prev_arr[-1]
	# prev_arr.append(t)
	temp = prev_arr.copy()
	if t == l:
		return(bar(t+1,h,arr,temp))
	if t == h:
		return(bar(l,t-1,arr,temp))
	if t>l and t<h:
		left = bar(l,t-1,arr,temp)
		if left == 1:
			return 1
		return(bar(t+1,h,arr,temp))

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
			# print(mark)
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
	return bwt(ibwt)

n = 5
k=1
failed = []
passed = []
num = 0
while k < 20:
	k+=1
	num+=1
	flag = 1
	n+=1
	sigma = 4
	s = []
	t = sigma-1
	count = {0:1}
	conflict_count = 0
	for i in range(1,sigma):
		count[i] = 0
	for i in range(n-1):
		s.append(t)
		count[t]+=1
		t-=1
		if t==0:
			t = sigma-1
	# print(s)
	count_copy=[0]
	for i in range(1,sigma):
		count_copy.append(count_copy[-1]+count[i-1])
	mx_length = 0
	mx_length_string = []
	temp = s.copy()
	rank = s.copy()
	c=count_copy.copy()
	for j in range(len(rank)):
		x= rank[j]
		rank[j] = c[x]
		c[x]+=1

	low = len(rank)
	high = 0
	# print(rank)
	for i in range(1,len(rank)):
		if rank[i] == i:
			conflict_count+=1
			low = min(i,low)
		if rank[i] ==i+1:
			conflict_count+=1
			high = i+1
	# print(high,low,conflict_count, len(rank))
	for i in range(len(s)):
	# for i in range(high-1,low+1):
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
		# print(bwt_string,cycle_length)	
		if cycle_length>mx_length:
			# print("yes", cycle_length,bwt_string)
			mx_length = cycle_length
			mx_length_string = bwt_string.copy()
		if cycle_length == n:
			flag = 0
			# print(temp)
			# print(len(bwt_string),cal_mtf(sigma,temp),0)
			passed.append(len(bwt_string)-1)
			break

	if flag == 1:
		failed.append(len(s))
		# print(mx_length_string)
		# mx_length_string = merge(mx_length_string,count_copy)
		# print(mx_length_string)
			# print(len(mx_length_string),cal_mtf(sigma,mx_length_string),cycle_count)

print(passed)
print(failed)

	