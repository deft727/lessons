a=open('C://tmp1/test.txt','r')
q=a.read()
s=q.split('\n')



def digit(s):                         #моя ф-я для очистки цифр
    s2=''                               #переменая для чисел
    for i in s:                     #перебор в переданом ф-и списке
        if i.isdigit()==True:       #если цифра
            s2+=i                   #добавляю в перем.s2
        else:                       #иначе
            break                   #пропускаю
    if len(s2)==0:              #если в списке 0 элементов
        return 0                #возвращаю 0
    else:                       #иначе
        return int(s2)

def alpha(s):
    s2=''
    for i in s:
        if i.isalpha():
            s2 += i
    return s2

def analyze(str) :
    symbols = {
        '=' : 0,
        '-' : 0,
        'alpha' : 0,
        '|' : 0,
        'digit':0
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

    return symbols
dict1=[]

for i in s:
    res = analyze(i)
    if res['=']>10:
        name=alpha(i)

    if res['alpha']==17:
        






