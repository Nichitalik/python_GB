a = int(input("введите число: "))
b = int(input("введите степень: "))

def power(A, B):
    if B == 1:
        return  A
    elif B == 0:
        return 1
    else:
        return power(A * a, B - 1)

print(power(a,b))