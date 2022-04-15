numero1= float(input('ingresa el primer numero: '))
numero2= float(input('ingresa el segundo numero: '))
numero3= float(input('ingresa el tercer numero: '))


if numero1 > numero2 and numero1 > numero3:
    print(numero1)
    
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
    
else:
    print(numero3)
    
