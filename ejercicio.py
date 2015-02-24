import json

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
	print "----------------------------------------------------------------"
