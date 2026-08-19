print("POKEMON BATTLE ARENA")

opcoes_iniciais = ["Bulbasaur", "Charmander", "Squirtle"]
for i in range(0,len(opcoes_iniciais)):
    print(i + 1, opcoes_iniciais[i])

escolha_inicial = int(input("Selecione seu inicial! \n 1 = Bulbasaur \n 2 = Charmander \n 3 = Squirtle"))
escolha_inicial -= 1

while escolha_inicial < 1 or escolha_inicial > 3:
    print("Opção inválida!")
    escolha_inicial = int(input("Selecione novamente: "))
    
if escolha_inicial == 0:
    print("Vamos lá, Bulbasaur!")
elif escolha_inicial == 1:
    print("Vamos lá, Charmander!")
elif escolha_inicial == 2:
    print("Vamos lá, Squirtle!")
else:
    print("Opção inválida!")

      
    