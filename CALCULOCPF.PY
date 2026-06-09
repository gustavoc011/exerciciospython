# Pedir ao usuario a entrada dos numeros do cpf a gurda na variavel 
# cpf-original . aqui o usuario digitara o cpf completo
cpf_original = input ("Digite o seu cpf apenas numeros:")
# ajuda contar os numeros do cpf no laço while
i = 0
# guarda os 9 primeiros digitos do cpf
cpf_9 = ""
# Enquanto (while) o valor de i for menor que 9 neste caso ira ate 
# vai pegando um numero por vez no cpf- original (digitado pelo usuario com 11 digitos)
# e vai adicionando um ao lado do outro na variavel cpf-9
# a ideia e obter os 9 primeiros digitos
while i < 9:
    cpf_9+=cpf_original[i]
    i+=1
print(cpf_9)
# para calular o primeiro digito verificador , iremos usar cada numero 
# cpf-9 multiplicado pelo peso que vai de 10 a 2
peso = 10
#  a variavel resultado e utlizada para gurdar a soma do resultado da
# multiplicaçao
resultado = 0
# variavel i e usada para obter um numero por vez do cpf
i = 0
while i < 9:
# A variavel resultado soma os resultado obtidos da multiplicaçao
# dos numeros do cpf com o peso como a variavel cpf-9 e uma cadeia 
# de string sera necessario converter cara numero obtido para inteiro
# com o comando int 
    resultado+=int(cpf_9[i]) * peso 
# peso -=1 que diminuir em 1 o valor do peso passando de 10 para 9 depois
# para 8 e assim por diante ate chegar em 2
    peso -= 1
    #  a variavel i que inicia com 0 deve ser incrementada em 1 (1+=1)para
    #  sair do 0e chegar em 8 assim a cada vez que e laço roda(executada)
    # o valor de i e incrementado em 1 entao ele 1 vai para 1 depois 2 
#  e assim por diante ate chegar em 9(sendo 9 o ponto de saida )
    i+=1
print(resultado)   
# a variavel resto gurda o rsultado do calculo entre o resultado que 
# foi obtido dentro do laço while com numero 11 nesta opraçao estamos
# obtendo o resto da divisao por isso usamos o oprador %
# se o resto da divisao menor que 2  entao o primeiro digite seria 0 
# note que ele esta entre aspas pois queremos 
# juntas com os outros numeros que estao dentro da variavel cpf-9
# que tambem sao chacacteres
#casoo resultado do calculo resulteem numeros acima de 2 
# a subtraçao de 11 por resto que e o resulto que e resultado o calculo para manter
# o valor em formato string estamos usando comando (string)
  
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str (11-resto)
print(cpf_9)    


peso = 11
resultado = 0
i = 0
while i < 10:
    resultado+=int(cpf_9[i]) * peso 
    peso -= 1
    i+=1
print(resultado)    
resto = resultado % 11
if resto < 2:
    cpf_9 += "0"
else:
    cpf_9 += str (11-resto)
print(cpf_9)    

if cpf_9 == cpf_original:
    print("cpf valido")
else:
    print("cpf invalido")    

