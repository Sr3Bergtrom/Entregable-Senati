
def longitud ():
    
    dni= input('ingresa el DNI: ')
    if len(dni) != 8:      
        print('deben ser "8" digitos')
        longitud()
    else:
        print('correcto')
        return
        
longitud()





