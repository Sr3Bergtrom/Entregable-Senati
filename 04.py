n1 = int(input("ingresa el numero: "))
n2 = int(input("ingresa el numero: "))
operacion = input("que operacion?: ")

if operacion == "+":
	print(n1 + n2)
elif operacion == "-":
	print(n1 - n2)
elif operacion == "*":
	print(n1 * n2)
elif operacion == "/":
	print(n1 / n2)
else:
	print("elija una operacion correcta")
