idade = int(input("Quantos anos tem? "))
if idade < 18:
    print("Menor de idade.")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")