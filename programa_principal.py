import funciones_habitos 
 
actividad = input("ingrese una actividad: ") 

lista = funciones_habitos.registrar_habitos()
resultado = funciones_habitos.analizar_habitos(lista)
print("Resumen de actividades:")
print(resultado)
