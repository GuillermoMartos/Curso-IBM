from .Tarea import Tarea
from .Color import colors

#Clase Agenda. Su función es la de contener una lista de Tareas y un nombre  para sí.
class Agenda:
    def __init__(self, nombreAgenda) -> None:
        self.nombreAgenda:str=nombreAgenda
        self.tareas:list[Tarea]=[]
        self.__privateIdGenerator=0
    
    @property
    def generadorIncrementalDeIds(self):
        self.__privateIdGenerator = self.__privateIdGenerator + 1
        return self.__privateIdGenerator

    def comoVieneLaAgenda(self):
        print(f"""-----------------------------
                {colors.GREEN}Su agenda {self.nombreAgenda} viene así:{colors.ENDC}""")
        for tarea in self.tareas:
            print(f'➡ {tarea.nombre}: {tarea.detalleTarea()}')
        print('-----------------------------')
    
    def agregarTarea(self, tareaNueva = Tarea):
        self.tareas.append(tareaNueva)
    
    def eliminarTarea(self, id):
        print(f'¿Seguro quieres eliminar la tarea con el id... {id}?')
        yorn= input(f"""
                    👍 Ingrese Y para borrar
                    {colors.RED}❌ Ingrese N para desistir{colors.ENDC}
                    """).lower()
        if yorn=='y':
            for tarea in self.tareas:
                if tarea.idFilter == id: self.tareas.remove(tarea)
                return
        elif yorn == 'n':
            print('Cancelando borrado...')
            return
        else:
            print('Opción no válida, reintentamos...')
            return self.eliminarTarea(id)