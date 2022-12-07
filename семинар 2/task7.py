# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input("Введите число: "))
def factorial (num):
    if num == 1: 
        return num
    else: 
        return num * factorial(num - 1)
f = factorial(n)
print(f"Факториал числа {n} -> {f}")   