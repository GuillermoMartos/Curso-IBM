import importlib.util

# Cargamos el módulo 009_Ejercicios_Condicionales_3.py
spec = importlib.util.spec_from_file_location("ejercicios_condicionales_3", "./009_Ejercicios_Condicionales_3.py")
ejercicios_condicionales_3 = importlib.util.module_from_spec(spec)

# Desarrolla un programa que solicite la calificación de un examen (0 a 100) 
# y devuelva el rango de desempeño basado en la puntuación: insuficiente, 
# suficiente, bien, muy bien, o excelente.

spec.loader.exec_module(ejercicios_condicionales_3)
