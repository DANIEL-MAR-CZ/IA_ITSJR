
#Daniel Margarito Cruz
import json
import random
from operator import itemgetter

with open('base.json') as file:
	data = json.load(file)
ruta=[]
camino=[]
auxiliar = []
def subidadelacolina(inicial,objetivo,anterior):
	ruta.append(inicial)
	print("Inicio: "+inicial)
	print("Anterior: "+anterior)#
	if auxiliar:
		del auxiliar[:]
		del camino[:]
	if objetivo == inicial:
		print("Point Encontrado")
		return inicial
	if anterior == "":
		anterior = inicial
	for a in data:
		if a[0] == inicial:
			if anterior != "":
				if a[1] != anterior:
					camino.append(a)
	print("Extración de la lista menor de la Lista")
	print(min(camino, key=itemgetter(2))[:])
	print (camino)
	minimo = (min(camino, key=itemgetter(2))[2])
	for b in camino:
		if b[2] == minimo:
			auxiliar.append(b)
	print("Camino menor")
	print(auxiliar)
	cont = 0
	#Can use
	for c in auxiliar:
		cont += 1
		if cont > 1:
			r = random.random()
			print("Aleatoriedad de los caminos")
			if r < 0.5:
				auxiliar.pop()
			else: 
				auxiliar.pop(0)
		else:
			print(auxiliar) #end
	if auxiliar:
		for n in auxiliar:
			print("Punto Siguiente")
			print(n[1])
			return subidadelacolina(n[1],objetivo,inicial)
arch=subidadelacolina("Z","I","")
if arch:
	print(arch)
	print("FOUND ROUTE")
	print(ruta)
