# Задача 1 Напишите программу, 
# удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Я кракодил кракожу и буду кракодить тряттрявуабв ауеабв'
x = list(filter(lambda s: 'абв' not in s ,my_str.split()))
print(" ".join(x))
exit()
with open("test.txt", 'r') as data:
    my_list = list(map(int, data.read().split()))
    print(my_list)
find_ = []
for i in range(1, len(my_list)):
    if my_list[i] - 1 != my_list[i - 1]:
        d = my_list[i] - my_list[i - 1]
        for j in range(d-1):
            temp = my_list[i - 1] + j
            find_.append(temp + 1)
print(find_)