palavras = ["casa", "árvore", "elefante", "bola", "uva", "ovo", "mesa"] 

vogais = ("a","e","i","o","u","á")

for vogal in palavras:           # percorre cada palavra da lista 'palavras'
    if vogal[0] in vogais:      # vogal[0] acede ao primeiro caracter de cada posição da lista 'palavra'     se 'vogal' se encontra na lista 'vogais'
        print(vogal)