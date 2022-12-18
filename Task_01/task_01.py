# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

userNumber = float(input('Enter a Number: '))
text = str(userNumber)
sum = 0
index = 0
for i in text:
    if text[index] != '.':
        sum += int(text[index])
    index += 1
print(f'Sum of digits = {sum}')