def desconto(preco=0.0, taxa=0.0):

    """A funçao desconta calcula o valor de
 desconto de um determinado preço """
    return preco * taxa / 100

rs = desconto(550,4.2)
print(f"O valor de desconto e {rs}")    
 