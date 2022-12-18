# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

userNumber = int(input('Enter a number N: '))

def factorial (x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

list = []

for i in range(userNumber):    
    list.append(factorial(i+1))

print(list)

