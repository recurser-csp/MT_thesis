f = open('../Data/26/ub_mtf','r')
my_pre = open('../Data/26/new_mtf_swaps','r')

import matplotlib.pyplot as plt
points = 1000
arr = []
x = []
y = []
xp = []
yp = []
swaps = []
for i in f:
	arr.append(i.split(' '))
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	y.append(int(arr[i][0]))
	x.append(int(arr[i][1]))
arr = []
for i in my_pre:
	arr.append(i.split(' '))
print(arr)
for i in range(len(arr)):
	print(i)
	arr[i][2] = arr[i][2][:-1]
	yp.append(int(arr[i][0]))
	xp.append(int(arr[i][1]))
	swaps.append(int(arr[i][2]))
x = x[:points]
y = y[:points]

# fig,ax = plt.subplots(2	)
plt.plot(x, y,linewidth = 0.5, color = 'blue', label = 'Maximum MTF possible for any string')
plt.plot(yp, xp,linewidth = 1.0, color = 'orange' ,label = 'MTF value of the string given by algorithm')
# ax[1].plot(yp,swaps,linewidth = 0.5, color = 'green' ,label = 'Number of swaps'	)
# plt.plot(x, y, linewidth = 0.5, color = 'black', label = 'Ideal')
# plt.plot(yp, xp, linewidth = 0.5, color = 'red' ,label = '$ insertion')
# plt.plot(yp,swaps, linewidth = 0.5, color = 'green' ,label = 'Number of swaps')


plt.xlabel('Length of String')
plt.ylabel('MTF Value')
plt.legend(loc = 'upper left')
# ax[1].set_ylabel('Number of Swaps')
# ax[1].set_xlabel('Length of String')

  
# # giving a title to my graph 
plt.title('Variation on MTF for Σ = 7')
# # function to show the plot 
plt.show()
beta = 0.0
mx = 0
print(x[0],y[0],x[-1],y[-1])
print(xp[0],yp[0],xp[-1],yp[-1])
for i in range(len(y)):
	beta+=(xp[i]/y[i])
	# if yp[i] == y[i]:
	# 	print(x[i],y[i],xp[i])
	mx = max(mx,y[i]-xp[i])
beta = beta/(len(y))
print(beta)
print(mx)
print(max(swaps))
