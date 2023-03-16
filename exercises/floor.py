# eufloor = input('what floor are you in Europe? ' )
# usafloor = int(eufloor) + 1
# print(f'You are in the equivalent to floor ',usafloor,' in USA')

# name = input("whats your name? " )
# print("wellcome,", name)

# num = 1
# nume = 25
# if num < 10 and nume > 20:
#     print('yes')
# else:
#     print('no')


### EX 3.1
# horas = 45
# euros = 6
# paga = horas * euros
# if horas > 40:
#     paga = 40 * euros + (horas - 40) * (1.5 * euros) 
# print(paga)

### EX 3.2
horas = input("horas de trabajo? ")
try:
    horas = float(horas)
except:
    print("mete numeros pelele")
    horas = -1

euros = input("a cuanto la hora? ")
try:
    euros = float(euros)
except:
    print("mete numeros pelele")
    euros = -1

paga = 0
if horas < 0 or euros < 0:
    print('haz el favor de meter numeros positivos en todos los parametros')
elif horas <= 40:
    paga = horas * euros
    print(paga,' euros de paga')
else:
    paga = 40 * euros + (horas - 40) * (1.5 * euros) 
    print(paga,' euros de paga')