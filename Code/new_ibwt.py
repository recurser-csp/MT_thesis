import matplotlib.pyplot as plt
n = 5
k=1
failed = []
passed = []
num = 0
while k < 50:
	k+=1
	num+=1
	flag = 1
	n+=1
	sigma = 4
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
	if (len(s)-1)%(sigma-1) == 0:
		s[-1],s[-2] = s[-2],s[-1]

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
		# print(bwt_string)
		x = bwt_string[0]
		cycle_length = 1
		while x!=0:
			x = bwt_string[x]
			cycle_length+=1 
		if cycle_length == n:
			flag = 0
			# print("success",len(bwt_string)-1)
			passed.append(len(bwt_string)-1)
			# print(bwt_string)
			# print(s)
			break
	if flag == 1:
		# print(temp)
		# print("Failed",len(bwt_string)-1)
		failed.append(len(bwt_string)-1)
		# print(s)
		# print(bwt_string)
print("Failed : ",failed)
print("passed : ",passed)

print(len(failed)/(len(failed)+len(passed)))
print(len(passed)/(len(failed)+len(passed)))


	