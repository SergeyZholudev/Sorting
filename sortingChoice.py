# example of sortingBubble
# algorithm O(n*2)

import random

def findSmallest(arr):
    """Функция выбора наименьшего элемента из списка"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def sortingChoice(arr):
    """Функция сортировки списка выбором. О(n2)"""
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# создаём список вещественных чисел
numbers = [random.randint(0, 100) for i in range(0, 15)]
print(f"Несортированный список \n  {numbers}")

# основное тело 
sortedArr = sortingChoice(numbers)
print(f"Сортированный массив \n  {sortedArr}")
