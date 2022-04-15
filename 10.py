 def salario():

 	horas = int(input("numero de horas trabajadas: "))
 	turno = input("ingresa el turno: ")

 	if turno == "mañana":
 		pago = horas * 37.0
 		print(f"tu salario es: {pago}")

 	elif turno == "tarde":
 		pago = horas * (37.0 + 1.20)
 		print(f"tu salario es: {pago}")

 	elif turno == "noche":
 		pago = horas * (37.0 + 1.50)
 		if pago >= 2000 and pago <= 5000:
 			print(f"tu salario es: {pago - (pago * (15/100))} incluye el descuento de 15%")

 		elif pago  >= 8000 and pago <= 10000:
 			print(f"tu salario es: {pago - (pago * (17/100))} incluye el descuento de 17%")

 		else:
 			print("tu salario es: ", pago)

 salario()


