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
	
raw_input("Pulsa intro para iniciar ejercicio 3")
os.system('clear')


abiertas = 0
cerradas = 0

for beca in becas:
	if beca["estado"] == "Cerrado":
		cerradas = cerradas+1
	elif beca["estado"] == "Abierto plazo de solicitud" or beca["estado"] == "En Plazo de Solicitud":
		abiertas = abiertas+1


print "Abiertas:",abiertas
print "Cerradas:",cerradas

raw_input("Pulsa intro para iniciar ejercicio 4")
os.system('clear')

taxionomia = raw_input("Por que taxonomia desea filtrar: ").lower()

for beca in becas:
	if type(beca["taxonomias"]["taxonomia_item"]) == list:
		for taxi in beca["taxonomias"]["taxonomia_item"]:
			if taxionomia in taxi["nombre"].lower():
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

	else:
		if taxionomia in beca["taxonomias"]["taxonomia_item"]["nombre"].lower():
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






raw_input("Pulsa intro para iniciar ejercicio 5")
os.system('clear')

fecha=raw_input("Dame una fecha con formato(YYYY-MM-DD): ")
fecha=fecha.split("-")

for beca in becas:
	
	plazopresentacion=beca["plazopresentacion"]
	plazopresentacion_item=plazopresentacion["plazopresentacion_item"]
	if type(plazopresentacion_item) == list:
		
		for i in plazopresentacion_item:
			if str(type(i["final"])) == "unicode":
				fecha2=i["final"]
				fecha2=fecha2.split("T")
				fecha2=fecha2[0].split("-")
				
				if fecha2[0] >= fecha[0]:
					if fecha2[1] >= fecha[1]:
						if fecha2[2] >= fecha[2]:
							
							print "Titulo: ",beca["titulo"]
							print "Tipo: ",i["tipo"]
							print "Fecha inicial: ",i["incial"]
							print "Fecha final: ",i["final"]
							print "Descripcion"
							print beca["descripcion"]
							print ""
							print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	

	else:
		if str(type(plazopresentacion_item["final"])) == "unicode":
			fecha2 = plazopresentacion_item["final"]
			fecha2=fecha2.split("T")
			fecha2=fecha2[0].split("-")
			
			if fecha2[0] >= fecha[0]:
				if fecha2[1] >= fecha[1]:
					if fecha2[2] >= fecha[2]:
						print "Titulo: ",beca["titulo"]
						print "Tipo: ",plazopresentacion_item["tipo"]
						print "Fecha inicial: ",plazopresentacion_item["incial"]
						print "Fecha final: ",plazopresentacion_item["final"]
						print "Descripcion"
						print beca["descripcion"]
						print ""
						print "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
