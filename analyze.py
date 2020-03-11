a=open('C://tmp1/test.txt','r')
s=a.read()


def analyze(str) :
    symbols = {
        '=' : 0,
        '-' : 0,
        'alpha' : 0,
        '|' : 0
    }
    for i in str :
        if i == '=' :
            symbols['='] += 1
        if i == '-' :
            symbols['-'] += 1
        if i =='|':
            symbols['|']+=1
    return symbols

dict=[]
res = analyze('====================  sales  ================')
if res['='] > 10 :
    s.strip('=')
    s.strip()
    dict.append({s})
    print(dict)