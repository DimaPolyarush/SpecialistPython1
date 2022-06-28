# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome(number):
    return str(number) == str(number)[::-1]


a = int(input("a= "))
b = int(input("b= "))
if a > b:
    a, b = b, a
n_pal = 0
for number in range(a, b + 1):
    if palindrome(number):
        n_pal += 1

print(n_pal)
