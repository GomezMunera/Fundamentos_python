# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:59:43 2021

@author: Digital
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:33:48 2021

@author: Digital
"""

from PyQt5 import uic, QtWidgets


#from PyQt5.QtWidgets import QApplication


import sys

qtCreatorFile = "calculadora.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# from PyQt5.QtWidgets import QApplication, QDialog

class miApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        #self.ui=Ui_MainWindow()
        self.setupUi(self)  
        
        # botones
        self.multiplicacion.clicked.connect(self.multi)
        
        
        
        ## Se conecta el boton a una señal para cuando se le dé un click
        ## y se le asigna el método a realizar.
        #self.ui.ABRIR.clicked.connect(self.mostrarMensaje)
        
        
    def multi(self):
        # si se usa Text edit usar:
        # float(self.numero1.toPlainText())
        num1 = float(self.numero1.text())
        num2 = float(self.numero2.text())
        res_st = "El resultado es: "+str(num1*num2)
        self.result.setText(res_st)
        
if __name__=="__main__":
    
    aplicacion=QtWidgets.QApplication(sys.argv)
    miaplicacion=miApp()
    miaplicacion.show()
    sys.exit(aplicacion.exec())