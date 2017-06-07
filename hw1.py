##### 1 про возраст##
a=(input('Please, enter your age:'))
if a.isdigit()==False:
    print('This cannot be your age!')
elif a.isdigit()==True:
    if int(a)>=0:
        if int(a)<=7:
            print('You must be at kindergarden!')
        elif int(a)<=18:
            print('You must be studying at school!')
        elif int(a)<=23:
            print('You must be studying at university!')
        else:
            print('You must be working!')
    else: print('You cannot be that age!')


##### 2 равенство строк####
#Если строки одинаковые, возвращает 1.
#Если строки разные и первая длиннее, возвращает 2.
#Если строки разные и вторая строка 'learn', возвращает 3.
def fun(aa,bb):
    if str(aa) == str(bb):
        print('1')
    elif len(aa)>len(bb):
        print(3)
    elif str(bb)=='learn':   
        print(2)
if __name__ == '__main__':
    ass=fun('22a', '11')

##### 3 оценки студентов +1 ####
students_scores = [1, 21, 19, 6, 5, 6, 22, 34, 55, 34] 
for score in students_scores:
    print(score + 1)

##### 4 показать строка ####
a=('234561')
for score in a:
    print(score)  

##### 5 посчитать средние значения ####
### правильный #######
school_data = [
    {'class': '4a', 'scores': [3,4,4,5,2]}, 
    {'class':'4b', 'scores': [3,5,6,5,2]}, 
    {'class':'4v', 'scores': [3,4,2,3,2]}
]

z=[] #заведем список куда запишем значения 
for class_data in school_data:
    print(class_data['class'], sum(class_data['scores'])/len(class_data['scores']))
    z.append(sum(class_data['scores'])/len(class_data['scores']))
print(round(sum(z)/len(school_data), 1))

#сделала в лоб - изменила немного словарь и без цикла 
a={'4а':[3,4,4,5,2], '4б':[3,5,6,5,2],'4в':[3,4,2,3,2]}
z = (int(sum(a['4а']))+int(sum(a['4б']))+int(sum(a['4в']))) # сумма баллов по школе
yz = (int(len(a['4а']))+int(len(a['4б']))+int(len(a['4в']))) # колчиество учеников

print('Средний балл в классе 4А '+ str(sum(a['4а'])/len(a['4а'])))
print('Средний балл в классе 4Б '+ str(sum(a['4б'])/len(a['4б'])))
print('Средний балл в классе 4В '+ str(sum(a['4в'])/len(a['4в'])))
print('Средний балл в школе '+ str(round(z/yz, 1)))


###### 6 while про Валеру ##########
users=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

while True:
    if users[-1] == 'Валера':
        print('Валера нашелся!')
        break
    else:
        users.pop()
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
                users.pop()
    except IndexError:
        print('Таких нет')

if __name__ == '__main__':
    qq=find_person('Даша')

######### 8 вопрос ответ ########
##Написать функцию ask_user() чтобы помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user(question):
    while question != 'Хорошо':
        question = input('Как дела? ')
    print('Молодец')

if __name__ == '__main__':
    qq=ask_user(str(input('как дела?')))

######### 9 ответ вопрос ##############
##При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!

def ask_answer(answer):
    while answer != 'Пока':
        answer=str(input('Как дела? '))
if __name__ == '__main__':
    qq=ask_answer(str(input('как дела? ')))

################ 10 исключения #######
############ переделать##########
def ask_user(question):
    try: 
        while question.lower() != 'хорошо':
            if question.isdigit():
                raise ValueError() 
                question = input('Как дела? ')
    except ValueError:
        print('Я гуманитарий..')
    except KeyboardInterrupt:
        print('Вы чегооо?..')
    print(':) Пока')

if __name__ == '__main__':
    qq=ask_user(input('как дела? '))

def get_answer(question):
    answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    return answer.get(question) 