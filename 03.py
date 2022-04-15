
nombre= input('ingrese el nombre: ')
horas_trabajo= float(input('ingrese las horas de trabajo: '))
salario_hora= float(input('ingrese el salario por hora: '))

sueldo= horas_trabajo*salario_hora
sueldo+= 0.15*sueldo

print(f'\nel sueldo de {nombre} es:  {sueldo} soles')

