import json
import csv

class ExportData :
    def __init__() :
        pass

    def exportToTxt(self) :
        pass

    def exportToCsv(self) :
        csv.dump(dbs, 'dbs.json')

    def exportToJSON(self, dbs) :
        json.dump(dbs, 'dbs.json')

    def exportDbs(self, dbs, type) :
        if type == 'json' :
            self.exportToJSON(dbs)

            TKinter