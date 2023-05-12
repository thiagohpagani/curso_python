# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'Thiago Pagani'
print(nome_completo)

soma_dois_mais_dois = 2 + 2

print(nome_completo, soma_dois_mais_dois)

int_um = bool('1')
print(int_um, type(int_um))

nome = 'Thiago'
sobrenome = 'Pagani'
idade = 38
ano_nascimento = 2023 - idade-1
maior_de_idade = idade >= 18
altura = 1.78
print('Nome: ', nome, sobrenome )
print('Sobrenome:', sobrenome)
print('Idade', idade)
print('Ano de Nascimento: ', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura)