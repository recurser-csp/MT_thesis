import matplotlib.pyplot as plt
import numpy as np
visit_count = 0
def loop_check(arr,previous_arr,location):
	global visit_count
	temp_arr = previous_arr.copy()
	t = temp_arr[-1]
	while t!=location and len(temp_arr)<=len(arr):
		if t<location:
			temp_arr.append(arr[t])
			t = arr[t]
			visit_count+=1
			continue
		else:
			temp_arr.append(arr[t-1])
			visit_count+=1
			t = arr[t-1]
	# print(temp_arr)
	if len(temp_arr) == len(arr)+1:
		return 1
	else:
		return 0

def bar(l,h,arr,previous_arr):
	global visit_count
	left = 0
	right = 0
	prev_arr = previous_arr.copy()
	t = prev_arr[-1]
	# print(l,h,arr)
	if l == h:
		return(loop_check(arr,prev_arr,l))
	while t<l or t>h:
		# print(t)
		if t<l:
			prev_arr.append(arr[t])
			t = prev_arr[-1]
			visit_count+=1
			continue
		if t>h:
			prev_arr.append(arr[t-1])
			t = prev_arr[-1]
			visit_count+=1
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

n = 14
k=1
failed = []
passed = []

lengths = []
visits = []
squares = []
nlogn = []
brute_force = []
num = 0
while k < 2000:
	# print(k)
	visit_count = 0
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

	count_copy=[0]
	for i in range(1,sigma):
		count_copy.append(count_copy[-1]+count[i-1])
	mx_length = 0
	mx_length_string = []
	temp = s.copy()
	rank = s.copy()
	c=count_copy.copy()
	low = len(rank)
	high = 1
	for j in range(len(rank)):
		x= rank[j]
		rank[j] = c[x]
		c[x]+=1
		if j>=1:
			if rank[j] == j:
				conflict_count+=1
				low = min(j,low)
			if rank[j] ==j+1:
				conflict_count+=1
				high = j+1


	# low = len(rank)
	# high = 0
	# for i in range(1,len(rank)):
	# 	if rank[i] == i:
	# 		conflict_count+=1
	# 		low = min(i,low)
	# 	if rank[i] ==i+1:
	# 		conflict_count+=1
	# 		high = i+1
	# print(high,low,conflict_count, len(rank))
	# visit_count = 0
	# for i in range(1,len(rank)+1):
	# 	loop_check(rank,[0],i)
	# brute_force.append(visit_count/len(rank))
	visit_count = 0
	if low<high:
		# print("invalid")
		# failed.append(len(rank))
		length = len(rank)
		lengths.append(len(rank))
		visits.append(visit_count/length)
		# squares.append(k*k)
		# t = np.sqrt(k)
		t = np.log2(length)
		nlogn.append(50*t)
		continue
	if bar(high,low,rank,[0]) == 1:
		# print("passed")
		passed.append(len(rank))
	else:
		failed.append(len(rank))
	length = len(rank)
	lengths.append(len(rank))
	visits.append(visit_count/length)
	# squares.append(k*k)
	t = np.log2(length)
	nlogn.append(50*t)



plt.plot(lengths, visits,linewidth = 0.5, color = 'green', label = 'Implemented Algorithm')
# plt.plot(lengths, brute_force,linewidth = 0.5, color = 'black', label = 'Brute Force')
plt.plot(lengths, nlogn,linewidth = 0.5, color = 'black', label = '50*Log(n)')
plt.plot(lengths, lengths,linewidth = 0.5, color = 'red', label = 'n')
plt.xlabel('Length of String')
plt.ylabel('Average Number of access at each character')
plt.legend(loc = 'upper left')
plt.show()
	