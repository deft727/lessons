import sys

sys.path.append('./classes/import')
sys.path.append('./classes/commands')

from importData import ImportData
from command import Command

i = ImportData('./data/input/testDb.txt')

i.importFromTxt()

#print(i.getDbs())

cmd = Command(i.getDbs())

"""req = {
    "command" : "remove",
    "table" : "sales",
    "condition" : {
        "=" : ['city', 'Londoself.databasen']
    }
}"""


req = {
     "command" : "insert",
     "table" : "sales",
     "values" : { 'snum' : 1008,
                   'city' : 'Kiyv',
                'sname' : "John"
                 }
}

cmd.doCommand(req)

