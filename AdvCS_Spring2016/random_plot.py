import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

#
y = [i for i in range(100)]
x = [i for i in range(len(y))]

plt.ion()

for i in range(50):       ## Do the following 50 times
    print i
    plt.clf()             ## Clear the plot
    plt.bar(x,y)          ## Plot a bar chart
    plt.pause(0.01)            ## Pause for 1/2 a second
    shuffle(y)            ## Shuffle the data

plt.show()
