frase = 'O Python é uma linguagem de programação'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu = ''
while i < len(frase):
    letra_atual = frase[i]
    qt_apareceu_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qt_apareceu_atual:
        qtd_apareceu_mais_vezes = qt_apareceu_atual
        letra_apareceu = letra_atual
  
    i += 1

print(f'A letra que apareceu mais vezes foi "{letra_apareceu}" que apareceu {qtd_apareceu_mais_vezes}')