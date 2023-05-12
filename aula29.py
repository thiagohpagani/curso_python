numero = input('Dobro do seu numero: ')

try:
   
    numero_float = float(numero)
    print('Float:', numero_float)
    print(f'O dobro de {numero} é {numero_float *2:.2f}')
except:
    print('Isso não é um número')
