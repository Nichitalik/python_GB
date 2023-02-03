size = int(input('Введите кол-во монеток: '))
arr =[]
for i in range(size):
    arr.append(int(input('Введите сторону монетки(1 или 0): ')))
    if arr[-1] != 1 or arr[-1] != 0:
        print('введны невенный данные!')
        break
    
if sum(arr) < len(arr):
    print(len(arr) - sum(arr))
else:
    print(sum(arr) - len(arr))
