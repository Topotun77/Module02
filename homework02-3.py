def print_params(text='Привет!'):
    print(text*2)


print_params()
print_params('Это вротой вызов функции.')
print_params('А это третий вызов.')

# Здесь заканчивается домашняя работа и начинается тест передачи параметров в функцию
# Последние 2 строчки не работают и я не понимаю как заставить их работать?

print(f'\n{'='*60}\n')


def step(x):
    if not(type(x) is dict or type(x) is set):
        return x*2
    else:
        print(f'{type(x)} - Не могу умножить на 2. А когда я изучу исключения, то может выясню какие еще типы '
              f'я не умею умножать.')
        return type(x)


def test_(*args):
    # print(type(args))
    print(args)
    print(list(args))
    print(list(map(str, args)))
    print(step(args))
    print(list(map(step, args)))
    print()


test_()
test_('Qwerty')
test_(*'Qwerty')
test_(1, 2, 5)

test_({10, 20, 30})

list_ = [34, True, "Йцукен"]
test_(list_)
test_(*list_)

dict_ = {3: 12,
         'str1': "Пароль",
         'list1': [1, 2, 3]}
test_(dict_)
test_(*dict_)
print(*dict_)

# test_(**dict_)    # А вот эта строчка и следующая у меня не работают
# print(**dict_)

# Вот так будет работать:

def test_2(str1, list1):
    print(f'str1 = {str1}, list1 = {list1}')

def test_3(**kwargs):  # только пока не понятно, как это может быть использовано, если можно просто
    print(kwargs)      # сразу передавать словарь, а не распаковывать, а потом снова запаковывать его

del dict_[3]
test_2(**dict_)

dict_['3'] = 'три'
test_3(**dict_)
