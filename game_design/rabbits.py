import matplotlib.pyplot as plt

import time
rabbit_list = []
rabbits = 180
n = 1000
for i in range(n):
    #print(rabbits)
    rabbits = 0.008*rabbits*(200-rabbits)
    rabbit_list.append(rabbits)
    time.sleep(0.1)

print(rabbit_list)
plt.scatter(range(n),rabbit_list)
plt.show()
