# f = open('3_15_5000.txt','r')
f = open('../Data/7_cc0_cycles.txt','r')
g = open('../Data/7_cc1_cycles.txt','r')
h = open('../Data/7_cc_cycles.txt','r')

points = 2000
import matplotlib.pyplot as plt
# f = open('temp.txt','r')
x = []
y = []
x1 = []
y1 = []
x2 = []
y2 = []
for i in f:
	x.append(int(i.split(',')[1]))
	# f[i] = f[i].split(',')
	y.append(int(i.split(',')[2][:-1]))

	# print(f[i])
for i in g:
	x1.append(int(i.split(',')[1]))
	# f[i] = f[i].split(',')
	y1.append(int(i.split(',')[2][:-1]))
for i in h:
	x2.append(int(i.split(',')[1]))
	# f[i] = f[i].split(',')
	y2.append(int(i.split(',')[2][:-1]))
# prit(x,y)
x = x[:points]
y = y[:points]
x1 = x1[:points]
y1 = y1[:points]
x2 = x2[:points]
y2 = y2[:points]
plt.plot(x, y, linewidth = 0.5, color = 'black', marker='o', markerfacecolor='white', markersize=2,label = 'With Self Loops')
plt.plot(x1, y1, linewidth = 0.5, color = 'green', marker='o', markerfacecolor='white', markersize=2,label = 'After Removing Self Loops')
plt.plot(x2, y2, linewidth = 0.5, color = 'red', marker='o', markerfacecolor='white', markersize=2,label = 'After Completion of Algorithm')

# naming the x axis 
plt.xlabel('Length of String')
# naming the y axis 
plt.ylabel('Number of Cycles including Self loops')
plt.legend(loc = 'upper left')
  
# giving a title to my graph 
plt.title('Variation on Numbers of Cycles for Σ = 7')
# function to show the plot 
plt.show()