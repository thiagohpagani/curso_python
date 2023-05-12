""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*) ')
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os números figitados são inválidos')
        continue

    operadores_perm = '+-/*'
    if operador not in operadores_perm:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    
    print('Resultado, confira abaixo:')
    ###
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=',num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=',num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=',num_1_float / num_2_float)
    else:
        print('Não deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)
    if sair is True:
        break