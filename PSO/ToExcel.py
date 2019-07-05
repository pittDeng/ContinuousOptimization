import xlwt
import xlrd
from xlutils.copy import copy
class ToExcel:
    def __init__(self,fileName,sheetName):
        self.fileName=fileName
        try:
            temp=xlrd.open_workbook(fileName)
            self.f=copy(temp)
        except:
            self.f=xlwt.Workbook()
        try:
            self.sheet=self.f.get_sheet(sheetName)
        except:
            self.sheet=self.f.add_sheet(sheetName)
    def insertData(self,row_num,col_num,data):
        self.sheet.write(row_num,col_num,data)

    def save(self):
        self.f.save(self.fileName)

if __name__=="__main__":
    toexcel=ToExcel("hello.xls","second")
    toexcel.insertData(0,0,200)
    toexcel.insertData(2,2,300)
    toexcel.save()
