print("\nBem vindo à nossa loja!\n")

produtos = ["café", "farinha", "batatas"]

unidades = [10,5,8]

inicio = True
                                                                 
print("\n***LISTA DE PRODUTOS***\n")
for qt_prod in range(len(produtos)):
    print(f"{(produtos[qt_prod])}: {unidades[qt_prod]} unidades.")  
    
while inicio:                                                               # início do loop principal
    des = input("\nEscolha de (1-4) uma das seguintes opções:\n1 - Vender produto\n2 - Repor stock\n3 - Consultar stock\n4 - Sair\nEscolha: ")

    # VENDER PRODUTO
    inicio = False                                                          # if false continua o código
    if des == "1":                                                         
        print("\n\n***VENDER PRODUTO***\n")
        prod = input("Escolha de (1-3) uma das seguintes opções:\n1 - café\n2 - farinha\n3 - batatas\nEscolha: ")    #prod = produto
        if prod == "1":                                                     # produto café ---- início             
            quantidade = int(input("Quantas unidades que vender? "))        # [0] posição do café e do 10 nas listas
            if quantidade <= unidades[0]:                                   # se quantidade do input for <= que 10 (na posição [0])
                unidades[0] -= quantidade                                   # então 10 - input(quantidade)
                print(f"{(produtos[0])}: {(unidades[0])} unidades.")                                                          
            else:                                                           # se for maior que 10 (valor que está na posição [0]) a conta fica negativa por isso dá erro
                print("\nErro! Stock Insuficiente!")                         # produto café ----- fim
                                                                                                                                                                                                                      
        elif prod == "2":                                                   # produto farinha ---- início
            quantidade = int(input("Quantas unidades que vender? "))         
            if quantidade <= unidades[1]:                                   # [1] posição da farinha e do 5 nas listas
                unidades[1] -= quantidade
                print(f"{(produtos[1])}: {(unidades[1])} unidades.")                                  
            else:
                print("\nErro! Stock Insuficiente!")                         # produto farinha ---- fim
                                                                                                        
        elif prod == "3":                                                   # produto batatas ----- início
            quantidade = int(input("Quantas unidades que vender? "))
            if quantidade <= unidades[2]:                                   # [2] posição das batatas e do 8 nas listas
                unidades[2] -= quantidade
                print(f"{(produtos[2])}: {(unidades[2])} unidades.")        # produto batatas -----fim         
            else:
                print("\nErro! Stock Insuficiente!")                                                                                      
        else:
            print("\nErro! Produto não existe!")
        inicio = True 

    # REPOR PRODUTO
    elif des == "2":                                                         
        print("\n\n***REPOR PRODUTO***\n")
        prod = input("Escolha de (1-3) uma das seguintes opções:\n1 - café\n2 - farinha\n3 - batatas\nEscolha: ")    #prod = produto

        if prod == "1":                                                     # produto café ---- início           
            quantidade = int(input("Quantas unidades que repor? "))                                               
            unidades[0] += quantidade                                   
            print(f"{(produtos[0])}: {(unidades[0])} unidades.")            # produto café --- fim                                                              

        elif prod == "2":                                                   # produto farinha ---- início            
            quantidade = int(input("Quantas unidades que repor? "))                                               
            unidades[1] += quantidade                                   
            print(f"{(produtos[1])}: {(unidades[1])} unidades.")            # produto farinha ---- fim                                                                     

        elif prod == "3":                                                   # produto batatas ---- início            
            quantidade = int(input("Quantas unidades que repor? "))                                               
            unidades[2] += quantidade                                   
            print(f"{(produtos[2])}: {(unidades[2])} unidades.")            # produto batatas ---- fim   
        else:
            print("\nErro! Produto não existe!")
        inicio = True 
        
    # CONSULTAR STOCK
    elif des == "3":
        print("\n\n***CONSULTA DE STOCK***\n")
        for qt_prod in range(len(produtos)):
            print(f"{(produtos[qt_prod])}: {unidades[qt_prod]} unidades.")
        inicio = True 
    
    # SAIR
    elif des =="4":
        print("\n\n***SAIR***\n")
        sair = input("Deseja sair do programa? S/N? ")
        if sair == "N" or sair == "n":
            inicio = True 
        elif sair == "S" or sair == "s":
            print("\nEncerrou o programa\n")
            inicio = False                                                                      
        else:
            print("\nErro de input\n")
            inicio = True 
    else:
         print("\nEscolha inválida! Digite um número de 1 a 4.\n")
         inicio = True
    


