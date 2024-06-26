def multiplicity(xx, yy):     # проверка кратности 2 чисел
    return yy % xx == 0

def pass_wd(nn):             # основная функция
    result = ""
    for i in range(1, (nn + 1) // 2):
        for j in range(i + 1, nn - i + 1):
            if multiplicity(i + j, nn):
                result += str(i) + str(j)
    return result


n = 0 # использовано имя переменной из одной буквы, т.к. в задании оно так было указано, хотя PEP 8 не рекомендует
while n < 3 or n > 20:
    n = int(input("Введите число от 3 до 20: "))
print("Пароль:", pass_wd(n))

# сверка паролей с тем, что дано в задании, т.к. проверять вручную очень муторно

pass_dic = {3: "12",
    4: "13",
    5: "1423",
    6: "121524",
    7: "162534",
    8: "13172635",
    9: "1218273645",
    10: "141923283746",
    11: "11029384756",
    12: "12131511124210394857",
    13: "112211310495867",
    14: "1611325212343114105968",
    15: "1214114232133124115106978",
    16: "1317115262143531341251161079",
    17: "11621531441351261171089",
    18: "12151811724272163631545414513612711810",
    19: "118217316415514613712811910",
    20: "13141911923282183731746416515614713812911"}

res_bool = {True: "Все зашибись!",
            False: "Косяк какой-то, нужно фиксить!"}

test_pass = True
for i in range(3, 21):
    test_pass = test_pass and pass_wd(i) == pass_dic[i]
    if pass_wd(i) != pass_dic[i]:
        print(i, pass_wd(i))
print("\nРезультат сверки всех паролей со значениями из текста задания: ", res_bool[test_pass])