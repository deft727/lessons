from dbms import DBMS

db = DBMS('test.txt')
db.importData()






cmd = {
    "command" : "find",
    "table" : "sales",
    "condition" : {
        "=" : ['city', 'London']
    }
}
db.doCommand(cmd)
