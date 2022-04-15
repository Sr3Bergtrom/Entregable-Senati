#primero declaramos algunas funciones que luego utilisaremos
def elegir (c):
    if c == '1':
        return 'salsa'
    elif c == '2':
        return 'rock'
    elif c == '3':
        return 'pop'
    elif c == '4':
        return 'folklore'

diccionario= {'salsa':56.,'rock':63.,'pop':87.,'folklore':120.5}

def precio (disco,cantidad):
    return cantidad*disco

def descuento (porcentaje,monto):
    return porcentaje*monto/100

#inprimimos y pedimos las opciones de compra
print('\n---> que disco desea:\n\t[1]-> salsa\n\t[2]-> rock\n\t[3]-> pop\n\t[4]-> folklore\n\t[5]-> Finalisar Compra\n')
opcion= input('elija una opcion: ')
cantidad= int(input('cuantas unidades desea: '))

#calculamos el monto a pagar
disco= elegir(opcion)
print(f'\nusted compro {cantidad} discos de {disco}')
PrecioDisco= diccionario[disco]
monto= precio(PrecioDisco,cantidad)
print(f'el precio original debio ser: {monto} soles')

#aqui calculamos el descuento
porcentaje = 0
if cantidad>=1 and cantidad<=3:
    porcentaje= 0
elif cantidad ==4:
    porcentaje= 6.2
elif cantidad>=5 and cantidad<=10:
    porcentaje= 8.2
elif cantidad>10:
    porcentaje= 10.2
descuento= round(descuento(porcentaje,monto),1)
print(f'le corresponde un descuento de {descuento} soles')

#hallamos el monto final
PrecioPago= monto - descuento
print(f'\nsu monto a pagar es: {PrecioPago} soles')

#aca vemos si hay obsequio o no
if (disco == 'rock' or disco == 'pop') and cantidad>6:
    print(f'felicitaciones se lleva UN POSTER :)\n')
else:
    print(f'no le corresponde NINGUN POSTER :(\n')




