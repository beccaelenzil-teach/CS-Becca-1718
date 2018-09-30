import matplotlib.pyplot as plt
from random import shuffle
import time
import numpy as np

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.pause(0.1)
    plt.draw()

def bubble_sort(some_list):
    t0 = time.time()
    n = 0
    sort = True
    while sort == True:
        sort = False
        for i in range(len(some_list)-1):
            n+=1
            if some_list[i+1] < some_list[i]:
                some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
                sort = True
                #display(some_list)

    total_time =  time.time() - t0

    return [n,total_time]
    #return some_list

def selection_sort(some_list):
    t0 = time.time()
    n= 0
    smallest_index = 0
    for k in range(1,len(some_list)):
        for i in range(k,len(some_list)):
            n += 1
            if some_list[i] < some_list[smallest_index]:
                smallest_index = i
        some_list[k-1], some_list[smallest_index] = some_list[smallest_index], some_list[k-1]

        smallest_index = k
    #print(some_list)
    total_time =  time.time() - t0
    return [n,total_time]


def insertion_sort(some_list):
    t0 = time.time()
    n = 0
    for k in range(1,len(some_list)):
        for i in range(0,len(some_list)):
            n = n+1
            if some_list[k] < some_list[i]:
                some_list[i], some_list[k] = some_list[k], some_list[i]

            #print(some_list)
    total_time =  time.time() - t0
    return [n,total_time]

def quick_sort(some_list, start, stop):
    print(start, stop)
    if stop-start < 1:
        return some_list
    else:
        #pivot = np.median([some_list[0], some_list[len(some_list)//2], some_list[-1]])
        pivot = some_list[start]
        left = start
        right = stop
        while left <= right:
            print(left,right)
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1

            if left <= right:
                some_list[left], some_list[right] = some_list[right], some_list[left]
                left += 1
                right -= 1

                print('So the list becomes:')
                print(some_list)
                display(some_list)

            quick_sort(some_list, start, right)
            quick_sort(some_list, left, stop)

my_list = [39, 30, 45, 33, 20, 61, 36, 5, 31, 64]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)





#some_list = create_random_list(1000)
#t2 = bubble_sort(some_list)
#t1 = insertion_sort(some_list)
#t3 = selection_sort(some_list)
#print("bubble: ",t2)
#print("insertion: ",t1)
#print("selection: ",t3)
