# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

numbers = [2, 5, -3, 1, 10]
sum_p = 0
count = 0
while count < len(numbers):
    if numbers[count] > 0:
        sum_p += numbers[count]
    count += 1

print(sum_p)
