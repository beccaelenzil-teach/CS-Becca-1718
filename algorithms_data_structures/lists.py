numbers = [i for i in range(10)]
print(numbers)

y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

import matplotlib.pyplot as plt

plt.bar(x,y)
plt.show()
