import sys

sys.path.append('./classes')

from app import App

app = App()

app.loadInfo()

f = open('reqs.txt', 'r')

app.workData({
    "command" : "find",
    "table" : "sales",
    "condition" : {
        ">" : ['comm', 0.12]  
    }
})

app.unloadInfo()


#python DB.py reqs.txt