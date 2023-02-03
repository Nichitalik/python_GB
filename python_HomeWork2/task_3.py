X = int(input('Петя загад лисло X: '))
Y = int(input('Петя загад лисло Y: '))

if X <= 1000 and Y <= 1000:
    S = X + Y
    P = X * Y
    
    for i in range(S):
        i+=1
        if S - i == P / i:
            predict_X = i
            predict_Y = S - i

    print(predict_X, predict_Y)