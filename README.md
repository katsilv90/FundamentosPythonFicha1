# FundamentosPythonFicha1
Ficha 1 
 
1 - Pede ao utilizador para introduzir um número inteiro e um número decimal. 
Depois: 
• imprime o tipo de cada variável 
• converte o inteiro para float e o float para inteiro e imprime o resultado das 
conversões. 

2 - Pede ao utilizador a sua idade e imprime: 
• "Menor de idade" se tiver menos de 18 anos 
• "Adulto" se tiver entre 18 e 64 anos 
• "Idoso" se tiver 65 ou mais anos 

3 - Simula uma entrada para um concerto: 
• Pergunta se a pessoa tem bilhete ou se é convidada. 
• Se uma das respostas for afirmativa, imprime "Pode entrar". 
• Caso contrário, imprime "Não pode entrar". 

4 - Cria um pequeno sistema de cálculo de desconto: 
1. Pede o valor total da compra. 
2. Pergunta se o utilizador tem cartão de cliente (S/N). 
3. Se tiver cartão, aplica 10% de desconto. 
4. Se não tiver cartão, aplica 5% de desconto para compras superiores a 100 
euros; caso contrário, sem desconto. 
5. Mostra o valor final a pagar.

   
5 - Sistema de encomenda de café 
1. Pede ao utilizador para escolher: 
o Tamanho: P, M, G 
o Tipo de café: normal ou descafeinado 
o Com ou sem leite 
o Com ou sem açúcar 
2. Calcula o preço com base nas regras: 
o P: 1.5 €, M: 2 €, G: 2.5 € 
o Descafeinado: +0.3 € 
o Leite: +0.5 € 
o Açúcar: +0 € (grátis) 
3. Mostra o resumo da encomenda e o preço total. 

6 - Planeador de viagem 
1. Pede ao utilizador para indicar: 
o Distância da viagem em km. 
o Consumo médio do carro (litros/100km). 
o Preço atual do combustível por litro. 
2. Calcula: 
o Quantos litros vão ser consumidos. 
o Custo total da viagem. 
3. Mostra um resumo da viagem. 

7 - Sistema de avaliação escolar 
1. Pede ao utilizador para introduzir as suas 3 notas de avaliação (0 a 20). 
2. Calcula a média. 
3. Mostra o resultado: 
o = 18: "Excelente" 
o = 16 e < 18: "Muito Bom" 
o = 14 e < 16: "Bom" 
o = 10 e < 14: "Suficiente" 
o < 10: "Reprovado" 

8 - Dada a lista, imprime todos os elementos 
numeros = [1, 5, 8, 12, 3] 

9 - Calcula a soma de todos os números numa lista 
valores = [10, 20, 30, 40] 

10 - Encontra e imprime apenas os números pares 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

11 - Encontra o maior número numa lista sem usar a função max() 
numeros = [45, 12, 78, 23, 56, 89, 34] 

12 – Calcula a média de cada sublista 
notas_turmas = [[85, 90, 78], [92, 88, 76, 95], [80, 85, 90, 87, 82]] 

13 - Encontra palavras que começam com vogal 
palavras = ["casa", "árvore", "elefante", "bola", "uva", "ovo", "mesa"] 

14 - Cria um programa que ajude a gerir o stock de uma loja simples. O 
programa deve: 
1. Mostrar um menu de 3 produtos disponíveis com o stock inicial (exemplo): 
o Produto A: 10 unidades 
o Produto B: 5 unidades 
o Produto C: 8 unidades 
2. Perguntar ao utilizador o que pretende fazer: 
o "Vender produto" 
o "Repor stock" 
o "Consultar stock" 
o "Sair" 
3. Se escolher "Vender produto": 
o Perguntar qual o produto (A, B ou C) 
o Perguntar quantas unidades pretende vender 
o Verificar se há stock suficiente: 
▪ Se sim, atualizar o stock e mostrar mensagem de sucesso 
▪ Se não, mostrar "Stock insuficiente!" 
4. Se escolher "Repor stock": 
o Perguntar qual o produto (A, B ou C) 
o Perguntar quantas unidades pretende adicionar 
o Atualizar o stock e mostrar mensagem de confirmação 
5. Se escolher "Consultar stock": 
o Mostrar o stock atual de todos os produtos 
