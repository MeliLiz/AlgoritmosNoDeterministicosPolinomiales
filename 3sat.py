import random

def fase_adivinadora(variables):
    for variable in variables:
        rand = random.choice([True, False])
        if rand:
            variables[variable] = True
    
    return variables

def fase_verificadora(clausulas, diccionario):
    for clausula in clausulas:
        romper = False
        for variable in clausula:
            if variable[0] == "-": # La variable esta negada
                if diccionario[variable[1:]] == False:
                    romper = True
                    break # La clausula es verdadera
            else: # La variable no esta negada
                if variables[variable]:
                    romper = True
                    break # La clausula es verdadera
        if not romper:
            return False      
    return True
    
# Funcion que devuelve un diccionario con las variables y su valor (False)
def vars(clausulas):
    variables = {}
    for clausula in clausulas:
        for variable in clausula:
            variable = variable.replace("-", "")
            if variable not in variables:
                variables[variable] = False
    return variables

if __name__=="__main__":
    archivo = open("3sat.txt") #Abrir el archivo
    
    clausulas = (archivo.readline()).strip().replace("(", "").replace(")", "").split("*")
    
    for i in range(len(clausulas)):
        clausulas[i] = clausulas[i].split("+")
        
    variables = vars(clausulas)
    asignacion_vars = fase_adivinadora(variables)
        
    print(clausulas)
    
    