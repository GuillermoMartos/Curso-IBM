from datetime import datetime
from utils import accederOCrearAgenda
from clases.Agenda import Agenda
from clases.Color import colors

"""""Enunciado:
Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione
una lista de Tarea pendientes. El programa deberá permitir al usuario realizar las siguientes
operaciones:
• Agregar una nueva tarea: El programa deberá permitir al usuario agregar una nueva tarea a
la lista de Tarea pendientes.
• Marcar una tarea como completada: El programa deberá permitir al usuario marcar una
tarea como completada, dada su posición en la lista.
• Mostrar todas las Tarea: El programa deberá imprimir en pantalla todas las Tarea
pendientes, numeradas y mostrando su estado (completada o pendiente).
• Eliminar una tarea: El programa deberá permitir al usuario eliminar una tarea de la lista,
dada su posición.

El programa deberá incluir las siguientes características:
• Manejo de excepciones: El programa deberá manejar excepciones en caso de que el
usuario ingrese una opción no válida o una posición que no exista en la lista.
• Comentarios explicativos: El código deberá estar comentado para explicar su
funcionamiento en cada parte relevante.
"""

date= datetime.now()
print(f'''
      {colors.BLUE}Bienvenido a su Agenda Python{colors.ENDC}
      {colors.VIOLET}Son las {date.hour}:{date.minute} del día {date.strftime("%d/%m/%Y")}.{colors.ENDC}
    ''')
misAgendas:list[Agenda]=[]
accederOCrearAgenda(misAgendas)

