# one_point_en = ['A', "E", 'I', 'O', 'U', 'L', "N", 'S', 'T', 'R' ]
# two_point_en = ['D','G']
# three_point_en = ['B', 'C', 'M', 'P']
# four_point_en = ['F', 'H', 'V', 'W', 'Y']
# five_point_en = 'K'

leng = int(input('выберете язык \n1 - английский; 0 - русский: '))
word = (input('введите слово на выбранном языке: ')).upper()

point_en = {
    '1': ['A', "E", 'I', 'O', 'U', 'L', "N", 'S', 'T', 'R' ],
    '2': ['D','G'],
    '3': ['B', 'C', 'M', 'P'],
    '4': ['F', 'H', 'V', 'W', 'Y'],
    '5': ['K'],
    '8': ['J', 'X'],
    '10': ['Q', 'Z']
}

point_rus = {
    '1': ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', "Т"],
    '2': ['Д', 'К', 'Л', 'М', 'П', 'У'],
    '3': ['Б', 'Г', 'Ё', 'Ь', 'Я'],
    '4': ['Й', 'Ы'],
    '5': ['Ж', 'З', 'Х', 'Ц', 'Ч'],
    '8': ['Ш', 'Э', 'Ю'],
    '10': ['Ф', 'Щ', 'Ъ']
}

if leng == 0:
    now_dict = point_rus
else:
    now_dict = point_en
    
res = 0
for ch in word:
    for key in now_dict:
        if ch in now_dict[key]:
            res += int(key)
print(res)
