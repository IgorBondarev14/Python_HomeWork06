# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint

N = int(input("Введите размер списка: "))
array = [randint(0, 10) for array in range(N)]
print("Список из нескольких случайных чисел - ", array)

new_array = [array[i] for i in range(0, N, 2)]
print("Сумма элементов стоящих на нечетных позициях - ", sum(new_array))
