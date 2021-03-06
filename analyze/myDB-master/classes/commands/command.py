class Command :
    def __init__(self, dbs) :
        self.database = dbs
        
    
    def doCommand(self, cmd) :
        c = cmd['command']
        if c == None :
            return
        elif c == 'find' :
            self.doFind(cmd)
        elif c == 'remove':
            self.doRemove(cmd)
        elif c == 'update':
            self.doUpdate(cmd)
        elif c== 'insert':
            self.doInsert(cmd)


    def doFind(self, cmd) :
        table = cmd['table']
        if table == None:
            return
        p = False
        for t in self.database:
            # print(t)
            if t['table-name'] == table:
                p = True
                db = t
                break
        if p == False:
            return
        cond = cmd['condition']
        if cond == None or cond == '':
            # self.showAllData(db)
            return
        for op, val in cond.items():
            # print(op, val)
            args = cond[op]
            # print(args)
            # f = args[0]
            # val = args[1]
            # print(f, val)
            if op == '=':
                self.showEqData(db, args)
            if op == '>':
                self.showGtData(db, args)
            if op == '<':
                self.showL
        
    def showEqData(self, db, args) :
            f = args[0]
            val = args[1]
            #print(f, val)
            #flds = db['fields']
            data = db['data']
            #idx = flds.index(f)
            #print(flds)
            for line in data :
                if line[f] == val :
                    print(line)

    def showGtData(self, db, args) :
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                print(line)
                if line[idx] > val :
                    return line

    def showLtData(self, db, args) :
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
            
    def showAllData(self, db) :
        data = db['data']
        for i in data :
            print(i)

    def doInsert(self,cmd):

        datas = self.database
        table = cmd['table']
        val = cmd['values']

        for i in datas:
            if datas['table_name']==table:

                print(i)

    def doRemove(self,cmd):
        table = cmd['table']
        cnd = cmd['condition']
        for k, v in cnd.items():
            if k == '=':
                data = self.database
                #print(data)

                '''datas = dbs['data']
                for data in datas:
                    if data[v[0]] == v[1]:
                        datas.remove(data)
                        print(datas)'''

