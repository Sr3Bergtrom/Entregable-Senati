import time

salsa= 56.
rock= 63.
pop= 87.
folclore= 120.5

PrecioSalsa=0
PrecioRock=0
PrecioPop=0
PrecioFolclore=0

CantidadSalsa=0
CantidadRock=0
CantidadPop=0
CantidadFolclore=0

opcion='s'

while opcion == 'si' or opcion== 's' or opcion== 'S':
    print('\n---> que disco desea:\n\t[1]-> salsa\n\t[2]-> rock\n\t[3]-> pop\n\t[4]-> folclore\n')

    disco= input('elija una opcion: ')

    if disco == '1':
        CantidadSalsa= int(input('ud eligio salsa, cuantas unidades desea: '))
        PrecioSalsa= CantidadSalsa*salsa
        print('\npresione enter para terminar la compra')
        opcion= input('escriba [S] para segui comprando: ')

    elif disco == '2':
        CantidadRock= int(input('ud eligio rock, cuantas unidades desea: '))
        PrecioRock= CantidadRock*rock
        print('\npresione enter para terminar la compra')
        opcion= input('escriba [S] para segui comprando: ')

    elif disco == '3':
        CantidadPop= int(input('ud eligio pop, cuantas unidades desea: '))
        PrecioPop= CantidadPop*pop
        print('\npresione enter para terminar la compra')
        opcion= input('escriba [S] para segui comprando: ')

    elif disco == '4':
        CantidadFolclore= int(input('ud eligio folclore, cuantas unidades desea: '))
        PrecioFolclore= CantidadFolclore*folclore
        print('\npresione enter para terminar la compra')
        opcion= input('escriba [S] para segui comprando: ')

    else:
        print('--> elija una opcion valida por favor: ')
        time.sleep(2)

PrecioTotal= PrecioSalsa+PrecioRock+PrecioPop+PrecioFolclore
CantidadTotal= CantidadSalsa+CantidadRock+CantidadPop+CantidadFolclore


if CantidadTotal>=1 and CantidadTotal<=3:
    descuento= round(0,2)

elif CantidadTotal ==4:
    descuento= round(PrecioTotal*0.06,2)

elif CantidadTotal>=5 and CantidadTotal<=10:
    descuento= round(PrecioTotal*0.08,2)

elif CantidadTotal>10:
    descuento= round(PrecioTotal*0.102,2)

PrecioDescuento= PrecioTotal - descuento


if CantidadRock+CantidadPop>6:
    obsequio= 'UN POSTER'
else:
    obsequio= 'NINGUN'



print(f'\nusted compro un total de {CantidadTotal} discos, le corresponde un descuento de {descuento} soles')

print(f'el monto a pagar es de {PrecioDescuento} soles, y le corresponde {obsequio} obsequio')





 


