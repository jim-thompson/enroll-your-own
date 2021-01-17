'''
Created on Jan 16, 2021

@author: jct
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.menubar.setNativeMenuBar(False)

if __name__ == '__main__':
    print("*** main ***")
    app = QApplication([])
    
    main_window = MainWindow()
    main_window.show()
    
    app.exec_()
