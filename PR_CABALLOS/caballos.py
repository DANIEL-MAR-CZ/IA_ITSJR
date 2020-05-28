import json
import random

from operator import itemgetter
llaves = [0,0,0,0]
negrosyblancos = [1,1,-1,-1]
movim = [0,0,0,0]
cab = [[0,1],[2,1],[6,-1],[8,-1]]
tab = [[0,0,0],[0,0,0],[0,0,0]]

with open('caballos_pos.json') as file:
	data = json.load(file)

def caballos(data,cab,llaves,movim):
    for t in range(len(cab)):
        for d in data:
            if d[0] == cab[t][0]:
                if (t == 0)and(llaves[0] == 0) and (movim[0] == 0):
                    cab[t][0] = d[1]
                    movim[0] = 1
                    print("Caballo 1")
                    print("Position")
                    print(cab[t][0])
                    tab = tablero(cab[t][0],1)
                    if (cab[t][0]) == 8:
                        llaves[t] = 1
            
                if (t == 1)and(llaves[1] == 0)and (movim[1] == 0):
                    cab[t][0] = d[1]
                    movim[1] = 1
                    print("Caballo 2")
                    print("Position")
                    print(cab[t][0])
                    tab = tablero(cab[t][0],2)
                    if (cab[t][0]) == 6:
                        llaves[t] = 1
                    
                if (t == 2)and(llaves[2] == 0)and (movim[2] == 0):
                    cab[t][0] = d[1]
                    movim[2] = 1
                    print("Caballo 3")
                    print("Position")
                    print(cab[t][0])
                    tab = tablero(cab[t][0],3)
                    if (cab[t][0]) == 2:
                        llaves[t] = 1
                    
                if (t == 3)and(llaves[3] == 0)and (movim[3] == 0):
                    cab[t][0] = d[1]
                    movim[3] = 1
                    print("Caballo 4")
                    print("Position")
                    print(cab[t][0])
                    tab = tablero(cab[t][0],4)
                    if (cab[t][0]) == 0:
                        llaves[t] = 1
    print("posiciones")                
    for t in tab:
        print(t)
    print("Posiciones")

    
    if 0 in llaves:
        movim = [0,0,0,0]
        tab = reseteartablero(tab)
        return caballos(data,cab,llaves,movim)
    else:
        return solucion(cab)

def tablero(posicion,caballo):    
    if posicion==0:
        tab[0][0] = caballo
    if posicion==1:
        tab[0][1] = caballo
    if posicion==2:
        tab[0][2] = caballo
    if posicion==3:
        tab[1][0] = caballo
    if posicion==5:
        tab[1][2] = caballo
    if posicion==6:
        tab[2][0] = caballo
    if posicion==7:
        tab[2][1] = caballo
    if posicion==8:
        tab[2][2] = caballo
    return tab

def reseteartablero(tab):
    for t in range(len(tab)):
        for r in range(len(tab[t])):
            tab[t][r] = 0
    return tab

def solucion(cab):
    print("Resultado")
    
    for c in cab:
        print(c)
    


caballos(data,cab,llaves,movim)
