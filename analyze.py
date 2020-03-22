a=open('H://test.txt','r')
b=a.read()
s=b.split('\n')

def digit(s):                         
    s2=''                               #переменая для чисел
    for i in s:                     #перебор в переданом ф-и списке
        if i.isdigit()!=True:       #если цифра
            continue                 #добавляю в перем.s2
        else:                       #иначе
            s2+=i                    #пропускаю
    if len(s2)==0:              #если в списке 0 элементов
        return 0                #возвращаю 0
    else:                       #иначе
        return s2

def analyze(str) :
    symbols = {
        '=' : 0,
        '-' : 0,
        'alpha' : 0,
        '|' : 0,
        'digit':0,
		'space':0
    }
    for i in str :
        if i == '=' :
            symbols['='] += 1
        if i == '-' :
            symbols['-'] += 1
        if i =='|':
            symbols['|']+=1
        if i.isdigit() == True:
            symbols['digit']+=1
        if i.isalpha():
            symbols['alpha']+=1
		#if i == ' ' :
		#	res['space']+=1

    return symbols

def alpha(s):
    s2=''
    for i in s:
        if i.isalpha():
            s2 += i
    return s2


dbs=[]
dict={}
for i in s:
    res = analyze(i)
    if res['=']>10:

        table=alpha(i)


		


    if res['alpha']>10 and res['digit']<1:
        name=i.split(' | ')

    if res['|'] >= 3 and res['-'] < 7 and res['digit'] > 1:
        val = i.split('|')


        dict = {}
        dict['data'] = []
        t={}
        for j in range(len(name)):
            t[name[j]] = val[j]


        dict['table_name'] = table
        dict['data'].append(t)

        dbs.append(dict)


n=''
while n!=0:
    print('\n\nчто ищем?, sales = нажать 1,customers = нажать 2,orders = нажать 3, 0 = выход: \n\n\n')
    n=int(input('введите ваш выбор:'))

    if n==1:
            for i in dbs:
                if i['table_name']=='sales':
                    print(i)
    if n==2:
            for i in dbs:
                if i['table_name']=='customers':
                    print(i)
    if n==3:
            for i in dbs:
                if i['table_name']=='orders':
                    print(i)
                    