# example of sortingBubble
# algorithm O(n*2)

import random

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# создаём список вещественных чисел
numbers = [random.randint(0, 100) for i in range(0, 15)]
print(f"Несортированный список \n  {numbers}")
