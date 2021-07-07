# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:33:48 2021

@author: Digital
"""

from PyQt5 import uic, QtWidgets
import sys

qtCreatorFile = "calculadora.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class miApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)     
        
        # agregamos los botones
        self.multiplicacion.clicked.connect(self.multiplica)
        self.suma.clicked.connect(self.sumar)
        self.resta.clicked.connect(self.restar)
        
        
    def multiplica(self):
        a = float(self.num1.text())
        b = float(self.num2.text())
        
        res = "El resultado es: "+ str(a*b)
        self.textResultado.setText(res)
        
    def sumar(self):
        a = float(self.num1.text())
        b = float(self.num2.text())
        
        res = "El resultado es: "+ str(a+b)
        self.textResultado.setText(res)
        
    def restar(self):
        a = float(self.num1.text())
        b = float(self.num2.text())
        
        res = "El resultado es: "+ str(a-b)
        self.textResultado.setText(res)
        

if __name__=="__main__":
    
    aplicacion=QtWidgets.QApplication(sys.argv)
    miaplicacion=miApp()
    miaplicacion.show()
    sys.exit(aplicacion.exec())