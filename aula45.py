"""
Interável -> str, range, etc (método (__inter__) objeto)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próprio valor
inter -> me entregue seu iterador

"""
#texto = iter('Thiago') #__iter__()
#print(texto)

texto ='Luiz' #iterável

for letra in texto:
    print(letra)