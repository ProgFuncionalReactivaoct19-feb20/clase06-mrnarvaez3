"""
	Progroamacion funcional:
	Funciones puras
	Efectos secundarios
"""
import csv

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = ";")


with open("data/data-estudiantes.csv") as midata:
	lineas = list(lineasDiccionario(midata))

	#	obtengo los dos elementos que requiero y le aplico restricciones con .split
	resultado = map(lambda x: "%s-%s"%(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]), lineas)
	
	# salida de datos
	print(list(resultado))