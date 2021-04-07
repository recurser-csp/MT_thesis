n=int(input())
sigma = int(input())
position = [-1 for i in range(n)]
for i in range(1,sigma+1):
	position[i-1] = sigma+1-i


k=sigma
for i in range(sigma+1,n+1):
	if k == 0:
		k=sigma
	position[i-1] = k
	k-=1
print(position)

# algorithm 4.2.1 ended here and starting algorithm 4.4.2

#4.2.2  Starts

count = [-1 for i in range(sigma)] # initializing array
C1 = int((n-1)/sigma)
C2 = (n-1)%sigma
T1 = 1
count[0] = 0
# count[1] = 2
if C2 == 0:
	for i in range(1,sigma):
		count[i] = C1*(i)
		# print(i)
else:
	for i in range(1,sigma-C2+1):
		count[i] = C1*(i)
		# print(i)
	if C2>0:
		for i in range(sigma-C2,sigma):
			count[i] = C1*(i)+T1
			T1+=1
			# print(i,T1)
print(count)

#4.2.2  ends


#4.2.3 starts

char_arr = [0 for i in range(n)]
count_copy = list(count)

last_pos = position[n-1]
count_last_pos = count[last_pos-1]
# print(last_pos,count_last_pos)
for i in range(1,n+1):
	char_arr[i-1] = count_copy[position[i-1]-1]
	count_copy[position[i-1]-1] +=1
	if i-1 == char_arr[i-1]:
		# print("entered if case")
		# print(i,char_arr[i-1])
		if i<n:
			# print("before swapping char array")
			# print(char_arr)
			# print(position)
			char_arr[i-1],char_arr[i-2] = char_arr[i-2],char_arr[i-1]
			position[i-1],position[i-2] = position[i-2],position[i-1]
			# print("after swapping char array")
			# print(char_arr)
			# print(position)			
			for j in range(i+1,n+1):
				if position[j-2] == position[i-1] and position[j-1] == position[i-2]:
					position[j-2],position[j-1] = position[j-1],position[j-2]
		elif i == n:
			# print(char_arr)
			# print(" i == n")
			char_arr[i-1] = count_last_pos
			for j in range(1,n):
				if char_arr[j-1] >= count_last_pos:
					# print("entered inner if")
					char_arr[j-1] +=1
print("char_arr")
print(char_arr)
print("position")
print(position)



#4.2.3 ends

#4.2.4 starts

# mark = [0 for i in range(n)]
# cycle_length = 1
# cycle_pos = 1
# found = -1
# for i in range(1,n+1):
# 	if char_arr[cycle_pos] == 1 and i<n:
# 		for j in range(cycle_pos,sigma):
# 			if mark[j] == 0

#4.2.4 ends


