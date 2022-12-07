# задача 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
#     Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141
from math import pi as PI
print(PI)
def my_round_float(num: float, d: float = 1):
    temp = (num/d)*10
    if temp%10 >= 5:
        return (int(temp/10)+1)*d
    else:
        return int(temp/10)*d
result = my_round_float(PI, 0.01)
print(result)
