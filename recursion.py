# демонстрация работы рекурсивной функции

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

print(sum(10))

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    
print(fact(5))

def count(arr):
    if not arr:
        return 0
    else:
        return 1 + count(arr[1:])

numbers = [i for i in range(8)]    
print(count(numbers))
