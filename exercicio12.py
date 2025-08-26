notas_turma = [[85, 90, 78], [92, 88, 76, 95], [80, 85, 90, 87, 82]]

turma = 0

for notas in notas_turma:   #percorre sub-listas dentro da lista 'notas_turma'
    soma = 0                #inicia soma das notas da turma atual

    for nota in notas:      #dentro de cada sub-lista soma valores
        soma += nota
    media = soma // len(notas)    #   // divisão inteira em vez de decimal
    turma += 1                    # turma 0 passa para turma 1, turma 2 passa para turma 2, etc.

    print(f"Média da Turma {turma}: {media} valores.")
    