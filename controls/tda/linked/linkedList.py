from typing import Any
from controls.tda.linked.node import Node
from controls.exception.arrayPositionException import ArrayPositionException
from controls.exception.linkedEmpty import LinkedEmpty


class Linked_List(object):
    def __init__(self):
        self.__head = None 
        self.__last = None
        self.__lenght = 0
    
    @property
    def _head(self):
        return self.__head

    @_head.setter
    def _head(self, value):
        self.__head = value
 

    @property
    def _lenght(self):
        return self.__lenght

    @_lenght.setter
    def _lenght(self, value):
        self.__lenght = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__lenght == 0  

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node  
            self.__last = node
            self.__lenght += 1
        else:
            headOld = self.__head  
            node = Node(data, headOld)
            self.__head = node  
            self.__lenght += 1

    def __addLast__(self, data):
        if self.isEmpty:
           self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node
            self.__last = node
            self.__lenght += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__lenght = 0

    #insetar en una posicion           
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__lenght:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos - 1)
            node_last = node_preview._next #self.getNode(pos)
            node = Node(data, node_last)
            node_preview._next = node
            self.__lenght += 1
    
    #Modificar
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data 
        elif pos == self.__lenght:
            self.__last._data = data
        else:
            node = self.getNode(pos)  
            node._data = data
    @property
    def toArray(self):
        #TODO
        pass

    def delete(self, pos = 0):
        if self.isEmpty:
           raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:  # Si se va a eliminar el primer nodo
            if self.__lenght == 1:  # Si solo hay un nodo en la lista
                self.__head = None
                self.__last = None
            else:
                self.__head = self.__head._next
        elif pos == (self.__lenght - 1):  # Si se va a eliminar el último nodo
             node_prev = self.getNode(pos - 1)
             node_prev._next = None
             self.__last = node_prev
        else:  # Si se va a eliminar un nodo intermedio
            node_prev = self.getNode(pos - 1)
            node_next = node_prev._next._next
            node_prev._next = node_next
        self.__lenght -= 1

        
    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__lenght - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    def get(self, pos):
        
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._lenght:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__lenght - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
    
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            return "List is Empty"
        else:
            node = self.__head  # Cambio aquí
            while node != None:
                out += str(node._data) + "\t"
                node = node._next          
        return out
    
    @property
    def print(self):
        node =self.__head
        data =""
        while node != None :
            data += str(node._data) + "    "
            node = node._next

        print("Lista de datos")
        print(data)

# #Pasar la lista a arreglo
    # @property
    # def toArray(self):
    #     if self.isEmpty:
    #         return []
    #     else:
    #         array = []
    #         node = self._head  
    #         while node != None:
    #             array.append(node._data)
    #             node = node._next
    #         return array

    
    

    