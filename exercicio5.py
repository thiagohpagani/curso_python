"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    resto_int = entrada_int % 2 ==0
    print(resto_int)
    if resto_int:
        print('Número PAR')
    else:
        print('Número IMPAR')

else:
    print('Você não digitou um número inteiro')

print(10 * '-')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada_hora = input('Digite a hora atual: ')

try:
    hora_int = int(entrada_hora)
    if hora_int <= 11:
        print('Bom dia')
    elif hora_int <= 17:
        print('Boa tarde')
    else:
        print('Boa noite')
except:
    ...

print(10 * '-')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome é curto')
elif tamanho_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')

print(f'Total de Letras no nome é: {tamanho_nome}')