pmax=0
pmin=9999
maxram=0
minram=99
memory=''
c=[]
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
        return int(s2)          #список s2  пребразовую в ИНТ

def mysort(s):
	p =s.split(':')
	x=p[3].strip()
	
	c=my_func(x)
	return c



spisok='''Lenovo A98; 1748UAH; screen: 5''; ram: 1GB; ROM : 16GB; qnty : 2; camera: 8MPx
Lenovo A300; 1244UAH; screen: 4''; ram: 2GB; ROM : 8GB; qnty : 16; camera: 2MPx 
Lenovo A15; 2748UAH; screen: 3''; ram: 4GB; ROM : 8GB; qnty : 3; camera: 4MPx 
Lenovo    A918; 1556UAH; screen: 6''; ram: 2GB; ROM : 4GB; qnty : 8; camera: 8MPx 
Lenovo G398;2148UAH; screen: 5''; ram: 4GB; ROM : 16GB; qnty : 21; camera: 4MPx 
Lenovo   S498;1045UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 1; camera: 4MPx 
Lenovo   Bt58; 1267UAH; screen: 3''; ram: 1GB; ROM : 2GB; qnty : 0; camera: 2MPx 
Lenovo  N98 ;  1433UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 4; camera: 16MPx 
Lenovo   M98;   1115UAH; screen: 5''; ram: 4GB; ROM : 4GB; qnty : 15; camera: 8MPx 
Lenovo       M8798; 1978UAH; screen: 6''; ram: 2GB; ROM : 1GB; qnty : 1; camera: 4MPx 
Lenovo H98;  1228UAH; screen: 4''; ram: 4GB; ROM : 2GB; qnty : 0; camera: 2MPx 
Lenovo A122 ; 1005UAH; screen: 4''; ram: 1GB; ROM : 1GB; qnty : 2; camera: 2MPx 
Lenovo A98; 1683UAH; screen: 5''; ram: 2GB; ROM : 4GB; qnty : 19 
Lenovo   M5   ; 2054UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 3; camera: 8MPx 
Lenovo A9 ; 1999UAH; screen: 6''; ram: 3GB; ROM : 16GB; qnty : 0; camera: 4MPx 
Lenovo A  ; 1074UAH; screen: 3''; ram: 2GB; ROM : 2GB; qnty : 0 
Lenovo A98;1648UAH; screen: 5''; ram: 3GB; ROM : 8GB; qnty : 2; camera: 2MPx 
Lenovo X10; 2099UAH; screen: 4''; ram: 4GB; ROM : 1GB; qnty : 21; camera: 1MPx 
Lenovo  C33 ; 1367UAH; screen: 5''; ram: 1GB; ROM : 0GB; qnty : 9 
Lenovo K6; 1845UAH; screen: 3''; ram: 2GB; ROM : 16GB; qnty : 17; camera: 8MPx 
Lenovo G7 ; 1409UAH; screen: 5''; ram: 1GB; ROM : 4GB; qnty : 10  
Lenovo N1  ; 1220UAH; screen: 4''; ram: 4GB; ROM : 4GB; qnty : 1; camera: 4MPx 
Lenovo X0  ; 1848UAH; screen: 4''; ram: 2GB; ROM : 2GB; qnty : 0; camera: 2MPx 
Lenovo F3; 1748UAH; screen: 5''; ram: 1GB; ROM : 8GB; qnty : 16 '''

items=spisok.split('\n')
#print(items)
n=''

while n!=7:
    print('\n узнать у кого больше всего рам 1\n\n','узнать у кого меньше всего рам 2\n\n','сортировка по возростанию ром 3\n\n','сортировка по убыванию ром 4\n\n','сортировать по диагонали экрана 5\n\n','сортировать по камере 6 \n\n','выход 7\n\n')
    n=int(input('введите ваш выбор:'))
    if n==1:
        for item in items:
            x=item.split(';')       
            ram=x[3].strip()     
            r=my_func2(ram)
            price=x[1].strip()
            c=my_func(price)
            name=x[0]
            neme=' '.join(name.split())
            if r>maxram:
                maxram=r
                maxName=neme
                maxPrice=c
        print('\n\n\n\t\tбольше всего ram' , maxram,' у' , maxName,maxPrice,' uah','\n\n')


    elif n==2:
        for item in items:
            
            x=item.split(';')       
            ram=x[3].strip()     
            r=my_func2(ram)
            name=x[0]
            neme=' '.join(name.split())
            price=x[1].strip()
            c=my_func(price)
            if r<minram:
                
                minram=r
                minName=neme
                minPrice=c

        print('\n\n\n\t\tменьше всего ram',minram,' у ' ,minName,minPrice, 'uah')

    elif n==3:
        s=items[:]
        s.sort(key=mysort)
        for i in s:
            x=i.split(';')
            name=x[0].strip()
            neme=' '.join(name.split())
            rom=x[4].strip()
            price=x[1].strip()
            c=my_func(price)
            print('\n\t',rom,neme,':',c,' uah')

    elif n==4:
        a=items[:]
        a.sort(key=mysort,reverse=True)
        for i in a:
            x=i.split(';')
            name=x[0].strip()
            neme=' '.join(name.split())
            rom=x[4].strip()
            price=x[1].strip()
            c=my_func(price)
            print('\n\t',rom,neme,':',c,' uah')
    else:
        print('\n\n\n\t\t\t','пункт ',n,'в разработке\n\n\n')
        

