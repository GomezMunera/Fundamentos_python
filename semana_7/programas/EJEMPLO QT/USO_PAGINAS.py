from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys
from VENTANA_PRIN import *
# from PyQt5.QtWidgets import QApplication, QDialog

class miventana(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)     
        
        ## Se conecta el boton a una señal para cuando se le dé un click
        ## y se le asigna el método a realizar.
        self.ui.ABRIR.clicked.connect(self.mostrarMensaje)
        
        
    def mostrarMensaje(self):
        ## textEdit recibe un texto enriquecido, entonces es necesario ponerle 
        ##el tipo de conversión. En este caso texto plano.
        print("hola")
        # hola=self.ui.textEdit.toPlainText()
      
        # # hola="holaas"
        # self.ui.label.setText(hola)

if __name__=="__main__":
    
    aplicacion=QApplication([])
    miaplicacion=miventana()
    miaplicacion.show()
    sys.exit(aplicacion.exec())
    