'''
Created on Jan 16, 2021

@author: jct
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from PyQt5.Qt import QStandardItemModel, QStandardItem

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.menubar.setNativeMenuBar(False)

if __name__ == '__main__':
    print("*** main ***")
    app = QApplication([])
    
    main_window = MainWindow()
    main_window.show()
    
    foo = [["a", "b"], ["c", "d"]]
    
    model = QStandardItemModel(main_window.lv_enrollees)
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
        
    main_window.lv_enrollees.setModel(model)
            
    app.exec_()
