N = int(input('Введите размер списка: '))
A = []
for i in range(N):
    A.append(int(input('введите элемент списка: ')))
X = int(input('Введите искомое число: '))
print(A.count(X))