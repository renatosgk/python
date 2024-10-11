def menu_principal():
    print("======================")
    print("Bem-Vindo ao Mercado")
    print("1-Frutas")     
    print("2-Legumes")   
    print("3-Temperos")
    print("4-Sair")
    print("======================")

escolha_escolhido = input("Qual dessas opções você gostaria de comprar: ")
compras = []
def escolha_escolhido_1():
    if escolha_escolhido == "1": 
        frutas = ['banana', 'maçã', 'uva', 'pera', 'manga']
        print(*frutas)
        fruta_escolhida = input("Qual dessas fruta você gostaria de comprar?\n ").lower()

    if fruta_escolhida in frutas:
        compras.append(fruta_escolhida)
        print(f"{fruta_escolhida}, foi adicionado no carrinho de compras")

    else:
        print(f"A fruta,{fruta_escolhida} não possui no mercado, lamento")

def escolha_escolhido_2():
    if escolha_escolhido == "2":
        legumes = ['abóbora', 'berinjela', 'chuchu']
        print(*legumes)
        legume_escolhido = input("Qual desses legumes você gostaria de comprar?").lower()

    if legume_escolhido in legumes:
        compras.append(legume_escolhido)
        print(f"O legume,{legume_escolhido}, foi adicionado ao carrinho de compras")

    else:
        print(f"O legume,{legume_escolhido}, não possui no mercado ,lamento")

def escolha_escolhido_3():
    if escolha_escolhido == "3":
        temperos = ["sal", "azeite", "cebolinha", "salsa", "oregano"]
        print(*temperos)
        tempero_escolhido = input("Qual desses temperos você gostaria de comprar? ").lower

    if tempero_escolhido in temperos:
        compras.append(tempero_escolhido)
        print(f"O tempero,{tempero_escolhido}, foi adicionado no carrinho de compras")

    else:
        print(f"O tempero,{tempero_escolhido}, não possui no mercado, lamento")

def escolha_escolhido_4():
    if escolha_escolhido == "4":
        print("Saindo do mercado")





