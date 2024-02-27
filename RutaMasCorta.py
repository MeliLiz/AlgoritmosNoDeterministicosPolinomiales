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
    suma = 0
    for arista in elegidas:
        suma += int(arista[2])
        
    if suma > k: 
        return False
    else: #Verificar si es una u-v trayectoria
        
        matriz = crear_matriz_adyacencias(elegidas)
        
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
                
                matriz = bfs(matriz, u_inicial)
                
                #Obtener los vértices en los que incide alguna arista elegida
                vertices_elegidos = []
                for arista in elegidas:
                    if arista[0] not in vertices_elegidos:
                        vertices_elegidos.append(arista[0])
                    
                    if arista[1] not in vertices_elegidos:
                        vertices_elegidos.append(arista[1])
                    
                #Verificar si todos los vértices marcados fueron visitados    
                for vertice in vertices_elegidos:
                    if matriz[0][vertice] == 0:
                        return False
                    
                return True
                    
            else:
                return False  
        else:
            return False 
        
    
def crear_matriz_adyacencias(aristas, num_vertices):
    matriz = [] #Inicializar matriz
    for i in range(num_vertices)+1:
        fila = []
        for j in range(num_vertices)+1:
            fila.append(0)
        matriz.append(fila)
        
    for arista in aristas:
        u = int(arista[0])
        v = int(arista[1])
        matriz[u][v] = arista[2]
        matriz[v][u] = arista[2]
        
    return matriz

def bfs(matriz_adyacencias, vertice):
    
    if matriz_adyacencias[0][vertice] == -1:
        matriz_adyacencias[0][vertice] = -1
        matriz_adyacencias[vertice][0] = -1
        
        fila = matriz_adyacencias[vertice]
                
        for i in range(1, len(fila)):
            if fila[i] != 0:
                matriz_adyacencias = bfs(matriz_adyacencias, i)
            
    return matriz_adyacencias
            
        

if __name__=="__main__":
    k = 5
    archivo = open("RutaMasCorta.txt") #Abrir el archivo
    cadenas = [] #Lista para guardar las cadenas del archivo
    while(True): #Leer el archivo
        linea = archivo.readline()
        if not linea:
            break
        else:
            cadenas.append(linea) 
                
    vertices = (cadenas[0].replace("\n", "")).split(",") #Los vertices son la primer cadena del archivo
    vertice_inicial = vertices[0] #Seleccionar un vertice inicial
    vertice_final = vertices[r.randint(1, len(vertices)-1)] #Seleccionar un vertice final
    
    adyacencias = [] #Agregar las aristas
    for i in range(1, len(cadenas)):
        adyacencias.append(re.split('[:,]',cadenas[i].replace("\n","")))
    
    elegidas = fase_adivinadora(adyacencias)
    respuesta = fase_verificadora(elegidas, k, vertice_inicial, vertice_final, len(vertices))
    
    print("Vertices: ",vertices)
    print("Aristas", adyacencias)
    print ("Elegidas: ",elegidas)  