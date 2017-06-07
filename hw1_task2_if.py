##### 2 равенство строк####
#Если строки одинаковые, возвращает 1.
#Если строки разные и первая длиннее, возвращает 2.
#Если строки разные и вторая строка 'learn', возвращает 3.
def fun(aa,bb):
    if str(aa) == str(bb):
        print('1')
    elif len(aa)>len(bb):
        print('3')
    elif str(bb)=='learn':   
        print('2')
    else:
        print('None')
if __name__ == '__main__':
    ass=fun('22', '11')