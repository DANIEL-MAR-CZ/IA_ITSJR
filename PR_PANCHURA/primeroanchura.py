"""
Cada funcion recibe la Carpeta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra 
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo):
	pass
"""
import json
with open('base.json') as file:
	data = json.load(file)
#lista para ruta
ruta=[]

visitados=[]

v=[]

sig=[]
	
def primeroAnchura(Carpeta,Archivo):
	print("...............................")
	if sig:

			contH=0
			print("prox nodos a verificar")
			print(sig)
			for s in sig:
				contH = contH +1 
			if contH > 1:
				print("nodo actual")
				print(sig[0])
				del sig[0] 
				
	if v:
		del v[:]
	if Carpeta == Archivo:
		return Archivo
	for d in data:
		if d[0] == Carpeta:
			print(d[0]+"/"+d[1])
			v.append(d[0])
			sig.append(d[1])
			if d[1] == Archivo:
				arch = primeroAnchura(d[1],Archivo)
				if arch:
					return arch
	
	visitados.append(list(set(v)))
	if visitados:
		print("visitados "+str(visitados))
		print("nodo siguiente ")
		print(sig[0])
		ruta.append(sig[0])
		print(".....................................")
		return primeroAnchura(sig[0],Archivo)


	
arch=primeroAnchura("A","M")
print("Nodo encontrado")
print(arch)
rt = []
if arch:
	for r in ruta:
			if r not in rt:
				rt.append(r)
	print("Nodos visitados")
	print(rt)
else:
	print("No existe")
