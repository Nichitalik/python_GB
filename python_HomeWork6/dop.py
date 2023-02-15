def friend(a):
    d = []
    for i in range(1, a):
        if a%i == 0:
            d.append(i)
    return sum(d)

            
k = int(input('введите число k: '))

r = []

for i in range(1,k+1):
    n = friend(i)
    if i == friend(n) and i != n:
        r.append(i)
    
print(r)
