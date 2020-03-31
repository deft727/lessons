class DBMS :
    def __init__(self, filename):
        self.filename = filename

    def analyze(self, line):
        res = {
            "=" : 0,
            "-" : 0,
            "|" : 0,
            'alpha' : 0,
            'space' : 0
        }
        for i in line :
            if i == '=' :
                res["="] += 1
            if i == '-' :
                res["-"] += 1
            if i == '|' :
                res["|"] += 1
            if i == ' ' :
                res["space"] += 1
            if i.isalnum() :
                res["alpha"] += 1
        return res

    def importData(self):
        state = 0
        dbs = []
        f = open(self.filename, 'r') #'testDB.txt'
        c = f.read()
        lines = c.split('\n')
        l = 1
        for line in lines :
            a = self.analyze(line)
            #print(l,a)
            #print(l, state)
            #l += 1
            if a['='] > 8 and state == 0 :
                tableName = line.strip().strip('=').strip()
                #print(tableName)
                dbs.append({ "table-name": tableName, "data" : []})
                state = 1
            if a['-'] > 8 and state == 1 :
                state = 2
            if a['|'] > 2 and a['alpha'] > 0 and state == 2 :
                tmpName = line.split('|')
                fldsName = []
                for fname in tmpName :
                    fldsName.append(fname.strip())
                state = 3
            if a['|'] > 0 and a['-'] > 2 and state == 3 :
                state = 4  
            if a['|'] > 2 and a['alpha'] > 0 and state == 4 :
                tmpName = line.split('|')
                fldsData = []
                for fname in tmpName :
                    fldsData.append(fname.strip())
                #print(fldsName)
                dataItem = {}
                for j in range(len(fldsName)) :
                    #print(j)
                    dataItem[fldsName[j]] = fldsData[j]
                for db in dbs :
                    if db['table-name'] == tableName :
                        break
                db['data'].append(dataItem)
                #state = 5
            if a['-'] > 2 and a['|'] == 0 and state == 4 :
                state = 0

        return dbs    

    def doCommand(self, cmd):
        c = cmd['command']
        if c == None:
            return
        if c == 'find':
            self.doFind(cmd)
        if c == 'remove':
            self.doRemove(cmd)

    def doFind(self, cmd):
        table = cmd['table']
        if table == None:
            return
        p = False
        for t in database:
            if t['name'] == table:
                p = True
                db = t
                break
        if p == False:
            return
        cond = cmd['condition']
        if cond == None or cond == '':
            self.showAllData(db)
            return
        for op, val in cond.items():
            #print(op, val)
            args = cond[op]
            #print(args)
            #f = args[0]
            #val = args[1]
            #print(f, val)
            if op == '=' :    
                self.showEqData(db, args)
            if op == '>':
                self.showGtData(db, args)
            if op == '<':
                self.showLtData(db, args)
        
    def showEqData(self, db, args):
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data:
                #print(line)
                if line[idx] == val:
                    print(line)

    def showGtData(self, db, args):
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                print(line)
                if line[idx] > val:
                    print(line)

    def showLtData(self, db, args):
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                #print(line)
                if line[idx] < val :
                    print(line)
            
    def showAllData(self, db):
        data = db['data']
        for i in data :
            print(i)

