"""
Объединить массивы A размером 7 и B размером 8, предварительно удалив максимальные
элементы этих массивов. Результат получить в массиве A. Удаление элемента массива
с заданным индексом осуществить в методе.
"""
import random

# массивы a и b
a = [random.randint(1, 100) for _ in range(7)]
b = [random.randint(1, 100) for _ in range(8)]
print("Массив А >>", a)
print("Массив В >>", b)

def max_ind(arr):
    mxin = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[mxin]:
            mxin = i
    return mxin

# Функция для удаления максимального элемента из массива по индексу
def remove_el(arr, index):
    arr.pop(index)

remove_el(a, max_ind(a))
remove_el(b, max_ind(b))

for i in range(len(b)):
    a.append(b[i])

print("\nМассив A (объединенный) после удалений максимальных элементов:", a)