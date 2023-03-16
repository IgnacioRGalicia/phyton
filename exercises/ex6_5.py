print('Ex 06.05')

str = 'X-DSPAM-Confidence: 0.0231'
print(str)

dospuntos = str.find(':')
print(dospuntos)

numero = str[dospuntos+2:]
print('numero es:', numero)

valor = float(numero)
print(type(valor))