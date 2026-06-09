palavra = input("Digite um texto")
# O comando len (length = comprimento) ou seja ,
# conta a quantidade de caracteres em uma
# coleçao
qtd_palavra =len(palavra)
print(qtd_palavra)
cont = 0
while cont < qtd_palavra:
    print(f"A {cont+1} a letra e {palavra[cont]}")
    cont+=1