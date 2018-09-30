import random
import math

def create_random_list(length):
    some_list = [i for i in range(length)]
    random.shuffle(some_list)
    return some_list


def sequential(some_list, target):
    for item in some_list:
        if item == target:
            return True
    return False

def binary_search(some_list, target):
    some_list.sort()
    print(some_list)
    center = round(len(some_list) / 2)
    print(center)
    while some_list[center] != target:
        if some_list[center] > target:
            center = math.ceil(len(some_list[0:center]) / 2)
        elif some_list[center] < target:
            center = center + math.ceil(len(some_list[(center+1):]) / 2)
        print(center)

    return center


some_list = create_random_list(21)
print(some_list)
(binary_search(some_list,20))
