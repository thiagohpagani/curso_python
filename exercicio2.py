pri_valor = input('Digite um valor: ')
seg_valor = input('Digite outro valor: ')

if pri_valor > seg_valor:
    print(f'{pri_valor=} é maior do que o {seg_valor=}')
elif seg_valor > pri_valor:
    print(f'{seg_valor=} é maior do que o{pri_valor=}')
else:
    print('Os valores são iguais')   
