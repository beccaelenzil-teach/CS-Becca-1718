import random

def create_random_list(length):
    some_list = [i for i in range(length)]
    random.shuffle(some_list)
    return some_list
