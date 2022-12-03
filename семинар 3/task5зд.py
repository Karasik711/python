# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

import random
k = random.randint(0, 10)
print(f'Список чисел негафибоначчи для числа {k}:')
fib = [0, 1]
for i in range(0, k - 1):
    fib.append(fib[i] + fib[i + 1])
for _ in range(0, k):
    fib.insert(0, (fib[1] - fib[0]))
print(fib)