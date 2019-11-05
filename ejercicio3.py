"""
	Progroamacion funcional:
	Funciones puras
	Efectos secundarios
"""
import csv
def lineas(archivo):
	return csv.reader(archivo, delimiter= ";")


with open("data/data-estudiantes.csv") as midata:
	print(list(lineas(midata)))




# midata = open("data/data-estudianes.csv") # en usos de grandes volumenes de 
	# datos es necesario cerrar el archivo 
# midata.close()