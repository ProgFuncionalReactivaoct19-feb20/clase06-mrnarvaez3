"""
	Progroamacion funcional:
	Funciones puras
	Efectos secundarios
	- Filtrar los registros cuyos países tengan en su nombre una longitud mayor a 10

	- Ordenar la lista en función del día de nacimiento.
"""
import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = "\t")


with open("data/trabajadores.csv") as midata:
	lineas =list(lineasDiccionario(midata))

	#  obtengo la posicion del nombre de los paises y luego hago la condicion
	paises = filter(lambda x: len(list(x.items())[2][1])>10, lineas)
	print("Listado cuyos nombres del pais son mayores a 10 digitos:\n",list(paises))

	#  entro a la posicion de la fecha, seguidamente al dia y le aplico el sorted
	ordenado = sorted(lineas, key = lambda x: list(x.items())[1][1].split("-")[2])
	print("Listado en funcion del dia de nacimiento: \n",list(ordenado))