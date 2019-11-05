"""
	Progroamacion funcional:
	Funciones puras
	Efectos secundarios
"""
import csv

# def lineas(archivo):
#	return csv.reader(archivo, delimiter = ";")

def lineasDiccionario(archivo):
	return csv.DictReader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
	lineas = lineasDiccionario(midata)

	resultado = map(lambda x: list(x.items())[0][1], lineas)
	print(list(resultado))



	#print(list(lineasDiccionario(midata)))