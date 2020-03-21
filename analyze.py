a=open('C://tmp1/test.txt','r')
b=a.read()
s=b.split('\n')


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

dbs=[]

for i in s:
    res = analyze(i)
    if res['=']>10 and state==0:

        table=i.strip().strip('=').strip()
        dbs.append({ "table-name": table, "data" : []})
        #print(table)
        state=1

    if res['-'] > 8 and state == 1 :
        state = 2

    if res['|'] > 2 and res['alpha'] > 0 and state == 2 :
        name=i.strip().split(' | ')
        #print(name)
        fldsName = []
        for fname in name:
            fldsName.append(fname)
            #print(fldsName)
        state=3

    if res['|'] > 0 and res['-'] > 2 and state == 3 :
        state = 4

    if res['digit'] > 2 and res['alpha'] >= 0   and state==4:
        val = i.strip().split('|')

        fldsData = []

        for fname in val:
            fldsData.append(fname)
        #print(fldsData)
        dataItem = {}
        for j in range(len(fldsName)) :
            dataItem[fldsName[j]] = fldsData[j]
        for db in dbs :
            if db['table-name'] == table :
                break
        db['data'].append(dataItem)
        #state = 5

    if res['-'] > 2 and res['|'] == 0 and state == 4:
        state = 0


for i in dbs:
    print(i)