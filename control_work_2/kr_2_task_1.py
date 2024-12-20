"""
Сформируйте одномерный массив из отрицательных элементов матрицы 'a' размером 5 на 7.
"""
import random

# матрица 5х7
row, col = 5, 7
arr = [[random.randint(-10, 20) for _ in range(col)] for _ in range(row)]

ngtv_arr = []

# добавляем отрицательные элементы в одномерный массив
for i in arr:
    for el in i:
        if el < 0:
            ngtv_arr.append(el)

print("Исходная матрица >>")
for i in arr:
    print(i)

print("Отрицательные элементы >>", ngtv_arr)