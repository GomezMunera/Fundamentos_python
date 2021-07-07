from vector import vector
from lista_ligada import LSL
# In[ ]:

"""
Colas en listas
"""

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
print("\nElementos desencolados de la cola")
print(queue.pop(0))
print("\nDespués de eliminar los elementos")
print(queue)


# ## Métodos de la clase Cola
# - __init__: Crea una cola vacía.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __es_vacia__: devuelve True o False según si la cola está vacía o no.
# - __muestraCola__: imprime lo que tiene la cola.

# In[8]:


"""
Clase Cola
"""

class Cola:
    def __init__(self):
        self.items=[]
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    def es_vacia(self):
        return self.items == []
    def muestraCola(self):
        print(self.items)
        
q = Cola()
print("Está vacía? ",q.es_vacia())
q.encolar(1)
q.encolar(2)
q.encolar(3)
q.muestraCola()
print("Está vacía? ",q.es_vacia())
q.desencolar()
q.muestraCola()


# •	Ejercicio [colas] -> Codifique el siguiente programa:
# - Construya un ciclo infinito, donde:
#     - Dentro del ciclo, solicite al usuario que ingrese una opción:
#         - 1 - para encolar, acaba debe solicitar el valor a encolar e ingresarlo en la cola
#         - 2 - para desencolar e imprimir el valor desencolado
#         - 3 - para imprimir el contenido de la cola
#         - 0 - para salir
#    
# 

# In[ ]:


queue=[]
while True:
    x=int(input("ingrese una opcion: "))   
    if (x == 1):
        valor=(input("ingrese valor a encolar: "))
        queue.append(valor)
    elif (x == 2):
        try:
            queue.pop(0)
        except IndexError:
            print("La cola está vacía")
    elif (x == 3):
        print(queue)
    else:
        print("saliendo del sistema")
        break


# # 2. Colas con la clase vector
# ### Métodos de la clase Cola
# - __init__: Crea un objeto vector.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __esVacia__: devuelve True o False según si la cola está vacía o no.
# - __esLlena__: devuelve True o False si la cola está llena o no.
# - __siguiente__: deveulve el elemento próximo a desencolar.

# In[ ]:

    """
    utilizando la clase vector
    """

class colaVector(vector):
    
        def __init__(self, n):
            vector.__init__(self, n)
            self.primero = 0
            self.ultimo = 0
            
        def esLlena (self):
            return self.primero == self.ultimo
        
        def esVacia (self):
            return self.primero == self.ultimo
        
        def encolar (self, d):
            self.ultimo = (self.ultimo + 1) % self.n
            if self.esLlena():
                print("cola llena, no se puede encolar\n")
                self.ultimo = (self.ultimo - 1 + self.n) % self.n
                return
            self.V[self.ultimo] = d
            
        def desencolar (self):
            if self.esVacia():
                print("cola vacía, no se puede desencolar\n")
                return None
            self.primero = (self.primero + 1) % self.n
            return self.V[self.primero]
        
        def siguiente (self):
            if self.esVacia():
                print("cola vacía, no hay siguiente\n")
                return None
            aux = (self.primero + 1) % self.n
            return self.V[aux]
    
qu = colaVector(10)
print("Está vacía? ",qu.esVacia())
print("Está llena? ",qu.esLlena())
qu.encolar("a")
qu.encolar("b")
qu.encolar(316)
print("Elemento próximo a desencolar", qu.siguiente())
d = qu.desencolar()
print("\nDato desencolado:", d)


# # 3. Colas con la clase LSL
# ### Métodos de la clase Cola
# - __init__: Crea un objeto lista ligada.
# - __encolar__: Agrega el elemento x como último de la cola.
# - __desencolar__: Elimina el primer elemento de la cola y devuelve su valor. Si la cola está vacía, levanta ValueError.
# - __siguiente__: deveulve el elemento próximo a desencolar.

# In[ ]:


class colaLSL(LSL):
     def __init__(self):
         LSL.__init__(self)
     
     def encolar(self, d):
         self.agregarDato(d)
     
     def desencolar(self):
        if self.esVacia():
            print("\nCola vacía no hay datos para desencolar")
            return None
        d = self.primero.retornarDato()
        p = self.primerNodo()
        self.borrar(p)
        return d
     
     def siguiente (self):
         if self.esVacia():
             print("\nCola vacía no hay siguiente")
             return None
         d = self.primero.retornarDato()
         return d

a = colaLSL()
b = a.esVacia()
print(b)
a.encolar("a")
a.encolar("e")
a.encolar("i")
a.encolar("o")
a.recorrerLista()
b = a.esVacia()
print("\nEstá vacía? ", b)
d = a.desencolar()
print("\ndato desencolado es: ", d)
a.recorrerLista()
d = a.siguiente()
print("\nel siguiente es:", d)
d = a.desencolar()
a.recorrerLista()


# # 4. Cola con la clase queue

# In[7]:


import queue

q = queue.Queue()
print(q.qsize())

for i in range(5):
    q.put(i)
print("Tamaño,",q.qsize())

print("Está vacía?,",q.empty())
print("Desencolar",q.get())
print("Tamaño,",q.qsize())

while not q.empty():
    print(q.get(), end=' ')

#print(q)
