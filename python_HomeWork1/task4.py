# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("введите число n: "))
m = int(input("введите число m: "))
k = int(input("введите число k: "))

if k <= (n * m):
    if k % n == 0:
        print('yes')
    elif k % m == 0:
        print('yes')
    else:
        print('no')
else:
    print('требуемое кол-во плиток больше размера шоколадки')
