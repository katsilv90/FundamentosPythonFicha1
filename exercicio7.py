print("Avaliação Escolar")

n1 = int(input("Introduz de 0 a 20 a nota nº1: "))
n2 = int(input("Introduz de 0 a 20 a nota nº2: "))
n3 = int(input("Introduz de 0 a 20 a nota nº3: "))

media = (n1 + n2 + n3) // 3      # // para ter resultado da divisão int em vez de float

print(f"A média é {media} valores.")

if media < 10:
    print("Reprovado")
elif media < 14:
    print("Suficiente")
elif media < 16:
    print("Bom")
elif media < 18:
    print("Muito Bom")
else:
    print("Excelente")