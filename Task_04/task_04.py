# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
list_numbers = [i for i in range(-N, N+1)]
print(list_numbers)

file = open('file.txt', 'r')
a = file.readlines()
print(a)

for i in range(len(a)):
    a[i] = int(a[i].strip())
print(a)
product = 1
for i in range(len(a)):
    product*=list_numbers[a[i]]
print(product)
file.close()