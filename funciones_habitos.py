def registrar_habitos(actividad): 
    """
    descripcion: la funcion dada una actividad y la guarda en una lista 

    parametros
    -------------
    actividad: str 
            la activdiad ingresada por el usuraio 
    lista_actividades: list 
            lista donde se guardan las actividades 
            
    retorna 
    -------------
    lista_actividades: list 
            lista donde etsan guardadas las activdiades 
            
    """
    
    lista_actividades = []  
    

    while True: 
        
        lista_actividades.append(actividad)
        
        actividad = input("Ingrese otra actividad (o escriba 'fin' para terminar): ")
        
        if actividad.lower() == "fin":
            break

    return lista_actividades

def analizar_habitos(lista):
    diccionario = {}
    for actividad in lista:
        if actividad not in diccionario:
            diccionario[actividad] = 1
        else:
            diccionario[actividad] += 1
    return diccionario

