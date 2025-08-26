
print("Boa noite!")

concerto = input("Tem bilhete para o concerto? 'S' ou 'N'? ")
if concerto == "S":
    print("Pode entrar.")
else:
    convite = input("Tem convite? 'S' ou 'N'? ")
    if convite == "S":
        print("Pode entrar.")
    else:
        print("Não pode entrar.")