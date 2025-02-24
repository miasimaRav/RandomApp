import random

def generateRandomList(num_elements):
    return [random.randint(5, 1100) for i in range(num_elements)]

random_list = generateRandomList(21)
