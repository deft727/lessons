pmax=0
pmin=9999
maxram=0
minram=99
maxcam=0


def my_func(s):                         #моя ф-я для очистки цифр
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

def my_func2(s):                         #моя ф-я для очистки цифр
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

def my_func3(s):                         #моя ф-я для очистки цифр
    s2=''                               #переменая для чисел
    for i in s:                     #перебор в переданом ф-и списке
        if i.isdigit()!=True:       #если цифра
            continue                 #добавляю в перем.s2
        else:                       #иначе
            s2+=i                    #пропускаю
    if len(s2)==0:              #если в списке 0 элементов 
        return 0                #возвращаю 0
    else:                       #иначе
        return int(s2)     

def mysort(s):
	p =s
	x=p[n]
	c=my_func(x)
	return c
    
def mysort2(s):
	p =s
	x=p[n]
	c=my_func2(x)
	return c
    
def mysort3(s):
	p =s
	x=p[n]
	c=my_func3(x)
	return c

a=open('C:\\tmp1\data2.txt','r')
s=a.read()
items=s.split('\n')
#print(items)
items2=[]
for item in items:
   
    x=item.split(';')
    name=x[0].strip()
    name=' '.join(name.split())
    cena=x[1]
    price=my_func2(cena)
    scrin=x[2].strip()
    screen=my_func2(scrin)
    ram1=x[3].strip()
    ram=my_func2(ram1)
    ROM1=x[4].strip()
    ROM=my_func2(ROM1)
    qnty1=x[5].strip()
    qnty=my_func2(qnty1)
    try:
        camera=x[6].strip()
    except:
        camera='net'
   
    items2.append({'brand':name,'price':price,'screen':screen,'ram':ram,'ROM':ROM,'qnty':qnty,'camera':camera})

#print(items2)

n=''

while n!=0:
    print('\n узнать у кого самая большая цена 1\n\n','узнать у кого самая маленькая цена 2\n\n','узнать у кого больше всего рам 3\n\n','узнать у кого меньше всего рам 4\n\n','сортировка по возростанию цены 5\n\n','сортировка по убыванию цены 6\n\n','сортировать по диагонали экрана 7\n\n','сортировать по ром 8\n\n','сортировать по qnty 9\n\n','узнать у кого лучшая камера 10\n\n','сортировать по камере 11 \n\n','выход 0\n\n')
    n=int(input('введите ваш выбор:'))

    if n==1:
        for item in items2:
            
            x=item       
            price=x['price'].strip()
            c=my_func(price)
            name=x['brand']
            name=' '.join(name.split())
            if c>pmax:
                pmax=c
                maxName=name
                maxPrice=c
        print('\n\n\n\t\tсамая большая цена' ,maxPrice,' uah', ' у' , maxName,'\n\n')

    elif n==2:
        for item in items2:
            
            x=item       
            price=x['price']
            c=my_func(price)
            name=x['brand']
            name=' '.join(name.split())
            if c<pmin:
                pmin=c
                minName=name
                minPrice=c
        print('\n\n\n\t\tсамая меньшая цена' ,minPrice,' uah', ' у' , minName,'\n\n')
    
    elif n==3:
        for item in items2:
            
            x=item       
            ram=x['ram'].strip()     
            r=my_func(ram)
            price=x['price'].strip()
            c=my_func(price)
            name=x['brand']
            name=' '.join(name.split())
            if r>maxram:
                maxram=r
                maxName=name
                maxPrice=c
        print('\n\n\n\t\tбольше всего ram' , maxram,' у' , maxName,maxPrice,' uah','\n\n')

    
    elif n==4:
        for item in items2:
            
            x=item       
            ram=x['ram'].strip()     
            r=my_func(ram)
            price=x['price'].strip()
            c=my_func(price)
            name=x['brand']
            name=' '.join(name.split())
            if r<minram:
                minram=r
                minName=name
                minPrice=c

        print('\n\n\n\t\tменьше всего ram',minram,' у ' ,minName,minPrice, 'uah')

    elif n==5:
        n='price'
        s=items2[:]
        s.sort(key=mysort)
        for i in s:
            print(i['brand'],':',i['price'],' uah')

    elif n==6:
        n='price'
        a=items2[:]
        a.sort(key=mysort,reverse=True)
        for i in a:
            print(i['brand'],':',i['price'],' uah')
        
    elif n==7:
        n='screen'
        b=items2[:]
        b.sort(key=mysort)
        for i in b:
            print(i['brand'],' : ',i['screen'],' "')

    
    elif n==8:
        n='ROM'
        c=items2[:]
        c.sort(key=mysort)
        for i in c:
            
            print(i['brand'],' : ',i['ROM'],' ROM')

    elif n==9:
        n='qnty'
        q=items2[:]
        q.sort(key=mysort)
        for i in q:
            
            print(i['brand'],' : ',i['qnty'],' (qnty) ')

    elif n==10:
        n='camera'
        for item in items2:
            
            x=item   
            cam=x['camera'].strip()
            camera=my_func3(cam)
            name=x['brand'].strip()
            name=' '.join(name.split())
            if camera>maxcam:
                maxcam=camera
                maxName=name
                
        print('\n\n\n\t\tсамая большая камера' ,maxcam,' mpx', ' у', maxName , '\n\n')

    elif n==11:
        n='camera'
        q=items2[:]
        q.sort(key=mysort3)
        for i in q:
            
            print(i['brand'],' : ',i['camera'])

    else:
        print('\t\t\tвыход')

print(items2)
