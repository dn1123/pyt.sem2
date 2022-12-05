number = int(input('Введите число '))

f = 1
for i in range(number):
    i = i + 1
    f = i * f

    print(f, end=" ")
    