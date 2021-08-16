def loop_check(arr,previous_arr,location):
	# previous_arr = temp_arr.copy()
	temp_arr = previous_arr.copy()
	t = temp_arr[-1]
	while t!=location  len(temp_arr)<=len(arr):
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


	
def foo(l,h,arr):
	temp = arr.copy()
	arr.insert(h,-1)
	x = 0
	count = 1
	# print(l,h)
	if l == h:
		temp.insert(h,0)
		while temp[x]!=0 and count <=len(temp):
			x = temp[x]
			count+=1
		if count == len(temp):
			return h
		else:
			return 0
	while x < l or x > h:
		x = arr[x]
	# print(x)
	if x ==l:
		left = foo(l,x,temp)
	else:
		left = foo(l,x-1,temp)
	if left!=0:
		return left
	if x == h:
		right = foo(x,h,temp)	
	else:
		right = foo(x+1,h,temp)
	return right
rank = [8,4,1,9,5,2,10,6,3,11,7]
rank = [9,5,1,10,6,2,11,7,3,12,8,4]
rank = [4,2,1,5,3]
low = len(rank)
high = 1
conflict_count = 0
for i in range(1,len(rank)):
	if rank[i] == i:
		conflict_count+=1
		low = min(i,low)
	if rank[i] ==i+1:
		conflict_count+=1
		high = i+1
# print(high,low)
# print(foo(high,low,rank))
p_arr = [0]
print(bar(1,len(rank),rank,p_arr))

