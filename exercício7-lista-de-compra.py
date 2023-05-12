import os

lista_compra = []
opcao_escolhida =''

while True:
    print('Selecione uma opção')
    opcao_escolhida = input('[i]nserir [a]pagar [l]istar [s]air: ')
    
    if opcao_escolhida == 'i':
        os.system('cls')
        produto_lista = input('Insira o produto na lista: ')
        lista_compra.append(produto_lista)

    elif opcao_escolhida == 'a':
        os.system('cls')
        if len(lista_compra) == 0:
            print('Não Existe itens para serem apagados')
        else:
            for i, produto_lista in enumerate(lista_compra):
                print(i, produto_lista)
            indice_str = input('Escolha o íncice para apagar:')
        try:
            indice = int(indice_str)
            del lista_compra[indice]
        except:
            print('O índice escolhido não existe')


    elif opcao_escolhida == 'l':
        os.system('cls')
        if len(lista_compra) == 0:
            print('Não Existe itens na lista')

        for i, produto_lista in enumerate(lista_compra):
            print(i, produto_lista)
    
    elif opcao_escolhida == 's':
        break