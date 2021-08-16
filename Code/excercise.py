import matplotlib.pyplot as plt
import numpy as np
# print(np.sqrt(17))

limit = 2000
s = []
n = []
nlgn = []
for i in range(limit):
	n.append(i)
	s.append(i*i)
	t = np.log2(i)
	nlgn.append(100*t*i)
plt.plot(n, s,linewidth = 0.5, color = 'black', label = 'Ideal')
plt.plot(n, nlgn,linewidth = 0.5, color = 'green', label = 'Ideal')
# plt.plot(lengths, nlogn,linewidth = 0.5, color = 'red', label = 'Ideal')
plt.show()