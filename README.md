# Algoritmos no deterministicos polinomiales
Algoritmos de ruta mas corta y 3SAT con fase adivinadora y fase verificadora

Compitar con: python3 <Nombre_archivo>

## Algoritmo de ruta más corta
El programa trabaja dado un archivo txt nombrado RutaMasCorta.txt con un ejemplar de gráfica de la forma:

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
El archivo que acepta el programa se debe llamar  "RutaMásCorta.txt".

## Algoritmo del 3SAT
El programa trabaja dado un archivo txt llamado 3sat.txt con una fórmula lógica con la forma:
(x + -y + z) * (x + y + z) * (-x + -y + -z) * (-x + y + -z)

El archivo que acepta el programa se debe llamar "3sat.txt"



