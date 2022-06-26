# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random

numbers = []
n = int(input("Введите количество чисел: "))
i = 0

while i <= n - 1:
    numbers.append(random.randint(-100, 100))
    print(numbers[i])
    i += 1

sum_p = 0
count = 0
while count < len(numbers):
    if numbers[count] > 0 and numbers[count] % 2 == 0:
        sum_p += numbers[count]
    count += 1

print("Сумма: ", sum_p)
