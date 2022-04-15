print("\n__________________________________________________________________________________________________________")
print("\n----------------------------------------------------------------------------------------------------------")
print()
print("                                           Bienvenid@ al interfaz del trabajador")
print()
print("                             Mediante ésta sesión, usted conocerá más detalles sobre su salario")
print()
print("\n__________________________________________________________________________________________________________")
print("\n----------------------------------------------------------------------------------------------------------")
print()


horas = int(input("         Horas laborales: "))
print()
turno = input("         Tipo de turno(mañana, tarde, noche): ")
print()

salario = horas*37

if turno=="mañana":
    salario==horas*37

elif turno=="tarde":
    salario+=salario*0.2

elif turno=="noche":
    salario+=salario*0.5

if salario>=200 and salario<=500:
    salario-=salario*0.15

elif salario >=800 and salario<=1000:
    salario*=salario*0.17

print("         El salario que le corresponde es de S/:",salario)
print()
print("\n__________________________________________________________________________________________________________")
print("\n----------------------------------------------------------------------------------------------------------")
print()
print("                                             Gracias por trabajar con nosotros")
print()
print("\n__________________________________________________________________________________________________________")
print("\n----------------------------------------------------------------------------------------------------------")
print()