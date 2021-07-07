# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 01:03:26 2021

@author: Digital
"""

from vagones import Nodo

class ListaEnlazada(Nodo):
    " Modela una lista enlazada, compuesta de Nodos. "
    
    def __init__(self):
        """ Crea una lista enlazada vacía. """
        super().__init__()
        # prim: apuntará al primer nodo - None con la lista vacía
        self.prim = None
        # len: longitud de la lista - 0 con la lista vacía
        self.len = 0
        
    def __str__(self):
        return str(self.dato)
    
    def __len__(self):
        return str(self.len)
    
    def empty(self):
      return self.prim == None
  
    def insert(self, i, x):
        """ Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError """
        
        if (i > self.len) or (i < 0):
            # error
            raise IndexError("Posición inválida")
        
        # Crea nuevo nodo, con x como dato:
        nuevo = Nodo(x)
        
        # Insertar al principio (caso particular)
        if i == 0:
            # el siguiente del nuevo pasa a ser el que era primero
            nuevo.prox = self.prim
            # el nuevo pasa a ser el primero de la lista
            self.prim = nuevo
        
        # Insertar en cualquier lugar > 0
        else:
            # Recorre la lista hasta llegar a la posición deseada
            n_ant = self.prim
            for pos in range(1,i):
                n_ant = n_ant.prox
        
            # Intercala nuevo y obtiene n_ant -> nuevo -> n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo
        
        # En cualquier caso, incrementar en 1 la longitud
        self.len += 1
        
    def append(self, x):
        """ Inserta el elemento x en la primera posición.
         """
         
         # Crea nuevo nodo, con x como dato:
        nuevo = Nodo(x)
        
        if self.len == 0:
            # el siguiente del nuevo pasa a ser el que era primero
            nuevo.prox = self.prim
            # el nuevo pasa a ser el primero de la lista
            self.prim = nuevo
        
        else: 
        
            # Obtiene el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
                
            while n_act != None:
                n_ant = n_act
                n_act = n_ant.prox
        
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        
        # En cualquier caso, incrementar en 1 la longitud
        self.len += 1
    
    def pop(self, i = 0):
        """ Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento. """
        
        # Verificación de los límites
        if (i < 0) or (i >= self.len):
            raise IndexError("Índice fuera de rango")
        
        # Si no se recibió i, se devuelve el último.
        if i == 0:
            i = self.len - 1
        
        # Caso particular, si es el primero,
        # hay que saltear la cabecera de la lista
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        
        # Para todos los demás elementos, busca la posición
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox
        
            # Guarda el dato y elimina el nodo a borrar
            dato = n_act.dato
            n_ant.prox = n_act.prox
        
        # hay que restar 1 de len
        self.len -= 1
        # y devolver el valor borrado
        return dato
    
    def remove(self, x):
        """ Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError """
        
        if self.len == 0:
            # Si la lista está vacía, no hay nada que borrar.
            raise ValueError("Lista vacía")
            
        # Caso particular, x esta en el primer nodo
        elif self.prim.dato == x:
            # Se descarta la cabecera de la lista
            self.prim = self.prim.prox
            
        # En cualquier otro caso, hay que buscar a x
        else:
            # Obtiene el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            
            while n_act != None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox
                
            # Si no se encontró a x en la lista, levanta la excepción
            if n_act == None:
                raise ValueError("El valor no está en la lista.")
                
            # Si encontró a x, debe pasar de n_ant -> n_x -> n_x.prox
            # a n_ant -> n_x.prox
            else:
                n_ant.prox = n_act.prox
        
        # Si no levantó excepción, hay que restar 1 del largo
        self.len -= 1
        
        
    def printList(self):
       n = self.prim
       for i in range(self.len):
       #while not n != None:
            print(n.dato, end = ", ")
            n = n.prox

# In[]
l2 = ListaEnlazada()
l2.insert(0,"hola")
l2.insert(1,"mundo")
l2.append("PR")