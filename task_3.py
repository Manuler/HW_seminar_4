# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
#
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

ls = [1, 1, 2, 4, 5, 6, 7, 7, 8]
ls1 = []
for i in ls:
    if ls.count(i) == 1:
        ls1.append(i)

print(ls1)