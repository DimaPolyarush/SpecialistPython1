# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

n = int(input("кол-во коров: "))
if n >= 11 and n <= 14:
    print(n, 'коров')
else:
    rem = n % 10
    if rem == 0 or (rem >= 5 and rem <= 9):
        print(n, 'коров')
    if rem == 1:
        print(n, 'корова')
    if rem >= 2 and rem <= 4:
        print(n, 'коровы')
