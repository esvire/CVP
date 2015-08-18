from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import *
import sys

def main():
    app 	= QApplication(sys.argv)
    table 	= QTableWidget()
    db      = QSqlDatabase.addDatabase("QMYSQL")

    table.setWindowTitle("Connect to Mysql Database Example")   
    
    db.setHostName("localhost")
    db.setDatabaseName("db_CVP")
    db.setUserName("root")
    db.setPassword("12345")
    
    if (db.open()==False):
        QMessageBox.critical(None, "Database Error", db.lastError().text())

			    
    query = QSqlQuery("SELECT * FROM tbl_usuario")
    
    table.setColumnCount(query.record().count())
    table.setRowCount(query.size())
    table.setGeometry(0, 0,500,250)
    
    index = 0
    while (query.next()):
        table.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
        table.setItem(index,1,QTableWidgetItem(query.value(1).toString()))
        table.setItem(index,2,QTableWidgetItem(query.value(2).toString()))
        table.setItem(index,3,QTableWidgetItem(query.value(3).toString()))
        table.setItem(index,4,QTableWidgetItem(query.value(4).toString()))

        index = index+1

    table.show()
    
    return app.exec_()
if __name__ == '__main__':
    main()