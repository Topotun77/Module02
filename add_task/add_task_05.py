def evklid(a, b):
    if a > b:
        a, b = b, a
    new_a = b % a
    if new_a == 0:
        return a
    else:
        return(evklid(new_a, a))


list_ = [[5, 7], [21, 111], [63, 49]]
for l in list_:
    print(f'НОД ({l[0]}, {l[1]}) = {evklid(*l)}')

a, b = map(int, input('\nВведите 2 числа через пробел: ').split())
print(f'НОД ({a}, {b}) = {evklid(a, b)}')
