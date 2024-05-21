def convert(*list_):
    return list(map(int, list_))


list_str =  [1, 2, '3', '4', '5', 6]
print(f'Начальный список: {list_str}')
print(f'Список из целых чисел: {convert(*list_str)}')