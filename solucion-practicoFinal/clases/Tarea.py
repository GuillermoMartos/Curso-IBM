from enum import Enum
from .Color import colors
from datetime import datetime

# Clase Tarea. Se compone de nombre, detalle, fecha a ser ingresados por el usuario. El id lo recibe por medio de la Agenda en la que se crea. El estado predeterminado es 'pendiente' y puede ser cambiado a 'completada' por el usuario.

class Estado(Enum):
    COMPLETADA= 'completada'
    PENDIENTE= 'pendiente'

class Tarea():
    def __init__(self, fecha= datetime, detalle=str, nombre=str, id=int):
        self._fecha=fecha
        self._detalle=detalle
        self._nombre=nombre
        self.__id=id
        self.__estado= Estado.PENDIENTE.value

    @property
    def estado(self):
        return self.__estado
    
    @property 
    def idFilter(self):
        return self.__id
    
    @estado.setter
    def set_estado(self, cambio=Estado):
        self.__estado = Estado.COMPLETADA.value if(cambio==Estado.PENDIENTE.value) else Estado.PENDIENTE.value
        print('TAREA ACTUALIZADA:', self.detalleTarea())

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def set_fecha(self, nuevaFecha):
        self._fecha=nuevaFecha
        print('FECHA ACTUALIZADA:', self.detalleTarea())
    
    def detalleTarea(self):
        return f"""{colors.VIOLET}
        Tarea: {self._nombre}. 
        Programada para fecha: {self._fecha.strftime("%d/%m/%Y")}. 
        Detalle: {self._detalle}. 
        Estado: {self.__estado} 
        ID_TAREA: {self.__id}
        {colors.ENDC}
        """ if self.__estado == Estado.COMPLETADA.value else f"""{colors.BLUE}
        Tarea: {self._nombre}. 
        Programada para fecha: {self._fecha.strftime("%d/%m/%Y")}. 
        Detalle: {self._detalle}. 
        Estado: {self.__estado} 
        ID_TAREA: {self.__id}
        {colors.ENDC}
        """