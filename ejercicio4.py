"""
	Progroamacion funcional:
	Funciones puras
	Efectos secundarios
"""
import csv
def lineas(archivo):
	return csv.reader(archivo, delimiter= ";")


with open("data/data-estudiantes.csv") as midata:
	#  obtengo unicamente los emails de cada linea
	resultado = map(lambda x: x[1], (lineas(midata)))	
	#resultado2 = filter(lambda x: x != "email", resultado)

	#  hago la filtracion y presento datos
	print(list(filter(lambda x: x!= "email",resultado)))