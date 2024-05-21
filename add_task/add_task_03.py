import random

list_ = []
for i in range(50):     # Список малький, часто не находится ни одного элемента, удовлетворяющего условиям
    list_.append(random.randint(1,9999))


list_sort = sorted(list_)

count_ = 0
mean_ = (list_sort[0] + list_sort [len(list_sort)-1]) / 2
print(f'Среднее арифметическое: {mean_}\nСписок: {list_}')
for i in list_sort:
    if i % 41 == 0 and i > mean_:
        count_ += 1
        print(f'{count_}: {i}')

print(f'Количество элементов, удовлетворяющих условию: {count_}')