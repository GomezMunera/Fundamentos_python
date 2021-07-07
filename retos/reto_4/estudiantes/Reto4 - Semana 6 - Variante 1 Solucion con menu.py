class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def incluir(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[len(self.items) - 1]

    def tamano(self):
        return len(self.items)

    def paginaActual(self, pagina):
        for i in range(self.tamano()):
            if (self.items[i] == pagina):
                posicion = i
        return posicion

    def atras(self, posicion):
        return posicion-1

    def adelante(self, posicion):
        return posicion+1

    def nombrePorPosicion(self, posicion):
        return self.items[posicion]

    def pilaAnteriores(self, posicion):
        anteriores = []
        for i in range(self.tamano()):
            if (i<posicion):
                anteriores.append(self.items[i])
        return anteriores

    def pilaAdelante(self, posicion):
        adelante = []
        for i in range(self.tamano()):
            if (i > posicion):
                adelante.append(self.items[i])
        return adelante

    def __str__(self):
        return str(self.items)

opc='1'
listaPaginas = Pila()
while(opc!='9'):
     opc = input("1. Agregar a la Pila\n2. Imprimir Pila\n3. Definir pagina Actual\n4. Default Pila\n5. Salir\n")
     if (opc == '1'):
         paginaNueva = input("Direcccion de la pagina? ")
         listaPaginas.incluir(paginaNueva)
     elif (opc == '2'):
         print(listaPaginas)
     elif (opc == '3'):
         posicionPaginaActual = listaPaginas.paginaActual(input("Escriba la pagina a buscar: "))
         pagOpc = '1'
         while(pagOpc!='5'):
             pagOpc = input("1. Mostrar Pilas Anterior y Adelante\n2. Funcion Atras\n3. Funcion Adelante\n4. Salir\n")
             if (pagOpc == '1'):
                print("Pagina Actual: ", listaPaginas.nombrePorPosicion(posicionPaginaActual))
                print("Pila Anteriores: ", listaPaginas.pilaAnteriores(posicionPaginaActual))
                print("Pila Adelante: ", listaPaginas.pilaAdelante(posicionPaginaActual))
             elif (pagOpc == '2'):
                posicionPaginaActual = listaPaginas.atras(posicionPaginaActual)
             elif (pagOpc == '3'):
                posicionPaginaActual = listaPaginas.adelante(posicionPaginaActual)
             else:
                 pagOpc = '5'
     elif (opc== '4'):
         listaPaginas.incluir("google.com")
         listaPaginas.incluir("youtube.com")
         listaPaginas.incluir("jw.org/es")
         listaPaginas.incluir("netflix.com")
         listaPaginas.incluir("micasa.com")
     else:
         opc = '9'
