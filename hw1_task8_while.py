######### 8 вопрос ответ ########
##Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user(question):
    while question.lower() != 'хорошо':
        question = input('Как дела? ')
    print('Молодец')

if __name__ == '__main__':
    qq=ask_user(str(input('Как дела?')))