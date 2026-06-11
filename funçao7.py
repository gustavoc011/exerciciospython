def acrescimo(preco:float,taxa:float):
    """A funçao acrecimo realiza o calculo de aumento 
    do valor do preço do produto de acordo com a taxa

    Args:
    preco(float) passe o preço do produto
    taxa(float): passe a taxa do acrescimo somente numero
    returne:
   float:retorna o do produto com o valor de acrescimo

    """
    return preco * (1+taxa) / 100
rs =acrescimo(3000.50, 7.7)

print(f"o valor final do produto {rs}")

