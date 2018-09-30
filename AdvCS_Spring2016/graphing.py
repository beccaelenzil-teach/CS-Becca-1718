__author__ = 'becca.elenzil'


import matplotlib.pyplot as plt


y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

plt.plot(x,y)
plt.scatter(x,y)
#plt.draw()
#plt.bar(x,y)
plt.show()