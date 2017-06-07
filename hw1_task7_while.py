####### 7 Валера функция #####
def find_person(name): 
    # name = input('Кто потерялся? ')
    users=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    try:
        while True:
            if users[-1] == str(name):
                print('Нашелся пользователь ' + name)
                break
            else:
                print(users[-1])
                users.pop()
    except IndexError:
        print('Таких нет')

if __name__ == '__main__':
    qq=find_person('Вася')