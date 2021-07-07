

class nodoSimple:
    """
    Esta clase crea un nodo simple nuevo, con dato y liga.
    el dato inicial es d y la liga None:
        nuevonodo = nodoSimple(d)
    """
    
    def __init__(self, d = None):
        self.dato = d
        self.liga = None
        
    def asignarDato(self, d):
        self.dato = d
        
    def asignarLiga(self, x):
        self.liga = x
        
    def retornarDato(self):
        return self.dato
    
    def retornarLiga(self):
        return self.liga


    
class LSL:
    """
    Lista simplemente ligada:
        Esta clase crea una lista simplemente ligada, a partir de objetos
        nodoSimple
    """
    
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None
        
    def primerNodo (self):
        return self.primero
    
    def ultimoNodo (self):
        return self.ultimo
    
    def esVacia (self):
        return self.primero == None
    
    def finDeRecorrido (self, p):
        return p == None
    
    def recorrerLista (self):
        """
        Este método recorre la lista a través de la actualización repetida
        de la liga del primer elemento hasta llegar al último
        """
        p = self.primerNodo()
        
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end = ",")
            p = p.retornarLiga()
            #print(p)
            
    def agregarDato (self, d):
        x = nodoSimple(d)      ## se crea un nodo simple con dato d
        p = self.primerNodo()  ## se llama el primer nodo
        
        if p == None:
            self.primero = x   ## si es el primer nodo que se agrega 
            self.ultimo = x    ## entonces se le asigna la primera y ultima posicion
        else:
            self.ultimo.liga = x  ## sino se cambia la liga del ultimo que estaba
            self.ultimo = x       ## al atributo ultimo se le asigna el nodo que se acaba de ingresar
    
    def buscarDondeInsertar (self, d):
        """
        Este método retorna un lugar para ingresar un nodo, sin embargo
        no puede usarse si la lista ligada está vacía, se debe 
        agregar primero un nodo
        """
        p = self.primerNodo()  ## se asigna a p el primer nodo
        y = None               ## se carga 'y' con None, por si no se encuentra el dato durante la búsqueda
        
        ## Se analiza si es no se ha llegado al final del recorrido,
        ## o si el dato fue encontrado
        while not self.finDeRecorrido(p) and p.retornarDato() < d:
            y = p
            p = p.retornarLiga()
            ## Si se encuentra el dato se le asigna a
            ## 'y' el nodo en el que se encuentra
        return y

    def insertar (self, d, y):
        """
        Para insertar un dato nuevo, se le asigna al dato un nodo nuevo
        y luego se llama el método conectar para que se realice la conexión
        ------
        NOTA: Solo se puede usar si ya se ha ingresado por lo menos un nodo
        """
        x = nodoSimple(d)
        self.conectar(x, y)
        
    def conectar (self, x, y):
        """
        Para conectar se reciben dos nodos 
        """
        if y == None:
            if self.primero == None: ## Si es None, es porque la lista está vacía
                self.ultimo = x      ## Entonces se asigna el nodo que ingresa como el último
            else:
                x.asignarLiga(self.primero)
                self.primero = x
            return
        
        ## Se ligan ambos nodos
        x.asignarLiga(y.retornarLiga())
        y.asignarLiga(x)           
        
        if y == self.ultimo:
            self.ultimo = x
            
    def longitud (self):
        p = self.primerNodo()
        n = 0
        #Se recorre las lista y se van contando los nodos con n
        while not self.finDeRecorrido(p):
            n = n + 1
            p = p.retornarLiga()
        return n
    
    def buscarDato (self, d, y):
        ## Se le asigna a x el primer nodo
        x = self.primerNodo()
        ## Se ejecuta el while mientras no se llegue al final del recorrido
        ## y mientras el dato que se obtenga del nodo evaluado en cada ciclo no sea 'd'
        while not self.finDeRecorrido(x) and x.retornarDato() != d:
            ## se entra al ciclo hasta que se encuentre el dato o
            ## se termine la lista ligada
            ## En cada ciclo se asigna el dato a x para obtener
            ## la siguiente liga y seguir preguntando por el dato
            y.asignarDato(x)
            x = x.retornarLiga()
        return x
    
    def borrar (self, x, y = None):
        if x == None:
            print("Dato no está en la lista")
            return
        
        if y == None:
            if x != self.primero:
                print("Falta el anterior del dato a borrar")
                return
        else:
            y = y.retornarDato()
        self.desconectar(x, y)


    def borrar_ultimo (self):
        ## Se pregunta si el ultimo no está vacío
        if self.ultimo != None:
            
            dat=self.ultimo.dato           ## Se obtiene el dato del último nodo
            y = nodoSimple()               ## Se crea un nodo auxiliar para ejecutar el método buscar
            x = self.buscarDato(dat, y)    ## Se busca la posición del dato
            self.borrar(x, y)              ## Se borra dicho dato
        else:
            print("La lista está vacía")   ## Si la lista está vacía
            
                
    def desconectar (self, x, y):
        ## Se reciben los dos nodos a desconectar "x" y "y"
        
        if y == None: 
            ## Si el nodo "y" está vacío, 
            ## se lleva a el primero la liga del nodo "x"
            ## Quedando así conectado al primero de la lista
            self.primero = x.retornarLiga()
            
            if self.esVacia():
                ## Si la lista está vacía se asigna un None
                ## a el último elemento
                self.ultimo = None          
        else:
            ## si el nodo "y" no es None
            ## se conecta con el nodo "x"
            y.asignarLiga(x.retornarLiga())
            
            if x == self.ultimo:
                ## Si se identifica que x es el último 
                ## se asigna "y" como último elemento
                self.ultimo = y
                
                
                
                