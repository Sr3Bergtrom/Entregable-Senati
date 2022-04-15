import math

def musica():
	disco = input("ingresa el disco que quieres: ")
	cantidad = int(input("ingresa la cantidad: "))
	if cantidad <= 0:
		print("selecciona una opcion correcta por favor")
		return
	poster = 0

	dvd = {
		"salsa": 56.00,
		"rock": 63.00,
		"pop": 87.00,
		"folclore": 120.00
	}

	desc = {
		"a": [ range(1,4), 1 , "ninguno" ],
		"b": [ [4], 6/100, "6.0%" ],
		"c": [ range(5,11), 8/100, "8.0%" ],
		"d": [ range(10, cantidad + 1), 10.2/100, "10.2%"]
	}

	precio1 = dvd[disco] * cantidad

	for i in desc:
		if cantidad in desc[i][0]:
			total = round( precio1 * desc[i][1], 2 )
			descuento = desc[i][2]
			poster = 1 if cantidad > 5 and disco in ["rock", "pop"] else 0


	print(
"""\n precio1 normal: {}
cantidad: {}
descuento: {}
total: {}
poster: {}""".format(precio1, cantidad, descuento, total, poster))

musica()


	
