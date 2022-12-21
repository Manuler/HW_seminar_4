# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)*
# многочлена и записать в файл многочлен степени k.
#
#     *Пример:*
#
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0


import random

k = int(input('Введите число k = '))
ratio = [random.randint(-100, 100) for i in range(0, k+1)]
print(ratio)

def Polynom(k, ratio):
    pol = ''
    for i in range(0, k+1):
        if k - i > 1 and ratio[i] != 0:
            pol += f'{ratio[i]}*x^{k-i} + '
        elif k - i == 1 and ratio[i] != 0:
            pol += f'{ratio[i]}*x + '
        elif ratio[i] == 0:
            pol += ''
        else:
            pol += f'{ratio[i]} = 0'
    return pol

with open('pol.twt', 'w') as data:
    data.write(Polynom(k, ratio).replace('+ -', '- '))