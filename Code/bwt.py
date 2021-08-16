def bwt(s):
	s+='$'
	A = []
	st = ''
	for i in range(len(s)):
		# t = s[:]
		t = s[len(s)-i:]+s[:len(s)-i]
		# print(i,t)
		A.append(t)
	A_ = sorted(A)
	# st = ''
	for i in range(len(A_)):
		# print(A_[i])
		st+=A_[i][-1]
	return st

S = 'abaccbc'
S_ = bwt(S)
print("\nBWT("+S+"$) : "+S_)
# c = "423$143"
# for i in range(1,5):
# 	print("inserting "+str(i))
# 	for j in range(len(S)+1):
# 		t = S
# 		t = t[:j]+str(i)+t[j:]
# 		# print(t)
# 		t_ = bwt(t)
# 		print(t_)
# 		if(t_[:-1] == c):
# 			print(t_)