f = open('../Data/10/ub_mtf','r')
g = open('../Data/10/algo','r')
h = open('../Data/10/random_mtf','r')
my = open('../Data/10/suffix_mtf','r')
my_pre = open('../Data/10/ext_mtf_2k','r')
import matplotlib.pyplot as plt
points = 2000
arr = []
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
xm = []
ym = []
xp = []
yp = []

for i in f:
	arr.append(i.split(' '))
# print(arr)
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	y.append(int(arr[i][0]))
	x.append(int(arr[i][1]))
# print(arr)
arr = []
for i in g:
	arr.append(i.split(' '))
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	y1.append(int(arr[i][0]))
	x1.append(int(arr[i][1]))
arr = []
for i in h:
	arr.append(i.split(' '))
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	y2.append(int(arr[i][0]))
	x2.append(int(arr[i][1]))
arr = []
for i in my:
	arr.append(i.split(' '))
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	ym.append(int(arr[i][0]))
	xm.append(int(arr[i][1]))
arr = []
for i in my_pre:
	arr.append(i.split(' '))
for i in range(len(arr)):
	arr[i][1] = arr[i][1][:-1]
	yp.append(int(arr[i][0]))
	xp.append(int(arr[i][1]))
# print(arr)
xm = xm[::-1]
ym = ym[::-1]
x = x[:points]
y = y[:points]
x1 = x1[:points]
y1 = y1[:points]
x2 = x2[:points]
y2 = y2[:points]
# xm = xm[:points]
# ym = ym[:points]
# xp = xp[:240]
# yp = yp[:240]
plt.plot(x, y, linewidth = 0.5, color = 'black', label = 'Ideal')
# plt.plot(x1, y1, linewidth = 0.5, color = 'orange' ,label = 'My_Algo MTF Value')
plt.plot(x2, y2, linewidth = 0.5, color = 'blue' ,label = 'Random MTF Value')
plt.plot(xm, ym, linewidth = 0.5, color = 'green' ,label = 'Removing Leading Character')
plt.plot(xp, yp, linewidth = 0.5, color = 'red' ,label = 'Brute Forcing for Adding single Character')

# naming the x axis 
plt.xlabel('Length of String')
# naming the y axis 
plt.ylabel('MTF Value')
plt.legend(loc = 'upper left')
  
# giving a title to my graph 
plt.title('Variation on Numbers of Cycles for Σ = 10')
# function to show the plot 
plt.show()
beta = 0.0
mx = 0
for i in range(len(y)):
	beta+=(yp[i]/y[i])
	if yp[i] == y[i]:
		print(x[i],y[i],xp[i])
	mx = max(mx,y[i]-yp[i])
beta = beta/(len(y))
print(beta)
print(mx)
