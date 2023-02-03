size = int(input('Введите кол-во арбузов: '))
arr =[]
for i in range(size):
    arr.append(int(input('Введите вес арбуза: ')))
print(min(arr), max(arr))