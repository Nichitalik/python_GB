n = int(input('размер первого: '))
m = int(input('размер второго: '))

print("первый список:")
N = {int(input('\tвведите {} элемент: '.format(i))) for i in range(1, n + 1)}
print("второй список:")
M = {int(input('\tвведите {} элемент: '.format(i))) for i in range(1, m + 1)}

print(N.intersection(M))