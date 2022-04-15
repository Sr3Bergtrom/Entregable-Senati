
InvP1= int(input('ingrese la inversion de la primera persona: '))
InvP2= int(input('ingrese la inversion de la segunda persona: '))
InvP3= int(input('ingrese la inversion de la tercera persona: '))

P1= round((InvP1/(InvP1+InvP2+InvP3)*100),1)
P2= round((InvP2/(InvP1+InvP2+InvP3)*100),1)
P3= round((InvP3/(InvP1+InvP2+InvP3)*100),1)

print(f'\nel porcentaje de inversion de la primera persona es: {P1}%')
print(f'el porcentaje de inversion de la segunda persona es: {P2}%')
print(f'el porcentaje de inversion de la tercera persona es: {P3}%')
