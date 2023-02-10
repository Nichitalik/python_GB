n = int(input('Код-во кустов: '))
a = [int(input('\tвведите кол-во ягод на {} кусте: '.format(i))) for i in range(1, n + 1)]
a = [a[-1]] + a + [a[0]] # Замыкаю список как кольцо

x = 0
for i in range(1, n):
    if (a[i]+a[i+1]+a[i-1] > x):
        x = a[i]+a[i+1]+a[i-1]
print(x)