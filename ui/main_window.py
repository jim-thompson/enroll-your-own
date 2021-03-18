'''
Created on Jan 23, 2021

@author: jct
'''

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.Qt import QStandardItemModel, QStandardItem
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from ui_mainwindow import Ui_MainWindow
from xltest import load_spreadsheet

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data[index.row()][index.column()]
            return str(value)

    def rowCount(self, index):
        try:
            return len(self._data)
        except:
            return 0

    def columnCount(self, index):
        try:
            return len(self._data[0])
        except:
            return 0


class MainWindow(Ui_MainWindow, QMainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)
        
        self.a_load.triggered.connect(self.load)
        self.a_quit.triggered.connect(self.quit)

        foo = [["a", "b"], ["c", "d"]]
        
        foods = [
            ['Cookie dough',1], # Must be store-bought
            ['Hummus', 2], # Must be homemade
            ['Spaghetti', 3], # Must be saucy
            ['Dal makhani', 4], # Must be spicy
            ['Chocolate whipped cream', 5] # Must be plentiful
        ]
     
        model = TableModel(foods)
        self.lv_enrollees.setModel(model)
        
    def quit(self):
        print("Bye now!")

    def load(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
#         dlg.setFilter("Text files (*.txt)")
#         filenames = QStringList()
#         dlg.exec_()

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            for f in filenames:
                print("### <%s>" % f)
                load_spreadsheet(f)
