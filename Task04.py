# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
import math
N = int(input("Введите число - "))
set = [math.factorial(i) for i in range(1, N + 1)]
print(set)


