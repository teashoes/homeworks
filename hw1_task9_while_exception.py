################ 10 исключения #######
############ переделать###########
###При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

def get_answer(question):
    try:
        def ask_user(question):
            question=question.lower()
            answer = {"привет": "И тебе привет!", "Как дела": "Лучше всех", "пока": "Увидимся"}
            answer =  {k.lower(): v for k, v in answer.items()} #приводим ключи к нижнему регистру
            if question in answer.keys():
                return answer.get(question)
            else:
                return 'не понимаю'
        question=question.lower()   
        while question != 'пока':
            if question != 'не понимаю': #### до тех пора пока не пока
                print(ask_user(question))
                question=input('') #### дальше даем спрашивать
            else: 
                question=input('') 
    except KeyboardInterrupt:
        print('Вы чегооо?..')
    return print(ask_user(question))

if __name__ == '__main__': 
    qq=get_answer(input(''))
