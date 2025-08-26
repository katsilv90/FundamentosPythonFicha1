print("Bem vindo ao Trip Planner!")

km = float(input("Qual a distância em 'km' que vai realizar? "))           #kilometros
cm = float(input("Qual o consumo médio (litros/100km) do seu carro? "))    #consumo médio
pr = float(input("Qual o preço atual do combustível por litro? "))         #preço combustível

k = int(km)       #para poder fazer print de um int em vez de float

ltconsum = (km*cm)/100      # fórmula dos litros que vão ser consumidos ----> litros consumidos = (distância x consumo médio)/100
ctotal = ltconsum*pr        # fórmula do custo total da viagem   -----------> custo total = litros consumidos x preço por litro

print(f"Vão ser consumidos {ltconsum}L durante a viagem de {k}km.\nO custo total será {ctotal: .2f}€")   # : .2f ----> para garantir 2 casas decimais