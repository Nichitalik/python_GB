input = input('Введите строку: ').lower()


input = input.split(' ')

def Check_Vow(string):
    vowels = "аеёиоуыэюя"
    final = [each for each in string if each in vowels]
    return (len(final))
     

count = 1
for i in range(1, len(input)):
    if Check_Vow(input[i]) == Check_Vow(input[i - 1]):
        count += 1
    else:
        break
    
        
if count == len(input):
    print('Парам пам-пам')
else:
    print('Пам парам')
