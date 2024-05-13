from clases.Agenda import Agenda
from clases.Tarea import Tarea
from clases.Color import colors
from datetime import datetime

textoOpcionInvalida = f'{colors.YELLOW}Opción seleccionada no válida...{colors.ENDC}'
textoError= f'{colors.RED}error inesperado... intentemos de vuelta{colors.ENDC}'

# función seguirOSalir se corre cada vez que finalizamos una tarea o si hubo un error para que el usuario elija cuando salir del programa (pulsando la "q") o si lo sigue usando (pulsando el "1")
def seguirOSalir(misAgendas:list[Agenda]):
    try:
        rta= input(f"""
                   1️⃣{colors.GREEN} Presione 1 si desea acceder o crear agenda.{colors.ENDC}
                   🏁{colors.RED} Para salir, presione letra 'Q/q' {colors.ENDC}
                   """).lower()
        if(rta=='q'):
            print(f'{colors.GREEN}Gracias por usar la Agenda Python! Hasta la próxima!{colors.ENDC}')
            return
        if(rta=='1'):
            return accederOCrearAgenda(misAgendas)
        else:
            print(textoOpcionInvalida)
            return seguirOSalir(misAgendas)
    except:
        print(textoError)
        return seguirOSalir(misAgendas)

# función accederOCrearAgenda revisa las agendas creadas en la lista misAgendas hasta el momento y nos permite crear una nueva o ingresar a una existente. Si accedemos a una, imprime el estado actual de las tareas de la agenda elegida.
def accederOCrearAgenda(misAgendas:list[Agenda]):
    try:
        if len(misAgendas)>0:
            print('Estas son tus agendas:')
            opcionesAgendas=[]
            for index, agenda in enumerate(misAgendas):
                opcionesAgendas.append(index)
                print (f'{colors.VIOLET}Id: {index}, Agenda: {agenda.nombreAgenda}{colors.ENDC}' if index%2 
                       else f'{colors.BLUE}Id: {index}, Agenda: {agenda.nombreAgenda}{colors.ENDC}')
            opcion=input(f"""
                    🔢 {colors.GREEN}Ingrese número identificador de agenda para acceder {colors.ENDC}
                    🆕 {colors.BLUE}Ingrese letra N para crear nueva agenda...{colors.ENDC}
                    """).lower()
            if (opcion=='n'):
                return crearAgenda(misAgendas)
            if(opcion.isnumeric() and opcionesAgendas.count(int(opcion))):
                agendaElegida = misAgendas[int(opcion)]
                print(f'Accediendo a {agendaElegida.nombreAgenda}')
                agendaElegida.comoVieneLaAgenda()
                editarTareasOCrearNueva(agendaElegida)
                return seguirOSalir(misAgendas)
            print(textoOpcionInvalida)
            return seguirOSalir(misAgendas)
        else:
            print(f'{colors.YELLOW}No tienes agendas aún... ¿Creamos una nueva?{colors.ENDC}')
            return crearAgenda(misAgendas)
            
    except:
        return seguirOSalir(misAgendas)

# función crearNuevaTarea toma los inputs necesarios para crear una nueva tarea, la añade a nuestra agenda en uso y nos muestra en pantalla la tarea nueva. Si se genera un error, lo imprime en pantalla.
def crearNuevaTarea(agenda:Agenda):
    try:
        print(f'Vamos a crear nueva tarea para agenda {agenda.nombreAgenda}')
        nombreTarea = input(f'Ingrese {colors.BOLD}nombre{colors.ENDC} de tarea nueva... ')
        fechaTarea = tomarYValidarFecha()
        detalleTarea = input(f'Ingrese {colors.BOLD}detalle{colors.ENDC} de tarea nueva... ')
        miTareaNueva = Tarea(fechaTarea, detalleTarea, nombreTarea, agenda.generadorIncrementalDeIds)
        agenda.agregarTarea(miTareaNueva)
        print(f'{colors.GREEN}¡Tarea creada con éxito!:{colors.GREEN}  {miTareaNueva.detalleTarea()}')
        mostrarMensajesTrasCambiosEnTarea(agenda)
    except Exception as error:
        print(textoError, error)

# función tomarYValidarFecha se encarga de validar la fecha ingresada como valor fecha y en formato dd/mm/yyyy y la devuelve
def tomarYValidarFecha():
    try:
        fecha= input(f'Ingrese {colors.BOLD}fecha en formato dd/mm/yyy{colors.ENDC} de tarea nueva... ')
        return datetime.strptime(fecha, '%d/%m/%Y')
    except Exception as error:
        print(f'{colors.YELLOW}Error en la fecha ingresada, intente de nuevo...{colors.ENDC}', error)
        return tomarYValidarFecha()

# función crearAgenda recibe la lista de agendas y le añade una nueva con el input necesario.
def crearAgenda(misAgendas:list[Agenda]):
            nombre = input('Ingrese nombre para nueva agenda Python ')
            miAgendaNueva = Agenda(nombre)
            misAgendas.append(miAgendaNueva)
            print(f'{colors.GREEN}¡Éxito! Agenda {nombre} creada {colors.ENDC}')
            crearNuevaTarea(miAgendaNueva)
            return seguirOSalir(misAgendas)

def mostrarMensajesTrasCambiosEnTarea(agenda=Agenda):
    input('Presione cualquier tecla para continuar y ver cómo quedó su agenda...')
    return agenda.comoVieneLaAgenda()

# función editarTareasOCrearNueva recibe input para crear nueva tarea y llama a la función crearNuevaTarea; o toma los parámetros para cambiar una tarea existente en la agenda.
def editarTareasOCrearNueva(agenda:Agenda):
    opcion= input(f"""
                  🆕 {colors.GREEN}Ingrese letra n para crear nueva tarea{colors.ENDC}
                  📝 {colors.YELLOW}Ingrese un numero de ID_TAREA de tarea a editar{colors.ENDC} 
                  🏁 {colors.RED}Ingrese letra "Q/q" para salir{colors.ENDC}
                  """)
    if(opcion=='n'):
        return crearNuevaTarea(agenda)
    if(opcion=='q'):
        return
    try:
        opcionNumeral=int(opcion)
        for tarea in agenda.tareas:
            if tarea.idFilter == opcionNumeral:
                editOpcion= input(f"""
                    Modificando {tarea.nombre}.
                    1️⃣ Ingrese 1 si desea cambiar su estado
                    2️⃣ Ingrese 2 si desea cambiar su fecha
                    ❌ {colors.RED}Ingrese 0 para eliminarla de su agenda{colors.ENDC}
                    🏁 {colors.RED}Ingrese letra "Q/q" para volver atrás{colors.ENDC}
                      """)
                if(editOpcion=='1'):
                    tarea.set_estado = tarea.estado
                    return mostrarMensajesTrasCambiosEnTarea(agenda)
                if(editOpcion=='2'):
                    nuevaFecha= tomarYValidarFecha()
                    tarea.set_fecha= nuevaFecha
                    return mostrarMensajesTrasCambiosEnTarea(agenda)
                if(editOpcion=='0'):
                    agenda.eliminarTarea(opcionNumeral)
                    return mostrarMensajesTrasCambiosEnTarea(agenda)
                if(editOpcion=='q'):
                    return
        raise Exception
    except Exception as error:
        print(textoError, error)
        return editarTareasOCrearNueva(agenda)
