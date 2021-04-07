bwt="4301243"
sigma = 4
count = [1]*(sigma+1)
f = list(bwt)
for i in range(len(f)):
	f[i] = int(f[i])
f.sort()
print(f)
print(count)
bwt = list(bwt)
for i in range(len(bwt)):
	bwt[i] = int(bwt[i])
print(bwt)
for i in range(len(bwt)):
	t = bwt[i]
	bwt[i] = str(bwt[i])+"_"+str(count[bwt[i]])
	count[t]+=1
count = [1]*(sigma+1)	
print(bwt)
for i in range(len(bwt)):
	t = f[i]
	f[i] = str(f[i])+"_"+str(count[f[i]])
	count[t]+=1
print(f)
ibwt = ""
s = "0_1"
for i in range(len(bwt)):
	for j in range(len(bwt)):
		if f[j] == s:
			ibwt = s+","+ibwt
			s = bwt[j]
			break
print(ibwt)

