
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


state = 0
dbs = []
f = open('test.txt', 'r')
c = f.read()
lines = c.split('\n')
l = 1
for line in lines:
    a = analyze(line)
    # print(l,a)
    # print(l, state)
    # l += 1
    if a['='] > 8 and state == 0:
        tableName = line.strip().strip('=').strip()
        # print(tableName)
        dbs.append({"table-name": tableName, "data": []})
        state = 1
    if a['-'] > 8 and state == 1:
        state = 2
    if a['|'] > 2 and a['alpha'] > 0 and state == 2:
        tmpName = line.split('|')
        fldsName = []
        for fname in tmpName:
            fldsName.append(fname.strip())
        state = 3
    if a['|'] > 0 and a['-'] > 2 and state == 3:
        state = 4
    if a['digit'] > 2 and a['alpha'] >= 0   and state==4:
        val = line.strip().split('|')

        fldsData = []

        for fname in val:
            fldsData.append(fname)
        #print(fldsData))
        dataItem = {}
        for j in range(len(fldsName)):
            # print(j)
            dataItem[fldsName[j]] = fldsData[j]
        for db in dbs:
            if db['table-name'] == tableName:
                break
        db['data'].append(dataItem)
        # state = 5
    if a['-'] > 2 and a['|'] == 0 and state == 4:
        state = 0
    if a['-'] == 0 and state == 5 :
        state = 4

n=''
while n!=0:
    print('\n\nчто ищем?, sales = нажать 1,customers = нажать 2,orders = нажать 3, 0 = выход: \n\n\n')
    n=int(input('введите ваш выбор:'))

    if n==1:
            for i in dbs:
                if i['table-name']=='sales':
                    print(i)
    if n==2:
            for i in dbs:
                if i['table-name']=='customers':
                    print(i)
    if n==3:
            for i in dbs:
                if i['table-name']=='orders':
                    print(i)
