num = [45,12,78,23,56,89,34] #45 é a posição 0

maior = num[0]    #  [0] = a posição é 0

for numero in num:
    if numero > maior:       #se 'numero' da posição for maior que a posição do 'maior', troca de posição   ex: 45>12 (não troca), 45>78 (troca)
        maior = numero       #se for maior atualiza-se a variável 'maior'
print(f"O maior número da lista é {maior}.")
