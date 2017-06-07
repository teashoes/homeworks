###### 6 while про Валеру ##########
users=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

try:
    while True:
        if users[-1] == 'Валера':
            print('Валера нашелся!')
            break
        else:
            print(users[-1])
            users.pop()
except IndexError:
    print('Валеры тут нет...')