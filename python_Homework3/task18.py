N = int(input('Введите размер списка: '))
A = []
for i in range(N):
    A.append(int(input('введите элемент списка: ')))
X = int(input('Введите X: '))

now_index = 0
result = 0

for el in A:
    if abs(X - el) < abs(X - result):
        result = el
        
print(result)
