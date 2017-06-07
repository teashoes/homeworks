##### 1 про возраст##
a=(input('Please, enter your age:'))
if a.isdigit()==True:
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
else: 
    print('This cannot be your age!')

