class Command :
    def __init__(self)
        pass
    
    def doCommand(self, cmd) :
    c = cmd['command']
    if c == None :
        return
    if c == 'find' :
        self.doFind(cmd)
    if c == 'remove' :
        self.doRemove(cmd)

    def doFind(self, cmd) :
        table = cmd['table']
        if table == None :
            return
        p = False
        for t in database :
            if t['name'] == table :
                p = True
                db = t
                break
        if p == False :
            return
        cond = cmd['condition']
        if cond == None or cond == '' :
            self.showAllData(db)
            return
        for op, val in cond.items() :
            #print(op, val)
            args = cond[op]
            #print(args)
            #f = args[0]
            #val = args[1]
            #print(f, val)
            if op == '=' :    
                self.showEqData(db, args)
            if op == '>' :
                self.showGtData(db, args)
            if op == '<' :
                self.showLtData(db, args)
        
    def showEqData(self, db, args) :
            f = args[0]
            val = args[1]
            print(f, val)
            flds = db['fields']
            data = db['data']
            idx = flds.index(f)
            #print(flds)
            for line in data :
                #print(line)
                if line[idx] == val :
                    return line

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
