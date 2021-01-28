'''
Created on Jan 23, 2021

@author: jct
'''

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.Qt import QStandardItemModel, QStandardItem
from ui_mainwindow import Ui_MainWindow
from xltest import load_spreadsheet

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
        
        model = QStandardItemModel(self.lv_enrollees)
        foods = [
            ['Cookie dough',1], # Must be store-bought
            ['Hummus', 2], # Must be homemade
            ['Spaghetti', 3], # Must be saucy
            ['Dal makhani', 4], # Must be spicy
            ['Chocolate whipped cream', 5] # Must be plentiful
        ]
     
        for foodlist in foods:
            (food, cost) = foodlist
            
            print(food)
            # Create an item with a caption
            item = QStandardItem(food)
         
            # Add a checkbox to it
            item.setCheckable(True)
         
            # Add the item to the model
            model.appendRow(item)
            
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
