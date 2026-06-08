# vamos usar uma varivel chamada nome para
# guarda o nome do cliente. Utilizaremos tambem
# o comando input(in dentro / put por em algum lugar)
nome = input("Digite o seu nome:")
print("Ola, Sr(a)."+nome)
print(f"ola, Sr(a).{nome}")
# o oprador + foi ultilizado para 
# concatenar(juntar) o texto entre aspas("")
# com a variavel nome
print("Ola, Sr(a)."+nome+". Seja bem vindo")
# abaixo, usamos o comando print com a letra
# f(forma) para inserir uma variavel no meio
# de uma string. A variavel foi inserida com chaves({})
# esta tecnica e chamada de interpolaçao
print(f"ola, Sr(a).{nome}. Seja bem vindo")