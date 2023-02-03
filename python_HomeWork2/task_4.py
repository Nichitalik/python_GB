N = int(input('введите число: '))

if N >= 2:
    l = [0]
    while(True):
        if 2 ** (l[-1] +  1) <= N:
            l.append(l[-1] + 1)
        else:
            break
    print(l)
else:
    print('нет подходящих степеней')