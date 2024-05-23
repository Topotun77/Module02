# Реализуйте в отдельной функции алгоритм Евклида (алгоритм нахождения наибольшего общего
# делителя (НОД) пары целых чисел), возвращая НОД. Проверить полученную функцию на списке,
# состоящем из 10 пар чисел (пример пар: [[5, 7], [21, 111], [63, 49]]).

def evklid(a, b):
    new_a = b % a
    if new_a == 0:
        return a
    else:
        return evklid(new_a, a)


def func_nod2(a, b):
    while a and b:
        a, b = b, a
        b %= a
    return a


def func_nod(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b


list_ = [[5, 7], [21, 111], [63, 49]]
for l in list_:
    print(f'НОД ({l[0]}, {l[1]}) = {evklid(*l)}\t\t{func_nod(*l)}\t\t{func_nod2(*l)}')

a, b = map(int, input('\nВведите 2 числа через пробел: ').split())
print(f'НОД ({a}, {b}) = {evklid(a, b)}\t\t{func_nod(a, b)}\t\t{func_nod2(a, b)}')
