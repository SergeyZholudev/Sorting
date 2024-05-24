# the algorithm of quick sorting

import random
import time

def qSort(arr) -> list:
    """Быстрая сортировка массива"""
    if len(arr) == 0:
        return arr
    else:
        pivot = arr[0]
        lessArr = [i for i in arr[1:] if i < pivot]
        greatArr = [i for i in arr[1:] if i > pivot]

    return qSort(lessArr) + [pivot] + qSort(greatArr)


# создаём список вещественных чисел
numbers = [random.randint(0, 100) for i in range(0, 110000)]
# print(f"Несортированный список \n  {numbers}")

start = time.time()
qSort(numbers)
end = time.time() - start

print(f"Время выполнения {end}")
