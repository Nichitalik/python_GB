a1 = int(input('введите первый элемент: '))
d = int(input('введите разность: '))
n = int(input('введите  кол-во элементов: '))

l = []
for i in range(n):
    l.append(a1 + (i) * d)
print(l)