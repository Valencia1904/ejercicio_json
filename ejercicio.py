import json
import os

fich=open("becas_premios_0.json")
becas=json.load(fich)
fich.close()

for beca in becas:
	print "Titulo: ",beca["titulo"]
	plazopresentacion=beca["plazopresentacion"]
	plazopresentacion_item=plazopresentacion["plazopresentacion_item"]
	if type(plazopresentacion_item) == list:
		for fecha in plazopresentacion_item:
			print "......................"
			print "Tipo: ",fecha["tipo"]
			print "Fecha inicial: ",fecha["incial"]
			print "Fecha final: ",fecha["final"]
	else:
		print "Fecha inicial: ",plazopresentacion_item["incial"]
		print "Fecha final: ",plazopresentacion_item["final"]
	print "Descripcion"
	print beca["descripcion"]
	print ""
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

raw_input("Pulsa intro para iniciar ejercicio 2")
os.system('clear')

for beca in becas:
	print "Titulo: ",beca["titulo"]
	
	if type(beca["documentacion"]["documentacion_item"]) == list:
		for documentacion in beca["documentacion"]["documentacion_item"]:
			print "Documento: ",documentacion["titulo"]
			print "...................................................."
	else:
		print "Documento",beca["documentacion"]["documentacion_item"]["titulo"]
	
	print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	

