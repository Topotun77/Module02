str_ = input("Введите строку для поиска испорченных слов: ")
list_str = str_.split()

list_no_star = []

for s in list_str:
    if s[0] != '*':
        list_no_star.append(s)

print('Список неиспорченных слов: ', list_no_star)