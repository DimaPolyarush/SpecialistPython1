# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

first_number = int(input("n1= "))
second_number = int(input("n2= "))
numbers = []
if first_number > second_number:
    first_number, second_number = second_number, first_number

i = first_number
while i < second_number:
    if i % 3 == 0 and i != 0:
        numbers.append(i)
    i += 1
print(numbers)
