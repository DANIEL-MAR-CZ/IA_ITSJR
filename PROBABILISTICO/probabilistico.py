

#Daniel Margarito Cruz

import json

clasificacion = [0,0,0]
pdef = [0,0,0]
porc = [0,0,0]
tipo = ""
c = 0

with open('base.json') as file:
	data = json.load(file)
S = input("Introduce el nombre")
for d in data["defecto"]:

	if d['nombre'] == S.lower():
		print(d['nombre'])
		pdef[0] = d['puntaje']['Ave']
		pdef[1] = d['puntaje']['Reptil']
		pdef[2] = d['puntaje']['Mamifero']
		
		index = pdef.index(max(pdef, key=int))
		max_item = max(pdef, key=int)
		
		if index == 0:
			clasificacion[index] = clasificacion[index] + max_item
		if index == 1:
			clasificacion[index] = clasificacion[index] + max_item
		if index == 2:
			clasificacion[index] = clasificacion[index] + max_item
				
			
	
for pregunta in data['Nodo']:
	
	Animal= input("")
	print('Tiene o puede ?')
	print(pregunta[1])
	R = input("")
	if R == "S":
		clasificacion[0] = clasificacion[0] + int(pregunta[2]["Ave"])
		clasificacion[1] = clasificacion[1] + int(pregunta[2]["Reptil"])
		clasificacion[2] = clasificacion[2] + int(pregunta[2]["Mamifero"])
	index = clasificacion.index(max(clasificacion, key=int))
	max_item = max(clasificacion, key=int)
	porc[0] = clasificacion[0]
		
	print(tipo)
		
	for t in pregunta[2]:
		"""print("tipo :"+t+" index :"+str(c))"""
		if index == c:
			tipo = t
		c=c+1
	c=0
print("Es un :"+" "+tipo+" Con un puntade de: "+str(max_item)) 
porc[0] = (clasificacion[0]/(clasificacion[0]+clasificacion[1]+clasificacion[2]) )*100
porc[1] = (clasificacion[1]/(clasificacion[0]+clasificacion[1]+clasificacion[2]) )*100
porc[2] = (clasificacion[2]/(clasificacion[0]+clasificacion[1]+clasificacion[2]) )*100
		
print("puntajes totales:  | Aves :"+str(clasificacion[0])+" | Reptiles :"+str(clasificacion[1])+" | Mamiferos :"+str(clasificacion[2])+"|")
print("porcentajes totales:  | Aves :"+str(porc[0])+"%"+" | Reptiles :"+str(porc[1])+"%"+" | Mamiferos :"+str(porc[2])+"%"+"|")
