oper_dic = {"+": 'сложить',
            "-": 'вычесть',
            "*": 'умножить',
            "/": 'разделить',
            "**": 'степень'
            }


stop_ = False
while not stop_:
    num1, num2 = map(int, input('Введите 2 числа через пробел: ').split())

    print('Введите действие с числами:', end='\n\n')
    for i in oper_dic:
        print(f'"{i}" - {oper_dic[i]}')
    print()

    oper_ = input("Ваш выбор: ")
    print('Ответ:')

    if oper_ in oper_dic:
        my_command = f'result = num1 {oper_} num2'
        exec(my_command)
        print(f'{num1} {oper_} {num2} = {result}', end='\n\n')
    else:
        print(f'Не знаю такой операции {oper_}', end='\n\n')

    stop_ = input('Посчитать еще раз (Y/N)? ') in 'Nn'
