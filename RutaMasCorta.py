import random as r

# Fase adivinadora: Seleccionar las aristas que formarán parte de la trayectoria usando random
def fase_adivinadora(aristas):
    elegidas = []
    for arista in aristas:
        rand = r.choice([True, False])
        if rand:
            elegidas.append(arista)
    return elegidas

#Fase verificadora: Verificar si el numero de aristas elegidas es menor o igual a k, 
# y si es una u-v trayectoria con las aristas elegidas
# Recibe: Lista de aristas de la forma [u, v], int k, int vértice inicial, int vértice final, int numero de vertices
# Regresa: True si es una u-v trayectoria de peso < = k, False en otro caso
def fase_verificadora(elegidas, k, u_inicial, v_final, num_vertices):
    
    suma = len(elegidas) # Obtenemos la suma de los pesos de las aristas
        
    if suma > k: # Si la suma es mayor a k, no es lo que buscamos
        print("El numero de aristas elegidas es mayor a k")
        return False
    else: #Verificar si es una u-v trayectoria
        
        matriz = crear_matriz_adyacencias(elegidas, num_vertices) # Crear matriz de adyacencias de acuerdo a las aristas elegidas
        vertices_elegidos = obtener_vertices(elegidas) # Obtener los vértices en los que inciden las aristas elegidas
        
        #Verificar Si alguna arista incide en u_inicial y si alguna incide en u final
        inicial = False
        final = False
        for vertice in vertices_elegidos:
            if not inicial or not final:
                if vertice == u_inicial:
                    inicial = True
                elif vertice == v_final:
                    final = True
            else:
                break
            
        # Si hay aristas que inciden en el vértice inicial y final
        if inicial and final:
            
            for vertice in vertices_elegidos: # Verificar si es una trayectoria
                fila = matriz[vertice]
                contador = 0 # Contador de aristas de la trayectoria propuesta que inciden en el vértice actual
                for i in fila:
                        if i != 0:
                            contador += 1
                            
                if vertice != u_inicial and vertice != v_final: # Si no es el vértice inicial o final
                    if contador > 2: # No puede terner más de 2 aristas que incidan en él
                        print("No es una trayectoria")
                        return False
                else:
                    if contador > 1: # Si es el vértice inicial o final, no puede tener más de 1 arista que incida en él
                        print("No es una trayectoria")
                        return False
                
            
            matriz = dfs(matriz, u_inicial,v_final) # Hacemos dfs a partir del vértice inicial
                
            #Verificar si todos los vértices marcados fueron visitados    
            for vertice in vertices_elegidos:
                if matriz[0][vertice] == 0:
                    print("No es una trayectoria")
                    return False
                
            return True
        
        else: # Si no hay aristas que incidan en el vértice inicial o final
            print("No hay aristas que incidan en el vértice inicial o final")
            return False 
        
# Obtener los vertices en los que inciden las aristas
# Recibe: Lista de aristas de la forma [u, v]
# Regresa: Lista de vertices
def obtener_vertices(aristas):
    vertices = []
    for arista in aristas:
        if arista[0] not in vertices:
            vertices.append(arista[0])
        if arista[1] not in vertices:
            vertices.append(arista[1])
    return vertices
       

# Crear matriz de adyacencias
# Recibe: Lista de aristas de la forma [u, v], int numero de vertices
# Regresa: Matriz de adyacencias con la fila 0 y columna 0 vacías
def crear_matriz_adyacencias(aristas, num_vertices):
    #Inicializar matriz
    matriz = [] 
    for i in range(num_vertices + 1):
        fila = []
        for j in range(num_vertices + 1):
            fila.append(0)
        matriz.append(fila)
    
    #Hacemos las adyacencias con el peso de la arista  
    for arista in aristas:
        u = arista[0]
        v = arista[1]
        matriz[u][v] = 1
        matriz[v][u] = 1
        
    return matriz

# Realizar un recorrido en profundidad
# Recibe: Matriz de adyacencias, int vertice desde donde empieza, int vertice final de la trayectoria
# Regresa: Matriz de adyacencias con los vértices visitados marcados con -1 en la fila 0 y columna 0
def dfs(matriz_adyacencias, vertice, vertice_final):
    
    if matriz_adyacencias[0][vertice] == 0:
        
        matriz_adyacencias[0][vertice] = -1
        matriz_adyacencias[vertice][0] = -1
        
        fila = matriz_adyacencias[vertice]
                
        for i in range(1, len(fila)):
            if fila[i] != 0:
                #print("dfs en (",vertice, ",", i, ")")
                matriz_adyacencias = dfs(matriz_adyacencias, i, vertice_final)
                #imprimir_matriz(matriz_adyacencias)
            
    return matriz_adyacencias

# Imprimir matriz
# Recibe: Matriz de adyacencias
def imprimir_matriz(matriz):
    inicio =[]
    for i in range(0, len(matriz)):
        inicio.append(i)
    print("\n ",inicio,"\n")
    for i in range(0, len(matriz)-1):
        print(i, matriz[i])
            
        

if __name__=="__main__":
    k = 5
    archivo = input("Nombre del archivo del ejemplar: ")
    try:
        archivo = open(archivo) #Abrir el archivo  que se quiere leer
    except:
        print("\nNo se encontró el archivo, se abrirá el archivo RutaMasCorta.txt\n")
        archivo = open("RutaMasCorta.txt") #Abrir el archivo
    
    cadenas = [] #Lista para guardar las cadenas del archivo
    while(True): #Leer el archivo
        linea = archivo.readline()
        if not linea:
            break
        else:
            cadenas.append(linea) 
                
    vertices = (cadenas[0].replace("\n", "")).split(",") #Los vertices son la primer cadena del archivo
    for vertice in vertices:
        vertices[vertices.index(vertice)] = int(vertice)
        
        
    vertice_inicial = vertices[0] #Seleccionar un vertice inicial
    vertice_final = vertices[r.randint(1, len(vertices)-1)] #Seleccionar un vertice final
    print("Vértice inicial: ", vertice_inicial, " Vértice final: ", vertice_final)
    
    adyacencias = [] #Agregar las aristas
    for i in range(1, len(cadenas)):
        adyacencias.append(cadenas[i].replace("\n","").split(","))
    
    for arista in adyacencias: #Convertir las aristas a enteros
        arista[0] = int(arista[0])
        arista[1] = int(arista[1])
    
    
    elegidas = fase_adivinadora(adyacencias) # Seleccionar las aristas que formarán parte de la trayectoria propuesta por la fase adivinadora
    print("\nPosible uv-trayectoria dada por la fase adivinadora: ", elegidas)
    
    respuesta = fase_verificadora(elegidas, k, vertice_inicial, vertice_final, len(vertices)) # Verificar si la trayectoria propuesta por la fase adivinadora es correcta
    print("\nFase verificadora: ",respuesta)
    
    #imprimir_matriz(crear_matriz_adyacencias(elegidas, len(vertices)))
    
    #El siguiente ejemplo debe dar True con el ejemplar del archivo RutaMasCorta.txt
    #r = fase_verificadora([[6,4],[6,7]], k, 4,7,10)
    #print(r)

    
    