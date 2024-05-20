import json
from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty


class StackOperation(Linked_List):
    def __init__(self):
       tope = 20
       super().__init__()
       self.__tope = tope
    

    @property
    def _tope(self):
        return self.__tope

    @_tope.setter
    def _tope(self, value):
        self.__tope = value

    @property
    def verifyTop(self):
        return  self._lenght <= self.__tope

    def push(self, data):
          if self._lenght < self.__tope:
              self.add(data)
          else:  
              self.delete()
              self.add(data)
              
    @property    
    def pop(self):
        if self.isEmpty:
            raise LinkedEmpty("Stack empty")
        else:
            return self.delete()
        
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._data
            current = current._next   
        
    def to_json(self):
        stack_list = []
        for i in range(self._lenght):
            stack_list.append(self.get(i))
        
        # Convertir la lista en JSON
        json_data = json.dumps(stack_list)
        
        # Especificar la ruta del archivo
        file_path = r"C:\Users\USUARIO_PC\Documents\Proyecto Estructura\Practica1\data\stack_data.json"
        
        # Guardar el JSON en el archivo
        with open(file_path, "w") as file:
            file.write(json_data)

        print("JSON guardado en", file_path)

        return  stack_list
    
    @staticmethod
    def from_json(file_path):
        with open(file_path, "r") as file:
            json_data = file.read()
        stack_list = json.loads(json_data)
        stack_operation = StackOperation()
        for data in stack_list:
            stack_operation.push(data)
        return stack_operation