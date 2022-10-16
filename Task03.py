# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

from random import randint
elements = [randint(1, 10) for x in range(int(input("Введите размер последовательности чисел: ")))]
print(elements)
Uniqe_elements = list(filter(lambda x: elements.count(x) == 1, elements))
print(Uniqe_elements)