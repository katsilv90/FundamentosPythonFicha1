print("Bem vindo ao StarChucks!")

tam = input("Qual o tamanho que deseja? 'P', 'M' ou 'G'? ") # tam = tamanho do copo

vtotal = 0.0
acucar = True

if tam == "P":
    vtotal = 1.5
    print ("O pequeno custa 1,50€.")
elif tam == "M":
    vtotal = 2.0
    print("O médio custa 2.00€.")
else:
    vtotal = 2.5
    print("O grande custa 2.50€.")

decaf = input("Quer descafeinado? São mais 0,30€. 'S' ou 'N'? ")
if decaf == "S":                      # se "S" ou seja Sim
    if tam == "P" or "M" or "G":      # e o tamanho for pequeno ou médio ou grande
        vtotal += 0.3                 # valor do descafeinado   
    else:                             # caso não queira descafeinado
        vtotal == 0.0

leite = input("Quer com leite? Custa mais 0,50€. 'S' ou 'N'? ")
if leite == "S":
    if tam == ("P" or "M" or "G") and (decaf == "S"):
        vtotal += (0.3+0.5)            # 0.3 é o valor do descafeinado
    else:
        vtotal += 0.5                  # apenas valor da soma do café com leite
else:
    vtotal == 0.0                      # café simples sem leite e descafeinado
a = input("Quer açúcar? 'S' ou 'N'? ")  # variável do pedido com açúcar
if a == "S" and acucar:                 # se 'a' e açúcar for verdadeiro
    print(f"O seu pedido é: tamanho - {tam}; descafeinado - {decaf}; leite - {leite}; açúcar? - {a}. São{vtotal: .2f}€ se faz favor.")
else:                                    # se 'a' for falso/ não quer
    print(f"O seu pedido é: tamanho - {tam}; descafeinado - {decaf}; leite - {leite}; açúcar - {a}. São{vtotal: .2f}€ se faz favor.")

