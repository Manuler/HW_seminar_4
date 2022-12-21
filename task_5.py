# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

with open('poly_1.txt', 'w') as file:
    file.write('4*x^3 + 7*x^2')
with open('poly_2.txt', 'w') as file:
    file.write('15*x^5 + 7*x^4')

with open('poly_1.txt', 'r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt', 'r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')