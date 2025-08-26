print("Bem vindo ao Mercado!")

vtotal = float(input("Por favor indique, qual valor total da sua compra? "))
cc = input("Tem cartão cliente? 'S' ou 'N'? ")           
if cc == "S":
    cc = vtotal - (vtotal * 0.10) 
    print(f"Você tem 10% de desconto! O valor a pagar é{cc: .2f}€")
elif cc == "N" and vtotal >100:
    cc = vtotal - (vtotal * 0.05)
    print(f"Você tem 5% de desconto! O valor a pagar é{cc: .2f}€")
else:
    print(f"Não tem desconto. O valor total da compra é{vtotal: .2f}€") 