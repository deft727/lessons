def analyze(s):
    res = {
        "=": 0,
        "-": 0,
        "|": 0,
        'alpha': 0,
        'space': 0
    }
    for i in s:
        if i == '=':
            res["="] += 1
        if i == '-':
            res["-"] += 1
        if i == '|':
            res["|"] += 1
        if i == ' ':
            res["space"] += 1
        if i.isalnum():
            res["alpha"] += 1
    return res


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
    if a['|'] > 2 and a['alpha'] > 0 and state == 4:
        tmpName = line.split('|')
        fldsData = []
        for fname in tmpName:
            fldsData.append(fname.strip())
        # print(fldsName)
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


