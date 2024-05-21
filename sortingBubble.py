# example of sortingBubble
# algorithm O(n*2)

import random


def sortingBubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# создаём список вещественных чисел
numbers = [random.randint(0, 100) for i in range(0, 15)]
print(f"Несортированный список \n  {numbers}")

# отправляем несортированный, получаем сортированный списки
sortedList = sortingBubble(numbers)
print(f"Сортированный список \n  {sortedList}")
