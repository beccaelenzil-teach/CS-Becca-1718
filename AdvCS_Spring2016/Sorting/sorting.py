__author__ = 'becca.elenzil'


import matplotlib.pyplot as plt
from random import shuffle
from time import *


plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.pause(0.01)
    plt.show()

def bubbleSort(some_list):
    sorted = False
    k = len(some_list)-1
    n = 0
    while not sorted:
        sorted = True
        for i in range(k):
            if some_list[i] > some_list[i+1]:
                n+=1
                some_list[i+1], some_list[i] = some_list[i], some_list[i+1]
                sorted = False
        k -= 1
    return n


def insertionSort(some_list):
    start = clock()
    for i in range(1,len(some_list)):
        for k in range(i,0,-1):
            if some_list[k] < some_list[k - 1]:
                some_list[k-1], some_list[k] = some_list[k], some_list[k-1]
                #display(some_list)
        #plt.show()
    end = clock()
    print "insertion sort time: ", end-start
    return some_list

def selectionSort(some_list):
    display(some_list)
    plt.pause(1)
    for k in range(len(some_list)):
        #initialize the smallest index
        smallest_index = k
        smallest_val = some_list[smallest_index]

        #loop through the list, cutting off one more from the front each time)
        for i in range(k+1,len(some_list)):
            if some_list[i] < smallest_val:
                smallest_index = i
                smallest_val = some_list[i]

        #put smallest value in right place using switch
        some_list[smallest_index], some_list[k] = some_list[k], some_list[smallest_index]

        #put smallest value in right place using insert
        #some_list = some_list[0:k] + [some_list[smallest_index]] + some_list[k:smallest_index] + some_list[(smallest_index+1):]

        display(some_list)
    plt.show()
    plt.pause(10)


        #some_list = some_list[0:k] + [smallest_val] + some_list[k:smallest_index] + some_list[(smallest_index+1):]


    return some_list

def quickSort(some_list, start, stop):
    if stop - start < 1:
        return some_list
    else:
        print "start: ",start, "stop:", stop
        pivot = some_list[start]
        print "pivot:", pivot
        print some_list
        left = start
        right = stop
        while left <= right:
            while some_list[left] < pivot:
                left += 1
            while some_list[right] > pivot:
                right -= 1
            if left <= right:
                some_list[left], some_list[right] = some_list[right],some_list[left]
                left += 1
                right -= 1
                print some_list

        quickSort(some_list, start, right)
        quickSort(some_list, left, stop)

    return some_list

def mergeSort(some_list):
    if len(some_list) > 1:
        split = len(some_list)/2

        list_a = some_list[0:split]
        list_b = some_list[split:]

        mergeSort(list_a)
        mergeSort(list_b)

        i=0
        j=0
        k=0
        while i < len(list_a) and j < len(list_b):
            if list_a[i] < list_b[j]:
                some_list[k]=list_a[i]
                i += 1
            else:
                some_list[k]=list_b[j]
                j += 1
            k += 1

        while i < len(list_a):
            some_list[k]=list_a[i]
            i += 1
            k += 1

        while j < len(list_b):
            some_list[k]=list_b[j]
            j += 1
            k += 1

    print "Merging ",some_list

a = create_random_list(20)
a = quickSort(a, 0, len(a)-1)


"""

num_iter = []
for i in range(100):
    print i
    n = bubbleSort(create_random_list(100))
    num_iter.append(n)

ave_iter = sum(num_iter)/len(num_iter)
print ave_iter

#print a
#print a
#bubbleList = bubbleSort(a)
#print bubbleList
#insertList = insertionSort(a)
#print insertList
#selectList = selectionSort(a)
#print selectList


some_list = [2,1,5]
display(some_list)
sleep(1)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
sleep(1)
some_list[1], some_list[2] = some_list[2], some_list[1]
display(some_list)
sleep(1)
some_list[0], some_list[1] = some_list[1], some_list[0]
display(some_list)
sleep(10)
"""

