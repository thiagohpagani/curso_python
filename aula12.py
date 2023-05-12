nome = 'Thiago Pagani'
altura = float(1.80)
peso = 85
imc = peso / (altura*altura) # ... -> Ellipsis (Place Holder) um codigo que ainda nao foi escrito
linha_1 = f'{nome} tem {altura:.2f} de altura' #f-strings usado para adicionar variaveis em uma string
linha_2 = f'pesa {peso} quilos e seu IMC é: {imc:.2f}'
print(linha_1)
print(linha_2)