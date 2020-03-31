import ImportData from importdata
import Command from commands
import ExportData from exportdata

class App :
    def __init__(self) :
        self.imp = ImportData()
        self.cmd = Command()
        self.exp = ExportData()

    def loadInfo(self) :
        self.imp.importFromTxt()
    
    def workData(self, req) :
        commd = decode(req)
        self.cmd.doCommand(commd)

    def unloadInfo(self) :
        dbs = self.imp.getDbs()
        self.exp.exportDbs(dbs, 'json')


