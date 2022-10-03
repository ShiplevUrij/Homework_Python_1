# 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print('Введите вещественное число')
a = input()
print(type(a))
summ_of_digits=0
for i in a: 
    if i.isdigit():
        summ_of_digits+= int(i)
print (f"Сумма цифр, введённого числа {a} равна {summ_of_digits}")       

# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial)

# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input('Введите число n ')) 
def sequence(n):
    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]          
print(sequence(n))
print(round(sum(sequence(n))))

# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint
def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list
n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)

# 5 Реализуйте алгоритм перемешивания списка.
size = int (input('Введите размер массива '))
import random
from random import randint
list=[randint(-10, 10) for i in range(size)]
print(list)
random.shuffle(list)
print('Перемешанный массив', list)