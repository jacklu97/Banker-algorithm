# Luis Angel Hernández Hernández
# Seminario de sistemas operativos
# Algoritmo del banquero

import numpy as np

def comprobar_data(necesarios, disponibles, asignados):
    meta = len(disponibles)
    terminados = []
    i = 0
    while(i < len(necesarios)):
        if(np.sum(np.less_equal(necesarios[i], disponibles)) == meta and i not in terminados):
            print("El proceso {} ha sido terminado".format(i))
            disponibles = np.sum([disponibles, asignados[i]], axis=0)
            print("Recursos disponibles: ", disponibles, "\n")
            terminados.append(i)
            i = 0
        else:
            i+=1
        
    return "Se ha completado el proceso correctamente." if len(terminados) == len(necesarios) else "Se ha producido un interbloqueo."
    
asignados = np.matrix( 
    '0 0 1 2; 1 0 0 0; 1 3 5 4; 0 6 3 2; 0 0 1 4'
)

maximos = np.matrix(
    '0 0 1 2; 1 7 5 0; 2 3 5 6; 0 6 5 2; 0 6 5 6'
)
necesarios = np.subtract(maximos, asignados)

disponibles = np.array([1,5,2,0])

print(comprobar_data(necesarios, disponibles, asignados))