# Algoritmos no determinísticos polinomiales

// Complejidad Computacional
// Melissa Lizbeth Fernández Blancas

Algoritmos de ruta mas corta y 3SAT con fase adivinadora y fase verificadora

Compilar con: python3 <Nombre_archivo>

## Algoritmo de ruta más corta
El programa trabaja dado un archivo txt con un ejemplar de gráfica de la forma:

1,2,3,4,5,6,7,8,9,10  
2,3  
4,5  
8,9  
3,1  
5,1  
7,8  
6,4  
8,3  
6,7  
2,5  
7,4  
9,10

Un número k elegido de forma arbitraria en el programa, el vértice inicial escogido como el primer vértice que aparece en el archivo txt y un vértice final escogido aleatoriamente de los otros vértices dados en el txt.

Al ejecutar el programa se pedirá la ruta del archivo txt que contiene el ejemplar. Si esta ruta no se encuentra, se trabajará con el
archivo "RutaMásCorta.txt".

La salida del programa nos da cuál es el vértice inicial y el final de la trayectoria que buscaremos. Además de la posible trayectoria dada por la fase adivinadora y la salida de la fase verificadora. En caso de que la fase verificadora nos regrese False, se imprimirá la razón por la que fue así.

## Algoritmo del 3SAT
El programa trabaja dado un archivo txt llamado 3sat.txt con una fórmula lógica con la forma:
(x + -y + z) * (x + y + z) * (-x + -y + -z) * (-x + y + -z)

EAl ejecutar el programa se pedirá la ruta del archivo txt que contiene el ejemplar. Si esta ruta no se encuentra, se trabajará con el
archivo "3sat.txt".



