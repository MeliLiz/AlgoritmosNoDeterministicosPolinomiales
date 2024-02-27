import random as r
import re

#Fase adivinadora
def fase_adivinadora(aristas):
    elegidas = []
    for arista in aristas:
        rand = r.choice([True, False])
        if rand:
            elegidas.append(arista)
    return elegidas

#Fase verificadora
def fase_verificadora(elegidas, k, u_inicial, v_final, num_vertices):
    
    suma = sumar_pesos(elegidas)
        
    if suma > k: 
        print("La suma de los pesos de las aristas elegidas es mayor a k")
        return False
    else: #Verificar si es una u-v trayectoria
        
        matriz = crear_matriz_adyacencias(elegidas, num_vertices)
        
        #Verificar Si alguna arista tiene a u
        inicial = False
        for num in matriz[u_inicial]:
            if num != 0:
                inicial = True
                break
         
        if inicial:
            #Verificar Si alguna arista tiene a v
            final = False 
            for num in matriz[v_final]:
                if num != 0:
                    final = True
                    break
            
            if final:
                
                matriz = dfs(matriz, u_inicial)
                
                #Obtener los vértices en los que incide alguna arista elegida
                vertices_elegidos = obtener_vertices(elegidas)
                    
                #Verificar si todos los vértices marcados fueron visitados    
                for vertice in vertices_elegidos:
                    if matriz[0][vertice] == 0:
                        print("No se visitaron todos los vértices que inciden en las aristas elegidas")
                        return False
                    
                return True
                    
            else:
                print("No hay aristas que incidan en el vértice final")
                return False  
        else:
            print("No hay aristas que incidan en el vértice inicial")
            return False 
        
def obtener_vertices(aristas):
    vertices = []
    for arista in aristas:
        if arista[0] not in vertices:
            vertices.append(arista[0])
        if arista[1] not in vertices:
            vertices.append(arista[1])
    return vertices
       
def sumar_pesos(aristas):
    suma = 0
    for arista in aristas:
        suma += arista[2]
    return suma
    
def crear_matriz_adyacencias(aristas, num_vertices):
    matriz = [] #Inicializar matriz
    for i in range(num_vertices + 1):
        fila = []
        for j in range(num_vertices + 1):
            fila.append(0)
        matriz.append(fila)
        
    for arista in aristas:
        u = arista[0]
        v = arista[1]
        matriz[u][v] = arista[2]
        matriz[v][u] = arista[2]
        
    return matriz

def dfs(matriz_adyacencias, vertice):
    
    if matriz_adyacencias[0][vertice] == -1:
        
        matriz_adyacencias[0][vertice] = -1
        matriz_adyacencias[vertice][0] = -1
        
        fila = matriz_adyacencias[vertice]
                
        for i in range(1, len(fila)):
            if fila[i] != 0:
                matriz_adyacencias = dfs(matriz_adyacencias, i)
            
    return matriz_adyacencias

def imprimir_matriz(matriz):
    inicio =[]
    for i in range(0, len(matriz)):
        inicio.append(i)
    print("\n ",inicio,"\n")
    for i in range(0, len(matriz)-1):
        print(i, matriz[i])
            
        

if __name__=="__main__":
    k = 25
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
        
    print("Vertices: ",vertices)
    vertice_inicial = vertices[0] #Seleccionar un vertice inicial
    print("Vertice inicial: ",vertice_inicial)
    vertice_final = vertices[r.randint(1, len(vertices)-1)] #Seleccionar un vertice final
    print("Vertice final: ",vertice_final)
    
    adyacencias = [] #Agregar las aristas
    for i in range(1, len(cadenas)):
        adyacencias.append(re.split('[:,]',cadenas[i].replace("\n","")))
    
    for arista in adyacencias:
        arista[0] = int(arista[0])
        arista[1] = int(arista[1])
        arista[2] = int(arista[2])
        
    print("Aristas", adyacencias)
    
    elegidas = fase_adivinadora(adyacencias)
    print ("Elegidas: ",elegidas)  
    
    respuesta = fase_verificadora(elegidas, k, vertice_inicial, vertice_final, len(vertices))
    print(respuesta)
    #respuesta = fase_verificadora(elegidas, k, vertice_inicial, vertice_final, len(vertices))
    
    
    